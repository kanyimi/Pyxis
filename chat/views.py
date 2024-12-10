import requests
import json

from django.db.models import Sum
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .models import Feedback, ChatHistory, APICallCount, ButtonClick
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.utils import timezone


def index(request):
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    identifier = request.user.username if request.user.is_authenticated else session_key
    chat_history = ChatHistory.objects.filter(session_key=identifier).order_by('created_at')

    # Determine sender type
    for chat in chat_history:
        if chat.sender == 'user':
            chat.sender_type = 'user'
        else:
            chat.sender_type = 'bot'

    context = {
        "chat_history": chat_history,
    }
    return render(request, 'chat/index.html', context)




@csrf_exempt
def send_message_to_external_api(request):
    if request.method == 'POST':
        try:
            # Increment call count
            call_count, created = APICallCount.objects.get_or_create(function_name='send_message_to_external_api')
            call_count.count += 1
            call_count.last_called = timezone.now()
            call_count.save()

            is_widget_request = request.headers.get('X-Widget-Request', False)
            data = json.loads(request.body)

            # Determine user identifier and sender
            if request.user.is_authenticated:
                identifier = request.user.username
                sender = "user"
            else:
                session_id = data.get("session_id")
                if session_id:
                    print("session ID: ", session_id)
                    identifier = session_id
                else:
                    if not request.session.session_key:
                        request.session.create()
                    identifier = request.session.session_key
                sender = 'user'

            # Retrieve chat history for the identifier
            history = ChatHistory.objects.filter(session_key=identifier).order_by('created_at')
            history_text = ""

            # Format the chat history
            for entry in history:
                if entry.sender == 'user':
                    history_text += f"\n\nUSER: {entry.message} "
                elif entry.sender == 'bot':
                    history_text += f"\n\nASSISTANT: {entry.message} "

            # Format the current user message
            formatted_content = data['content'].replace('\\n', '\n').replace('\\\n', '\n').replace('\\\\n', '\n')
            history_text += f"\n\nUSER: {formatted_content}"
            print("chat history: ", history_text)
            print("length chat history: ", len(history_text))

            if len(history_text) > 5000:
                history_text = history_text[-5000:]

            # Находим индекс первого сообщения пользователя
            first_user_message_index = history_text.find("USER:")

            # Если сообщение пользователя найдено, смещаем историю
            if first_user_message_index != -1:
                # Обрезаем историю до первого сообщения пользователя
                history_text = history_text[first_user_message_index:]

            print("truncated chat history: ", history_text)
            print("length truncated chat history: ", len(history_text))

            # Create a new chat history entry for the user message
            ChatHistory.objects.create(session_key=identifier, message=formatted_content, sender = sender)

            # Prepare the request payload
            payload = {
                'content': history_text,
                'message_id': data.get('message_id', 'unique_message_270')
            }
            # Путь к клиентскому сертификату и ключу
            CLIENT_KEY = './client_key.key'
            CLIENT_CERT = './client_cert.crt'
            CA_CERT = './ca.crt'  # Путь к CA сертификату (если необходимо)
            # Send the request to the external API
            response = requests.post(
                'https://38.180.199.37:8443/omnia',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': '721bap7nan-4891-b1ed-706e9ad7970f_50jsh291g-636f'
                },
                json=payload,
                cert=(CLIENT_CERT, CLIENT_KEY),

                verify=False,
                timeout=180
            )
            bot_response = response.json()
            print("Response from external API:", bot_response)

            if 'response' in bot_response:
                bot_response['response'] = bot_response['response'].replace('\\n', '\n').replace('\\\n', '\n').replace(
                    '\\\\n', '\n')

                # Save the bot's response in chat history
                ChatHistory.objects.create(session_key=identifier, message=bot_response['response'], sender='bot')
            print(f"Статус-код: {response.status_code}")
            return JsonResponse(bot_response, status=response.status_code)
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except requests.RequestException as e:
            print(f"Request Error: {e}")
            return JsonResponse({'error': f"Request failed: {str(e)}"}, status=500)
        except Exception as e:
            print(f"Unexpected Error: {e}")
            return JsonResponse({'error': f"An unexpected error occurred: {str(e)}"}, status=500)
        else:
            print("Invalid HTTP method:", request.method)
            return JsonResponse({'error': 'This method is not allowed'}, status=405)


def home(request):
    return render(request, "chat/home.html")
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


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'authenticate/register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('index')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'authenticate/login.html', {'form': form})
@csrf_exempt
def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')

def telegrambot(request):
    return render(request, "chat/telegrambot.html")

def trafick(request):
    apicall_count = APICallCount.objects.aggregate(total_count=Sum('count'))['total_count'] or 0

    # Get the ButtonClick count
    button_click = ButtonClick.objects.first()  # Assuming you only have one instance
    button_click_count = button_click.count if button_click else 0
    context ={
            "apicall_count": apicall_count,
            "button_click_count": button_click_count,

    }
    return render(request, "chat/trafick.html", context)

@csrf_exempt
def increment_count(request):
    if request.method == 'POST':
        button_click, created = ButtonClick.objects.get_or_create(id=1)
        button_click.count += 1
        button_click.save()
        return JsonResponse({'count': button_click.count})
    return JsonResponse({'error': 'Invalid request'}, status=400)