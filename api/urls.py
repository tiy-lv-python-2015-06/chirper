from api.views import ChirpListCreateView, ChirpDetailAndUpdate, UserList, \
    UserDetail
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

__author__ = 'jeff'

urlpatterns = [
    url(r'^chirps/$', ChirpListCreateView.as_view(), name='api_chirp_list'),
    url(r'^chirps/(?P<pk>[0-9]+)/',
        ChirpDetailAndUpdate.as_view(), name='api_chirp_detail'),
    url(r'^users/$', UserList.as_view(), name='user_list'),
    url(r'^users/(?P<pk>[0-9]+)/', UserDetail.as_view(), name='user_detail'),
    url(r'^github/(?P<username>\w+)/$', 'api.views.github_user'),
    url(r'^github/(?P<username>\w+)/repos/$', 'api.views.github_repo')
]

urlpatterns = format_suffix_patterns(urlpatterns)