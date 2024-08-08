(function() {
    // Create the container for the iframe
    var container = document.createElement('div');
    container.style.position = 'fixed';
    container.style.bottom = '20px';
    container.style.right = '20px';
    container.style.width = '60px';
    container.style.height = '60px';
    container.style.zIndex = '1000';
    container.style.overflow = 'hidden';
    container.style.background = 'transparent';

        // Create the iframe
    var chatIframe = document.createElement('iframe');
    chatIframe.src = 'https://kpyx.co/home';
    chatIframe.style.width = '100%';
    chatIframe.style.height = '100%';
    chatIframe.style.border = 'none';
    chatIframe.style.background = 'transparent';

    // Append the iframe to the container
    container.appendChild(chatIframe);

    // Append the container to the body
    document.body.appendChild(container);
})();
