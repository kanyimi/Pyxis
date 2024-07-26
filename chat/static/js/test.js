let modal, span, submitFeedbackButton, feedbackText, feedbackMessageText;

document.addEventListener('DOMContentLoaded', function() {
    displayWelcomeMessage();

    const messageInput = document.getElementById('widget-message-input');
    const sendButton = document.getElementById('widget-send-button');
    const openWidgetButton = document.getElementById('open-widget-btn');
    const closeWidgetButton = document.getElementById('close-widget-btn');
    const supportWidget = document.getElementById('support-widget');

    openWidgetButton.addEventListener('click', function() {
        supportWidget.style.display = 'flex';
        openWidgetButton.style.display = 'none';
    });

    closeWidgetButton.addEventListener('click', function() {
        supportWidget.style.display = 'none';
        openWidgetButton.style.display = 'block';
    });

    messageInput.addEventListener('input', function() {
        sendButton.disabled = messageInput.value.trim() === '';
    });

    messageInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            if (!sendButton.disabled) {
                sendWidgetMessage();
            }
        }
    });

    // Инициализация элементов, связанных с модальным окном
    modal = document.getElementById('feedback-modal');
    span = document.getElementsByClassName('close')[0];
    submitFeedbackButton = document.getElementById('submit-feedback');
    feedbackText = document.getElementById('feedback-text');
    feedbackMessageText = document.getElementById('feedback-message-text');

    // Закрытие модального окна
    span.onclick = function() {
        modal.style.display = 'none';
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }

    // Отправка обратной связи
    submitFeedbackButton.addEventListener('click', function() {
        const feedbackContent = feedbackText.value.trim();
        const botMessageContent = feedbackMessageText.textContent;
        submitFeedback(botMessageContent, feedbackContent, 'negative');
    });
});

function displayWelcomeMessage() {
    const messageList = document.getElementById('widget-messages-list');
    const botMessage = document.createElement('li');
    botMessage.className = 'message bot-message';

    const botMessageHeader = document.createElement('div');
    botMessageHeader.className = 'message-header';

    const botIcon = document.createElement('img');
    botIcon.src = 'https://kpyx.co/static/img/chaticon/pyxw.png';
    botIcon.alt = 'Pyxis';

    const botMessageTitle = document.createElement('span');
    botMessageTitle.textContent = 'Pyxis';

    botMessageHeader.appendChild(botIcon);
    botMessageHeader.appendChild(botMessageTitle);

    const botMessageContent = document.createElement('div');
    botMessageContent.className = 'message-content';

    botMessage.appendChild(botMessageHeader);
    botMessage.appendChild(botMessageContent);
    messageList.appendChild(botMessage);

    const welcomeText = "Здравствуйте! Я Pyxis - искусственный интеллект, созданный командой KRAKEN для оперативной помощи нашим пользователям, покупателям и продавцам. Обращаю ваше внимание, что сейчас я нахожусь на стадии бета-тестирования, обучение - долгий процесс, но с вашей помощью он может пройти быстрее!";
    typeMessage(botMessageContent, welcomeText);
}

function typeMessage(element, text, callback) {
    let index = 0;
    const boldRegex = /\*\*(.*?)\*\*/g;
    const parts = text.split(boldRegex);
    let currentPart = 0;
    let currentPartLength = parts[currentPart].length;
    let isBold = false;

    function type() {
        if (currentPart < parts.length) {
            if (index < currentPartLength) {
                if (parts[currentPart].charAt(index) === '\n') {
                    element.innerHTML += '<br>';
                } else {
                    if (isBold) {
                        element.innerHTML += `<strong>${parts[currentPart].charAt(index)}</strong>`;
                    } else {
                        element.innerHTML += parts[currentPart].charAt(index);
                    }
                }
                index++;
                setTimeout(type, 20);
            } else {
                currentPart++;
                if (currentPart < parts.length) {
                    isBold = !isBold;
                    index = 0;
                    currentPartLength = parts[currentPart].length;
                    setTimeout(type, 20);
                } else if (callback) {
                    callback();
                }
            }
        } else if (callback) {
            callback();
        }
    }

    type();
}

async function sendWidgetMessage() {
    const messageInput = document.getElementById('widget-message-input');
    const messageText = messageInput.value.trim();
    if (messageText === '') return;

    messageInput.value = '';
    const sendButton = document.getElementById('widget-send-button');
    sendButton.disabled = true;

    const messageList = document.getElementById('widget-messages-list');
    const userMessage = document.createElement('li');
    userMessage.className = 'message user-message';

    const userMessageHeader = document.createElement('div');
    userMessageHeader.className = 'message-header';

    const userIcon = document.createElement('img');
    userIcon.src = 'https://kpyx.co/static/img/chaticon/usrw.png';
    userIcon.alt = 'User';

    const userMessageTitle = document.createElement('span');
    userMessageTitle.textContent = 'Вы';

    userMessageHeader.appendChild(userIcon);
    userMessageHeader.appendChild(userMessageTitle);

    const userMessageContent = document.createElement('div');
    userMessageContent.className = 'message-content';
    userMessageContent.innerHTML = messageText.replace(/\n/g, '<br>');

    userMessage.appendChild(userMessageHeader);
    userMessage.appendChild(userMessageContent);
    messageList.insertBefore(userMessage, messageList.firstChild);

    const typingIndicator = document.createElement('li');
    typingIndicator.id = 'widget-typing-indicator';
    typingIndicator.className = 'message typing-indicator';
    messageList.insertBefore(typingIndicator, messageList.firstChild);

    messageList.scrollTop = messageList.scrollHeight;

    try {
        const response = await fetch('https://kpyx.co/api/send_message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': '50jsh291g-636f-4891-b1ed-706e9ad7970f_721bap7nan'
            },
            body: JSON.stringify({
                content: messageText,
                message_id: 'unique_message_270'
            })
        });
        const data = await response.json();

        typingIndicator.remove();

        if (data.response) {
            const botMessage = document.createElement('li');
            botMessage.className = 'message bot-message';

            const botMessageHeader = document.createElement('div');
            botMessageHeader.className = 'message-header';

            const botIcon = document.createElement('img');
            botIcon.src = 'https://kpyx.co/static/img/chaticon/pyxw.png';
            botIcon.alt = 'Pyxis';

            const botMessageTitle = document.createElement('span');
            botMessageTitle.textContent = 'Pyxis';

            botMessageHeader.appendChild(botIcon);
            botMessageHeader.appendChild(botMessageTitle);

            const botMessageContent = document.createElement('div');
            botMessageContent.className = 'message-content';

            botMessage.appendChild(botMessageHeader);
            botMessage.appendChild(botMessageContent);
            messageList.insertBefore(botMessage, messageList.firstChild);

            // Добавление кнопок "палец вверх" и "палец вниз"
            const feedbackButtons = document.createElement('div');
            feedbackButtons.className = 'feedback-buttons';

            const goodButton = document.createElement('i');
            goodButton.className = 'fa fa-thumbs-up';
            goodButton.dataset.submitted = 'false';

            const badButton = document.createElement('i');
            badButton.className = 'fa fa-thumbs-down';
            badButton.dataset.submitted = 'false';

            feedbackButtons.appendChild(goodButton);
            feedbackButtons.appendChild(badButton);
            botMessage.appendChild(feedbackButtons);

            messageList.scrollTop = messageList.scrollHeight;

            typeMessage(botMessageContent, data.response);

            // Обработчики событий для кнопок обратной связи
            goodButton.addEventListener('click', function() {
                if (goodButton.dataset.submitted === 'true') return;
                goodButton.style.color = '#000000';
                submitFeedback(botMessageContent.textContent, '', 'positive');
                goodButton.dataset.submitted = 'true';
            });

            badButton.addEventListener('click', function() {
                if (badButton.dataset.submitted === 'true') return;
                badButton.style.color = '#000000';
                feedbackMessageText.textContent = botMessageContent.textContent;
                modal.style.display = 'block';
                badButton.dataset.submitted = 'true';
            });
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Произошла ошибка при запросе. Пожалуйста, проверьте консоль для получения дополнительной информации.');
        typingIndicator.remove();
    }
}

function submitFeedback(botMessage, feedback, type) {
    fetch('https://kpyx.co/api/submit_feedback', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': '50jsh291g-636f-4891-b1ed-706e9ad7970f_721bap7nan'
        },
        body: JSON.stringify({
            bot_message: botMessage,
            feedback: feedback,
            feedback_type: type
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Feedback submitted successfully:', data);
    })
    .catch(error => {
        console.error('Error submitting feedback:', error);
    });
}

async function submitFeedback(botMessageContent, feedbackContent, feedbackType) {
    try {
        const response = await fetch('https://kpyx.co/api/submit_feedback/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                botMessage: botMessageContent,
                feedback: feedbackContent,
                feedback_type: feedbackType
            })
        });

        if (response.ok) {
            alert('Обратная связь успешно отправлена');
            feedbackText.value = '';
            modal.style.display = 'none';
        } else {
            alert('Не удалось отправить обратную связь');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Произошла ошибка при отправке обратной связи. Пожалуйста, проверьте консоль для получения дополнительной информации.');
    }
}
