from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^chirps/', 'api.views.chirp_list'),
    #url(r'^snippets/(?P<pk>[0-9]+)$', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
