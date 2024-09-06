
# middleware.py
class ContentSecurityPolicyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # List of domains allowed to embed the website in an iframe
        allowed_domains = [
            "https://kpyx.co",
            "https://www.kpyx.co",
            "https://185.100.87.158:8000",
            # "https://localhost:8000",
            # "https://0.0.0.0:8000",
            "https://kpyx.io",
            "https://www.kpyx.io",
            "https://www.krmp.io",
            "https://krmp.io",
            # "https://localhost",
            "https://2krk.site",
            "https://portfolio-gzbf.onrender.com",
        ]

        # Generate the frame-ancestors directive for the Content-Security-Policy header
        frame_ancestors = ' '.join(allowed_domains)

        # Set the Content-Security-Policy header
        response['Content-Security-Policy'] = f"frame-ancestors {frame_ancestors}"

        return response
