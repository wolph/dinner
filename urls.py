# pylint: disable=E1120
from django.conf import urls, settings
from django.contrib import admin
from django.views.generic import base
from dinner import admin as dinner_admin

admin.autodiscover()

urlpatterns = urls.patterns(
    '',
    urls.url(r'^tags_input/',
             urls.include('tags_input.urls', namespace='tags_input')),
    urls.url(r'^dinner/', urls.include('dinner.urls', namespace='dinner')),
    urls.url(r'^dinner_admin/', urls.include(dinner_admin.site.urls),
             name='dinner_admin'),
    urls.url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        {'next_page': settings.LOGOUT_URL},
        name='logout',
    ),
    urls.url(r'^login/$', base.RedirectView.as_view(url=settings.LOGIN_URL),
             name='login'),
    urls.url(r'^admin/', urls.include(admin.site.urls), name='admin'),
    urls.url(r'^$', base.RedirectView.as_view(
        pattern_name='dinner:index', permanent=False)),
)
