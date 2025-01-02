
let modal, span, submitFeedbackButton, feedbackText, feedbackMessageText;

document.addEventListener('DOMContentLoaded', function() {


    const messageInput = document.getElementById('widget-message-input');
    const sendButton = document.getElementById('widget-send-button');
    const openWidgetButton = document.getElementById('open-widget-btn');
    const closeWidgetButton = document.getElementById('close-widget-btn');
    const supportWidget = document.getElementById('support-widget');
    const incrementCountUrl = openWidgetButton.getAttribute('data-url');

    openWidgetButton.addEventListener('click', function() {
//        supportWidget.style.display = 'flex';
//        openWidgetButton.style.display = 'none';
//        sendResizeToParent(440, 468);
          window.open("https://t.me/Pyxis_K_bot", "_blank");
                fetch(incrementCountUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({})
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Button click count incremented:', data);
        })
        .catch(error => {
            console.error('Error incrementing button click count:', error);
        });
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





//



