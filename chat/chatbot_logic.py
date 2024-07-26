import re
import requests
from .models import ChatHistory

def extract_user_name(message):
    match = re.search(r'\bMy name is (\w+)\b', message, re.IGNORECASE)
    if match:
        return match.group(1)
    return None

def handle_user_message(message, identifier):
    user_name = extract_user_name(message)
    if user_name:
        # Update or create attributes based on the identifier (username or session_key)
        ChatHistory.objects.filter(session_key=identifier).update_or_create(
            sender=identifier,
            defaults={'attributes': {'name': user_name}}
        )

    # Fetch stored attributes
    last_entry = ChatHistory.objects.filter(session_key=identifier).last()
    attributes = last_entry.attributes if last_entry else {}

    # Check if the message asks for the user's name
    if "name" in message.lower():
        if 'name' in attributes:
            return {'response': f"Your name is {attributes['name']}."}
        else:
            return {'response': "I don't know your name yet."}

    # Process the message with the external API or chatbot logic
    response = requests.post(
        'https://213.199.32.2',
        headers={'Content-Type': 'application/json'},
        json={'content': message},
        cert=(
            'C:/Users/User/OneDrive/Desktop/ca-certificates/client.crt',
            'C:/Users/User/OneDrive/Desktop/ca-certificates/client.key'
        ),
        verify=False
    )

    return response.json()
