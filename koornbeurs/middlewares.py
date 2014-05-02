from django.contrib import auth

class WebguiSessionMiddleware(object):
    def process_request(self, request):
        session_id = request.COOKIES.get('wgSession')
        if session_id:
            user = auth.authenticate(session_id=session_id)
            if user is None:
                auth.logout(request)
            else:
                auth.login(request, user)

