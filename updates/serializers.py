from rest_framework import serializers
from updates.models import Chirp


class ChirpSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(read_only=True,
                                                 many=False,
                                                 view_name='user_detail')

    class Meta:
        model = Chirp
        fields = ('id', 'author', 'message', 'title', 'posted_at')