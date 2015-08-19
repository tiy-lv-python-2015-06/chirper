from api.permissions import IsOwnerReadOnly
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from updates.models import Chirp
from updates.serializers import ChirpSerializer



class ListCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerReadOnly)
    queryset = Chirp.objects.all()
    serializer_class = ChirpSerializer

    def perform_create(self, serializer):
        user = User.objects.get(pk=1)
        serializer.save(author=user)

class DetailAndUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerReadOnly)
    queryset = Chirp.objects.all()
    serializer_class = ChirpSerializer