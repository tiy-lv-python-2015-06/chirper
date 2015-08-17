from django.contrib.auth.models import User
from rest_framework import generics
from updates.models import Chirp
from updates.serializers import ChirpSerializer
from rest_framework import permissions

class ChirpList(generics.ListCreateAPIView):
    """
    List All chirps or create a new one
    """
    queryset = Chirp.objects.all()
    serializer_class = ChirpSerializer

    def perform_create(self, serializer):
        serializer.save(author=User.objects.get(pk=1))


class ChirpDetailAndUpdate(generics.RetrieveUpdateDestroyAPIView):

    queryset = Chirp.objects.all()
    serializer_class = ChirpSerializer