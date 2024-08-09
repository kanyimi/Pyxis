
(function() {
    // Create the iframe element
    var iframe = document.createElement('iframe');


    iframe.style.position = 'fixed';
    iframe.style.bottom = '20px';
    iframe.style.right = '20px';
    iframe.style.width = '80px';
    iframe.style.height = '80px';
    iframe.style.border = 'none';

    iframe.style.zIndex = '1000';
    iframe.style.transition = 'width 0.3s ease, height 0.3s ease';

    // Set the iframe source to the provided URL
    iframe.src = 'https://kpyx.co/home';

    // Append the iframe to the body of the host page
    document.body.appendChild(iframe);
    // Listen for messages from the iframe
    window.addEventListener('message', function(event) {
        // Optionally, check the origin for security reasons
        if (event.origin === 'https://kpyx.co') {
            // Check for the resize action and adjust iframe size
            if (event.data.action === 'resize') {
                iframe.style.width = event.data.width + 'px';
                iframe.style.height = event.data.height + 'px';
            }
        }
    }, false);
})();
