from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from updates.models import Chirp
from updates.serializers import ChirpSerializer


class ChirpList(APIView):
    """
    List All chirps or create a new one
    """
    def get(self, request, format=None):
        chirps = Chirp.objects.all()
        serializer = ChirpSerializer(chirps, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChirpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=User.objects.get(pk=1))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChirpDetailAndUpdate(APIView):

    def get(self, request, pk, format=None):
        chirp = get_object_or_404(Chirp, pk)
        serializer = ChirpSerializer(chirp)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        chirp = get_object_or_404(Chirp, pk)
        serializer = ChirpSerializer(chirp)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        chirp = get_object_or_404(Chirp, pk)
        chirp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
