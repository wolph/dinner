import models
from django.contrib.auth import models as auth_models

class WebguiSessionBackend(object):
    def authenticate(self, session_id=None):
        try:
            session = models.UserSession.objects.get(session_id=session_id)
        except models.UserSession.DoesNotExist:
            return

        try:
            webgui_user = session.user
            if webgui_user.id not in ('1', '3'):
                return webgui_user.get_django_user()
        except models.User.DoesNotExist:
            return

    def get_user(self, user_id):
        return auth_models.User.objects.get(pk=user_id)

    def has_perm(self, user, perm, obj=None):
        if perm.startswith('dinner.'):
            cooks = models.Group.objects.cooks().filter(
                users__username=user.username,
            )
            return bool(cooks.count())

