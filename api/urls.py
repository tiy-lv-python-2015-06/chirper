from api.views import DetailAndUpdate
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^updates/$', 'api.views.chirp_list_create_view'),
    url(r'^updates/(?P<chirp_id>[0-9]+)/', csrf_exempt(DetailAndUpdate.as_view()))
]