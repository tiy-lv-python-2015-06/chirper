from api.views import DetailAndUpdate, ListCreateView
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from rest_framework.urlpatterns import format_suffix_patterns

__author__ = 'jeff'

urlpatterns = [
    url(r'^chirps/$', ListCreateView.as_view()),
    url(r'^chirps/(?P<pk>[0-9]+)/',
        DetailAndUpdate.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)