from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from updates.views import ChirpList, ChirpDetail, ChirpCreate

urlpatterns = [
    url(r'^$', ChirpList.as_view(), name='list_chirps'),
    url(r'(?P<chirp_id>[0-9]+)/', ChirpDetail.as_view(), name="detail_chirp"),
    url(r'create/', login_required(ChirpCreate.as_view()), name='create_chirp')
]