(function() {
    // Manually add the stylesheet(s) used by the widget
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'https://kpyx.co/static/css/try1.css'; // Replace with actual stylesheet URL
    document.head.appendChild(link);

    // Function to load and execute external JavaScript files dynamically
    function loadExternalJS(src) {
        return new Promise((resolve, reject) => {
            var script = document.createElement('script');
            script.src = src;
            script.onload = resolve;
            script.onerror = reject;
            document.head.appendChild(script);
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

            // Load external JavaScript file
            return loadExternalJS('https://kpyx.co/static/js/widget.js'); // Replace with actual JS URL
        })
        .then(() => {
            console.log('JavaScript file loaded successfully.');
        })
        .catch(error => {
            console.error('Error fetching widget content or loading JavaScript:', error);
        });
})();
