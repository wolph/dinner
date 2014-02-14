from django.conf import urls

urlpatterns = urls.patterns(
    'dinner.views',
    urls.url(r'^$', 'index', name='index'),
    urls.url(r'^(?P<date>\d{4}-\d{2}-\d{2})/$', 'index', name='index'),
)

