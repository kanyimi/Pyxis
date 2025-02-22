
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
        sendResizeToParent(440, 468);
    });

    closeWidgetButton.addEventListener('click', function() {
        supportWidget.style.display = 'none';
        openWidgetButton.style.display = 'block';
        sendResizeToParent(85, 85);
    });

    messageInput.addEventListener('input', function() {
        sendButton.disabled = messageInput.value.trim() === '';
    });



    messageInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            if (event.shiftKey || event.altKey) {

                return;
            } else {
                event.preventDefault();
                if (!sendButton.disabled) {
                    sendWidgetMessage();
                }
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

function sendResizeToParent(width, height) {
    window.parent.postMessage({ action: 'resize', width: width, height: height }, '*');
}

function displayWelcomeMessage() {
    const messageList = document.getElementById('widget-messages-list');
    const botMessage = document.createElement('li');
    botMessage.className = 'message bot-message';

    const botMessageContent = document.createElement('div');
    botMessageContent.className = 'message-content';

    const botIcon = document.createElement('img');
    botIcon.src = 'https://kpyx.io/static/img/chaticon/pyxw.png';
    botIcon.alt = 'Pyxis';
    botIcon.className = 'message-icon';

    const botMessageTitle = document.createElement('span');
    botMessageTitle.className = 'message-title';
    botMessageTitle.textContent = ' Pyxis: ';

    const botTextContent = document.createElement('span');
    botTextContent.className = 'text-content';

    botMessageContent.appendChild(botIcon);
    botMessageContent.appendChild(botMessageTitle);
    botMessageContent.appendChild(botTextContent);
    botMessage.appendChild(botMessageContent);
    messageList.prepend(botMessage);

     //const welcomeText = "Здравствуйте! Я Pyxis - искусственный интеллект, созданный командой KRAKEN для оперативной помощи нашим пользователям, покупателям и продавцам. Обращаю ваше внимание, что сейчас я нахожусь на стадии бета-тестирования, обучение - долгий процесс, но с вашей помощью он может пройти быстрее!";
    const welcomeText = "Привет! Я Pyxis — искусственный интеллект, созданный командой KRAKEN для оперативной помощи нашим пользователям, покупателям и продавцам. Я знаю всё о маркетплейсе KRAKEN, могу ответить на любые вопросы связанные с площадкой, психоактивными веществами, здоровьем и безопасностью. Кроме того, я могу подсказать код от домофона (в Москве и Санкт-Петербурге) или просто поддержать приятную беседу! Я уже многому научился, но продолжаю учиться и развиваться с вашей помощью!"

    typeMessage(botTextContent, welcomeText);
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

// Function to get a cookie by name
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Function to set a cookie
function setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = "expires=" + date.toUTCString();
    document.cookie = name + "=" + (value || "") + ";" + expires + ";path=/";
}

// Function to generate a UUID (for session ID)
function generateUUID() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        const r = Math.random() * 16 | 0, v = c === 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}

// Check if session ID exists in cookies, if not create one
let sessionId = getCookie('widget_session_id');
if (!sessionId) {
    sessionId = generateUUID();
    setCookie('widget_session_id', sessionId, 14);  // 14 days expiration
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

    const userMessageContent = document.createElement('div');
    userMessageContent.className = 'message-content';

    const userIcon = document.createElement('img');
    userIcon.src = 'https://kpyx.io/static/img/chaticon/usrw.png';
    userIcon.alt = 'User';
    userIcon.className = 'message-icon';

    const userMessageTitle = document.createElement('span');
    userMessageTitle.className = 'message-title';
    userMessageTitle.textContent = ' Вы: ';

    const userTextContent = document.createElement('span');
    userTextContent.className = 'text-content';
    userTextContent.innerHTML = messageText.replace(/\n/g, '<br>');

    userMessageContent.appendChild(userIcon);
    userMessageContent.appendChild(userMessageTitle);
    userMessageContent.appendChild(userTextContent);
    userMessage.appendChild(userMessageContent);
    messageList.appendChild(userMessage);

    const typingIndicator = document.createElement('li');
    typingIndicator.id = 'widget-typing-indicator';
    typingIndicator.className = 'message typing-indicator';
    messageList.appendChild(typingIndicator);

    messageList.scrollTop = messageList.scrollHeight;

    // Setting up the timeout for the fetch request
    const controller = new AbortController();
    const signal = controller.signal;
    const timeoutId = setTimeout(() => controller.abort(), 180000);  // 180 seconds (3 minutes)

    try {
        const formattedMessage = `${messageText.replace(/\n/g, '')}`;

        const response = await fetch('/api/send_message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': '721bap7nan-4891-b1ed-706e9ad7970f_50jsh291g-636f'
            },
            body: JSON.stringify({
                content: formattedMessage,
                message_id: 'unique_message_270',
                session_id: sessionId
            }),
            signal: signal // Ensure this is correctly set
        });

        clearTimeout(timeoutId);  // Clear the timeout if the request completes in time

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();

        typingIndicator.remove();

        if (data.response) {
            const botMessage = document.createElement('li');
            botMessage.className = 'message bot-message';

            const botMessageContent = document.createElement('div');
            botMessageContent.className = 'message-content';

            const botIcon = document.createElement('img');
            botIcon.src = 'https://kpyx.io/static/img/chaticon/pyxw.png';
            botIcon.alt = 'Pyxis';
            botIcon.className = 'message-icon';

            const botMessageTitle = document.createElement('span');
            botMessageTitle.className = 'message-title';
            botMessageTitle.textContent = 'Pyxis: ';

            const botTextContent = document.createElement('span');
            botTextContent.className = 'text-content';

            botMessageContent.appendChild(botIcon);
            botMessageContent.appendChild(botMessageTitle);
            botMessageContent.appendChild(botTextContent);
            botMessage.appendChild(botMessageContent);
            messageList.appendChild(botMessage);

            messageList.scrollTop = messageList.scrollHeight;

            typeMessage(botTextContent, data.response);

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

            goodButton.addEventListener('click', function() {
                if (goodButton.dataset.submitted === 'true') return;
                goodButton.style.color = '#000000';
                submitFeedback(botMessageContent.textContent, '', 'positive');
                goodButton.dataset.submitted = 'true';
            });

            badButton.addEventListener('click', function() {
                if (badButton.dataset.submitted === 'true') return;
                badButton.style.color = '#000000';
                feedbackMessageText.textContent = botTextContent.textContent;
                modal.style.display = 'block';
                badButton.dataset.submitted = 'true';
            });
        }
    } catch (error) {
        if (error.name === 'AbortError') {
            console.error('Fetch request timed out');
        } else {
            console.error('Fetch request failed:', error);
        }
        alert('Произошла ошибка при запросе. Пожалуйста, проверьте консоль для получения дополнительной информации.');
        typingIndicator.remove();
    }
}


function submitFeedback(botMessage, feedback, type) {
    fetch('/api/submit_feedback/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': '721bap7nan-4891-b1ed-706e9ad7970f_50jsh291g-636f'
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
        const response = await fetch('/api/submit_feedback/', {
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
