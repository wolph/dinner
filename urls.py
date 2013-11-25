from django.conf import urls
from django.contrib import admin

admin.autodiscover()

urlpatterns = urls.patterns(
    '',
    urls.url(r'^dinner/', urls.include('dinner.urls', namespace='dinner')),
    urls.url(r'^admin/', urls.include(admin.site.urls)),
)
