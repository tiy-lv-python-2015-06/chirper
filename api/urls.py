from api.views import ChirpList, ChirpDetailAndUpdate
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^chirps/$', ChirpList.as_view()),
    url(r'^chirps/(?P<pk>[0-9]+)/$', ChirpDetailAndUpdate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
