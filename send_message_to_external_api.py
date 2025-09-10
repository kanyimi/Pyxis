from django.http import JsonResponse
from chat.models import Feedback, ChatHistory, APICallCount, ButtonClick
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import requests
import json
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
            CLIENT_KEY = '/etc/ssl/certs/client_key.key'
            CLIENT_CERT = '/etc/ssl/certs/client_cert.crt'
            CA_CERT = '/etc/ssl/certs/ca.crt'  # Путь к CA сертификату (если необходимо)
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
            print(f"Статус-код: {response.status_code}")

            if response.status_code == 500:
                bot_response = {
                    'response': "Упс. Кажется на сервере произошла ошибка. Повторите запрос через несколько минут"
                }
                print("Response from external API (500 error):", bot_response)
            else:
                bot_response = response.json()
                print("Response from external API:", bot_response)

                if 'response' in bot_response:
                    bot_response['response'] = bot_response['response'].replace('\\n', '\n').replace('\\\n',
                                                                                                     '\n').replace(
                        '\\\\n', '\n')

                    ChatHistory.objects.create(session_key=identifier, message=bot_response['response'], sender='bot')

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
