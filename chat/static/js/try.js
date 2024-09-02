(function() {
    // Function to create and append elements
    function createElement(tagName, className, parentElement) {
        const element = document.createElement(tagName);
        if (className) element.className = className;
        if (parentElement) parentElement.appendChild(element);
        return element;
    }

    // Create container for the widget
    const container = createElement('div', 'kpyx-widget-container', document.body);

    // Set initial styles for the container
    container.style.position = 'fixed';
    container.style.bottom = '20px';
    container.style.right = '20px';
    container.style.width = '85px';
    container.style.height = '85px';
    container.style.zIndex = '1000';
    container.style.transition = 'width 0.3s ease, height 0.3s ease';

    // Create loading indicator
    const loader = createElement('div', 'kpyx-loader', container);
    loader.innerHTML = '<span>Loading...</span>';

    // Fetch content from API
    fetch('https://kpyx.co/home')
        .then(response => response.text())
        .then(htmlContent => {
            // Remove loader
            loader.remove();

            // Parse HTML content
            const parser = new DOMParser();
            const doc = parser.parseFromString(htmlContent, 'text/html');

            // Append parsed content to container
            while (doc.body.firstChild) {
                container.appendChild(doc.body.firstChild);
            }

            // Add event listener for resize messages
            window.addEventListener('message', handleResizeMessage, false);
        })
        .catch(error => {
            console.error('Error fetching widget content:', error);
            loader.textContent = 'Failed to load widget.';
        });

    function handleResizeMessage(event) {
        if (event.origin === 'https://kpyx.co' && event.data.action === 'resize') {
            container.style.width = event.data.width + 'px';
            container.style.height = event.data.height + 'px';
        }
    }
})();
