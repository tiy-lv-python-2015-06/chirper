from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from updates.models import Chirp
from updates.serializers import ChirpSerializer


@api_view(['GET', 'POST'])
def chirp_list(request, format=None):

    if request.method == 'GET':
        chirps = Chirp.objects.all()
        serializer = ChirpSerializer(chirps, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ChirpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=User.objects.get(pk=1))
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
