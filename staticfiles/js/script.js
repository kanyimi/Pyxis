// Объявление переменных на верхнем уровне
let modal, span, submitFeedbackButton, feedbackText, feedbackMessageText;

document.addEventListener('DOMContentLoaded', function() {
    // Call the function to display the welcome message
    displayWelcomeMessage();

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

    // Modal window elements initialization
    modal = document.getElementById('feedback-modal');
    span = document.getElementsByClassName('close')[0];
    submitFeedbackButton = document.getElementById('submit-feedback');
    feedbackText = document.getElementById('feedback-text');
    feedbackMessageText = document.getElementById('feedback-message-text');

    // Modal window close
    span.onclick = function() {
        modal.style.display = 'none';
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }

    // Feedback submission
    submitFeedbackButton.addEventListener('click', function() {
        const feedbackContent = feedbackText.value.trim();
        const botMessageContent = feedbackMessageText.textContent;
        submitFeedback(botMessageContent, feedbackContent, 'negative');
    });
});

function displayWelcomeMessage() {
    const welcomeMessageDiv = document.getElementById('welcome-message');
    const botMessage = document.createElement('div');
    botMessage.className = 'message bot-message';

    const botMessageHeader = document.createElement('div');
    botMessageHeader.className = 'message-header';

    const botIcon = document.createElement('img');
    botIcon.src = 'static/img/chaticon/pyxw.png';
    botIcon.alt = 'Pyxis';

    const botMessageTitle = document.createElement('span');
    botMessageTitle.textContent = 'Pyxis';

    botMessageHeader.appendChild(botIcon);
    botMessageHeader.appendChild(botMessageTitle);

    const botMessageContent = document.createElement('div');
    botMessageContent.className = 'message-content';
    botMessage.appendChild(botMessageHeader);
    botMessage.appendChild(botMessageContent);
    welcomeMessageDiv.appendChild(botMessage);

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
    userMessageTitle.innerHTML = `Вы: ${messageText.replace(/\n/g, '<br>')}`;

    userMessageHeader.appendChild(userIcon);
    userMessageHeader.appendChild(userMessageTitle);

    userMessage.appendChild(userMessageHeader);
    messageList.appendChild(userMessage);

    const typingIndicator = document.createElement('li');
    typingIndicator.id = 'typing-indicator';
    typingIndicator.className = 'message typing-indicator';
    messageList.appendChild(typingIndicator);

    messageList.scrollTop = messageList.scrollHeight;

    try {
        const formattedMessage = `${messageText.replace(/\n/g, '')}`;
        console.log(formattedMessage)
        const response = await fetch('/api/send_message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': '50jsh291g-636f-4891-b1ed-706e9ad7970f_721bap7nan'
            },
            body: JSON.stringify({
                content: formattedMessage,
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
            botIcon.src = 'static/img/chaticon/pyxw.png';
            botIcon.alt = 'Pyxis';

            const botMessageTitle = document.createElement('span');
            botMessageTitle.innerHTML = `Pyxis: ${data.response.replace(/\n/g, '<br>')}`;


            const botMessageContent = document.createElement('div');
            botMessageContent.className = 'message-content';
            botMessageHeader.appendChild(botIcon);
            botMessageHeader.appendChild(botMessageTitle);

            botMessage.appendChild(botMessageHeader);
            botMessage.appendChild(botMessageContent);
            messageList.appendChild(botMessage);

            // Add feedback buttons
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
//            typeMessage(botMessageContent, data.response);
            // Add event listeners for feedback buttons
            goodButton.addEventListener('click', function() {
                if (goodButton.dataset.submitted === 'true') return;
                goodButton.style.color = '#000000';
                submitFeedback(botMessageTitle.textContent, '', 'positive');
                goodButton.dataset.submitted = 'true';
            });

            badButton.addEventListener('click', function() {
                if (badButton.dataset.submitted === 'true') return;
                badButton.style.color = '#000000';
                feedbackMessageText.textContent = botMessageTitle.textContent;
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
    fetch('/api/submit_feedback', {
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
        const response = await fetch('/api/submit_feedback/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                botMessage: botMessageContent,
                feedback: feedbackContent,
                feedback_type: feedbackType  // Указываем тип отзыва
            })
        });

        if (response.ok) {
            alert('Обратная связь успешно отправлена');
            feedbackText.value = '';  // Очистка текста в модальном окне после успешной отправки
            modal.style.display = 'none';  // Закрытие модального окна, если оно было открыто
        } else {
            alert('Не удалось отправить обратную связь');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Произошла ошибка при отправке обратной связи. Пожалуйста, проверьте консоль для получения дополнительной информации.');
    }
}


document.addEventListener("DOMContentLoaded", function() {
    const lines = document.querySelectorAll(".line");

    lines.forEach(line => {
        const totalWords = 1; // Уменьшаем количество слов
        const wordElements = [];

        for (let i = 0; i < totalWords; i++) {
            const word = document.createElement('div');
            word.classList.add('word');
            word.style.opacity = 0; // Устанавливаем начальное значение opacity в 0
            wordElements.push(word);
            line.appendChild(word);
        }

        function generateWord(wordElement) {
            const letters = "pyxis".split('');
            let letterIndex = 0;

            const animateLetter = () => {
                wordElement.innerText = letters[letterIndex];
                wordElement.style.opacity = 1;
                setTimeout(() => { wordElement.style.opacity = 0; }, 1600); // Замедляем исчезновение буквы

                letterIndex = (letterIndex + 1) % letters.length;
                requestAnimationFrame(() => {
                    setTimeout(animateLetter, 400); // Замедляем смену буквы
                });
            };
            animateLetter();
        }

        // Добавляем случайную задержку для каждой линии
        const randomDelay = Math.random() * 20; // случайная задержка от 0 до 20 секунд
        line.style.animationDelay = `${randomDelay}s`;

        wordElements.forEach((wordElement, index) => {
            setTimeout(() => {
                generateWord(wordElement);
            }, randomDelay * 1000 + index * 2000); // начинаем анимацию после случайной задержки
        });
    });
});



document.addEventListener('DOMContentLoaded', function() {
    const navItems = document.querySelectorAll('.navigation span');

    navItems.forEach(function(item) {
        const img = item.querySelector('img');
        const tooltipText = img.getAttribute('alt');

        item.addEventListener('mouseenter', function(event) {
            if (document.querySelector('.navigation').classList.contains('active')) {
                const tooltip = document.createElement('div');
                tooltip.className = 'tooltip';
                tooltip.textContent = tooltipText;
                document.body.appendChild(tooltip);

                const updateTooltipPosition = (e) => {
                    tooltip.style.left = e.pageX + 'px';
                    tooltip.style.top = (e.pageY + 20) + 'px'; // Смещение на 20px ниже курсора
                };

                updateTooltipPosition(event);

                item.addEventListener('mousemove', updateTooltipPosition);

                item.addEventListener('mouseleave', function() {
                    document.body.removeChild(tooltip);
                }, { once: true });
            }
        });
    });
});

