document.addEventListener('DOMContentLoaded', function() {
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');

    messageInput.addEventListener('input', function() {
        sendButton.disabled = messageInput.value.trim() === '';
    });

    messageInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            if (!sendButton.disabled) {
                sendMessage();
            }
        }
    });

    const modal = document.getElementById('feedback-modal');
    const span = document.getElementsByClassName('close')[0];
    const submitFeedbackButton = document.getElementById('submit-feedback');
    const feedbackText = document.getElementById('feedback-text');
    const feedbackMessageText = document.getElementById('feedback-message-text');

    span.onclick = function() {
        modal.style.display = 'none';
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }

    submitFeedbackButton.addEventListener('click', function() {
        const feedbackContent = feedbackText.value.trim();
        if (feedbackContent) {
            const botMessageContent = feedbackMessageText.textContent;
            submitFeedback(botMessageContent, feedbackContent);
        }
    });

    const welcomeMessageElement = document.querySelector('.bot-message .message-content');
    if (welcomeMessageElement) {
        typeMessage(welcomeMessageElement, welcomeMessageElement.textContent);
    }
});

function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
}

async function sendMessage() {
    const messageInput = document.getElementById('message-input');
    const messageText = messageInput.value.trim();
    if (messageText === '') return;

    messageInput.value = '';
    const sendButton = document.getElementById('send-button');
    sendButton.disabled = true;

    const messageList = document.getElementById('messages-list');
    const userMessage = document.createElement('li');
    userMessage.className = 'message user-message';

    const userMessageHeader = document.createElement('div');
    userMessageHeader.className = 'message-header';

    const userIcon = document.createElement('img');
    userIcon.src = 'static/img/chaticon/usrw.png';
    userIcon.alt = 'User';

    const userMessageTitle = document.createElement('span');
    userMessageTitle.textContent = 'Вы';

    const messageTime = document.createElement('span');
    messageTime.className = 'message-time';
    messageTime.textContent = formatDate(new Date().toISOString());

    userMessageHeader.appendChild(userIcon);
    userMessageHeader.appendChild(userMessageTitle);
    userMessageHeader.appendChild(messageTime);

    const userMessageContent = document.createElement('div');
    userMessageContent.className = 'message-content';
    userMessageContent.textContent = messageText;

    userMessage.appendChild(userMessageHeader);
    userMessage.appendChild(userMessageContent);
    messageList.appendChild(userMessage);

    messageList.scrollTop = messageList.scrollHeight;

    try {
        const response = await fetch('/send_message_to_external_api/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ content: messageText })
        });

        const data = await response.json();

        const botMessage = document.createElement('li');
        botMessage.className = 'message bot-message';

        const botMessageHeader = document.createElement('div');
        botMessageHeader.className = 'message-header';

        const botIcon = document.createElement('img');
        botIcon.src = 'static/img/chaticon/pyxw.png';
        botIcon.alt = 'Pyxis';

        const botMessageTitle = document.createElement('span');
        botMessageTitle.textContent = 'Pyxis';

        const botMessageTime = document.createElement('span');
        botMessageTime.className = 'message-time';
        botMessageTime.textContent = formatDate(new Date().toISOString());

        botMessageHeader.appendChild(botIcon);
        botMessageHeader.appendChild(botMessageTitle);
        botMessageHeader.appendChild(botMessageTime);

        const botMessageContent = document.createElement('div');
        botMessageContent.className = 'message-content';
        botMessageContent.textContent = data.response;

        botMessage.appendChild(botMessageHeader);
        botMessage.appendChild(botMessageContent);
        messageList.appendChild(botMessage);

        messageList.scrollTop = messageList.scrollHeight;

        typeMessage(botMessageContent, data.response);
    } catch (error) {
        console.error('Error:', error);
    }
}

function typeMessage(element, message) {
    let index = 0;
    const typingSpeed = 10;
    element.textContent = '';
    const interval = setInterval(() => {
        if (index < message.length) {
            element.textContent += message.charAt(index);
            index++;
        } else {
            clearInterval(interval);
        }
    }, typingSpeed);
}

function openFeedbackModal(messageContent) {
    const modal = document.getElementById('feedback-modal');
    const feedbackMessageText = document.getElementById('feedback-message-text');
    feedbackMessageText.textContent = messageContent;
    modal.style.display = 'block';
}

function submitFeedback(botMessageContent, feedbackContent) {
    fetch('/feedback/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: botMessageContent, feedback: feedbackContent })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            console.log('Feedback submitted successfully');
            const modal = document.getElementById('feedback-modal');
            modal.style.display = 'none';
        } else {
            console.error('Failed to submit feedback:', data.error);
        }
    })
    .catch(error => {
        console.error('Error submitting feedback:', error);
    });
}
