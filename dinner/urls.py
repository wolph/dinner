from django.conf import urls

urlpatterns = urls.patterns(
    'dinner.views',
    urls.url(r'^$', 'index', name='index'),
    urls.url(r'^create/$', 'create', name='create'),
)

