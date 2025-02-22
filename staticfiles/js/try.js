(function() {
    // Manually add the stylesheet(s) used by the widget
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'https://kpyx.io/static/css/widget.css'; // Replace with actual stylesheet URL
    document.head.appendChild(link);

    // Fetch content from the API
    fetch('https://kpyx.io/testwidget')
        .then(response => response.text())
        .then(htmlContent => {
            // Parse the fetched HTML content
            const parser = new DOMParser();
            const doc = parser.parseFromString(htmlContent, 'text/html');

            // Append the parsed content directly to the body (or another target element)
            while (doc.body.firstChild) {
                document.body.appendChild(doc.body.firstChild);
            }
        })
        .catch(error => {
            console.error('Error fetching widget content:', error);
        });
})();
