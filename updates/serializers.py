from rest_framework import serializers
from updates.models import Chirp


class ChirpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chirp
        fields = ('id', 'author', 'message', 'title', 'posted_at')