from django.conf import urls

urlpatterns = urls.patterns(
    'dinner.views',
    urls.url(r'^$', 'index', name='index'),
    urls.url(r'^remove/$', 'remove', name='remove'),
)

