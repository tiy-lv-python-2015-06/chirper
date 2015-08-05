from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'updates.views.list_chirps', name='list_chirps'),
    url(r'(?P<chirp_id>[0-9]+)/', 'updates.views.detail_chirp', name="detail_chirp"),
    url(r'create/', 'updates.views.create_chirp', name='create_chirp')
]