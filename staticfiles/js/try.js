(function() {
    // Manually add the stylesheet(s) used by the widget
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'https://kpyx.co/static/css/widget.css';
    document.head.appendChild(link);

    // Function to load and execute external JavaScript files dynamically
    function loadExternalJS(src) {
        return new Promise((resolve, reject) => {
            var script = document.createElement('script');
            script.src = src;
            script.onload = resolve;
            script.onerror = reject;
            document.body.appendChild(script);  // Append to body instead of head
        });
    }

    // Fetch content from the API
    fetch('https://kpyx.co/home')
        .then(response => response.text())
        .then(htmlContent => {
            // Parse the fetched HTML content
            const parser = new DOMParser();
            const doc = parser.parseFromString(htmlContent, 'text/html');

            // Append the parsed content directly to the body (or another target element)
            while (doc.body.firstChild) {
                document.body.appendChild(doc.body.firstChild);
            }

            // Return a promise that resolves when DOM is ready
            return new Promise((resolve) => {
                if (document.readyState === 'complete' || document.readyState === 'interactive') {
                    resolve();
                } else {
                    document.addEventListener('DOMContentLoaded', resolve);
                }
            });
        })
        .then(() => {
            // Load external JavaScript file after DOM has been modified and is ready
            return loadExternalJS('https://kpyx.co/static/js/try1.js');
        })
        .then(() => {
            console.log('JavaScript file loaded and executed successfully.');
        })
        .catch(error => {
            console.error('Error fetching widget content or loading JavaScript:', error);
        });
})();
