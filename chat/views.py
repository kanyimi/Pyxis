import requests
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Feedback, ChatHistory

def index(request):
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    chat_history = ChatHistory.objects.filter(session_key=session_key).order_by('created_at')
    if not chat_history.exists():
        welcome_text = ("hello Здравствуйте! Я Pyxis - искусственный интеллект, созданный командой KRAKEN для оперативной помощи нашим пользователям, покупателям и продавцам. "
                        "Обращаю ваше внимание, что сейчас я нахожусь на стадии бета-тестирования, обучение - долгий процесс, но с вашей помощью он может пройти быстрее!")
        ChatHistory.objects.create(session_key=session_key, message=welcome_text, sender='bot')

    context = {
        "chat_history": chat_history
    }
    return render(request, 'chat/index.html', context)

@csrf_exempt
def send_message_to_external_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            session_key = request.session.session_key or request.session.create()
            # Save user message to ChatHistory
            ChatHistory.objects.create(session_key=session_key, message=data['content'], sender='user')

            response = requests.post(
                'https://213.199.32.2',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': '50jsh291g-636f-4891-b1ed-706e9ad7970f_721bap7nan'
                },
                json=data,
                cert=('C:/Users/User/OneDrive/Desktop/ca-certificates/client.crt', 'C:/Users/User/OneDrive/Desktop/ca-certificates/client.key'),
                verify=False
            )

            bot_response = response.json()
            if 'response' in bot_response:
                # Save bot message to ChatHistory
                ChatHistory.objects.create(session_key=session_key, message=bot_response['response'], sender='bot')
            return JsonResponse(bot_response, status=response.status_code)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except requests.RequestException as e:
            return JsonResponse({'error': f"Request failed: {str(e)}"}, status=500)
    else:
        return JsonResponse({'error': 'This method is not allowed'}, status=405)



@csrf_exempt
def submit_feedback(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            bot_message = data.get('botMessage')
            feedback = data.get('feedback', None)
            feedback_type = data.get('feedback_type', 'negative')

            if not bot_message:
                return JsonResponse({'success': False, 'message': 'Bot message is required'}, status=400)

            Feedback.objects.create(bot_message=bot_message, feedback=feedback, feedback_type=feedback_type)
            return JsonResponse({'success': True, 'message': 'Feedback saved'})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)
