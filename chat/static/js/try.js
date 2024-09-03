(function() {
    // Function to fetch the widget HTML content
    function fetchWidgetHTML() {
        return fetch('https://kpyx.co/testwidget') // Use the actual URL of your widget HTML
            .then(response => response.text())
            .then(htmlContent => {
                const parser = new DOMParser();
                const doc = parser.parseFromString(htmlContent, 'text/html');

                // Append the parsed content directly to the body (or another target element)
                while (doc.body.firstChild) {
                    document.body.appendChild(doc.body.firstChild);
                }
            });
    }

    // Function to initialize the widget
    function initializeWidget() {
        fetchWidgetHTML()
        .then(() => {
            console.log('Widget initialized successfully.');
        })
        .catch(error => {
            console.error('Error initializing widget:', error);
        });
    }

    // Start the widget initialization
    initializeWidget();
})();
