(function() {
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
        })
        .catch(error => {
            console.error('Error fetching widget content:', error);
        });
})();
