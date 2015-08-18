from api.views import DetailAndUpdate
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

__author__ = 'jeff'

urlpatterns = [
    url(r'^chirps/$', 'api.views.list_create_view'),
    url(r'^chirps/(?P<chirp_id>[0-9]+)/',
        csrf_exempt(DetailAndUpdate.as_view()))
]