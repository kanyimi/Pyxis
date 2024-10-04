
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
            "https://kpyx.io",
            "https://www.kpyx.io",
            "https://www.krmp.io",
            "https://krmp.io",
            "https://2krk.site",
            "https://portfolio-gzbf.onrender.com",
            "https://krm.gg",
            "https://knm.st",
            "https://2kkm.co",
            "https://2kk.site",
            "https://2kramp.site",
            "https://2kk.ac",
            "https://2kkn.ac",
            "https://2kkm.st",
            "https://torkrn.cc",
            "https://torkrn.co",
            "https://2krk.in",
            "https://2krm.st",
            "https://2knmp.cc",
            "https://kkn.st",
            "https://2kkn.st",
            "https://2kkn.top",
            "https://tkm.ac",
            "https://tkm.cx",
            "https://tkm.gg",
            "https://2kkm.mx",
            "https://2kn.io",
            "https://dkm.gg",
            "https://2kk.to",
            "https://2kk.is",
            "https://2kk.ai",
            "https://2kk.cx",
            "https://2kk.mx",
            "https://2kk.sh",
            "https://2kk.so",
            "https://knmp.cc",
            "https://knmp.st",
            "https://zerkalo-kra.cc",
            "https://zerkalokrn.cc",
            "https://dkm.ac",
            "https://kr2.ai",
            "https://kr2.me",
            "https://kr2.is",
            "https://km2.is",
            "https://4kra.co",
            "https://2kn.is",
            "https://4kr.co",
            "https://t.me",
            "https://web.telegram.org",
            "https://cyberrpg.gg",
            "https://cyberika.gg",
            "https://knmp.io",
            "https://krn.is",
            "https://install.kkrn.co",
            "https://cybercity.gg",
            "https://km2.ac",
            "https://cybertown.gg",
            "https://3km.ac",
            "https://3km.so",
            "https://3km.gg",
            "https://kn1.ac",
            "http://kn2.cx"
            "http://1kn.ac",
            "https://1kn.ac",
            "https://kn2.cx",
            "https://ddna.top",
            "https://kr2.nl"
        ]

        # Generate the frame-ancestors directive for the Content-Security-Policy header
        frame_ancestors = ' '.join(allowed_domains)


        response['Content-Security-Policy'] = f"frame-ancestors {frame_ancestors}"

        return response
