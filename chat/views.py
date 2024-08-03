import requests
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .models import Feedback, ChatHistory
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages



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
            data = json.loads(request.body)

            # Determine user identifier and sender
            if request.user.is_authenticated:
                identifier = request.user.username
                sender = "user"
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
            # history_text += f"USER: {formatted_content}"
            print("chat history: ", history_text)
            # Truncate history_text if it exceeds 5000 characters
            if len(history_text) > 5000:
                # Keep the most recent 5000 characters
                history_text = history_text[-5000:]
            print("truncated chat history: ", history_text)

            # Create a new chat history entry for the user message
            ChatHistory.objects.create(session_key=identifier, message=formatted_content, sender = sender)

            # Prepare the request payload
            payload = {
                'content': f"{history_text}USER: {formatted_content}",
                'message_id': data.get('message_id', '')
            }

            # Send the request to the external API
            response = requests.post(
                'https://213.199.32.2',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': '50jsh291g-636f-4891-b1ed-706e9ad7970f_721bap7nan'
                },
                json=payload,
                cert=('C:/Users/User/OneDrive/Desktop/ca-certificates/client.crt',
                      'C:/Users/User/OneDrive/Desktop/ca-certificates/client.key'),
                verify=False
            )

            bot_response = response.json()

            if 'response' in bot_response:
                bot_response['response'] = bot_response['response'].replace('\\n', '\n').replace('\\\n', '\n').replace('\\\\n', '\n')

                # Create a new chat history entry for the bot response
                ChatHistory.objects.create(session_key=identifier, message=bot_response['response'], sender='bot')

            return JsonResponse(bot_response, status=response.status_code)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except requests.RequestException as e:
            return JsonResponse({'error': f"Request failed: {str(e)}"}, status=500)
    else:
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

def testwidget(request):
    return render(request, "chat/testwidget.html")
