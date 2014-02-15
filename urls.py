from django.conf import urls
from django.contrib import admin
from django.views.generic import base

admin.autodiscover()

urlpatterns = urls.patterns(
    '',
    urls.url(r'^tags_input/',
             urls.include('tags_input.urls', namespace='tags_input')),
    urls.url(r'^dinner/', urls.include('dinner.urls', namespace='dinner')),
    urls.url(r'^admin/', urls.include(admin.site.urls)),
    urls.url(r'^.*$',
             base.RedirectView.as_view(url='/dinner/', permanent=False)),
)
