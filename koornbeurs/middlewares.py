from django.contrib import auth

class WebguiSessionMiddleware(object):
    def process_request(self, request):
        session_id = request.COOKIES.get('wgSession')
        if session_id:
            user = auth.authenticate(session_id=session_id)
            if user is not None:
                auth.login(request, user)

