from django.contrib.auth.models import User
from rest_framework import serializers, permissions
from updates.models import Chirp


class UserSerializer(serializers.HyperlinkedModelSerializer):

    chirp_set = \
        serializers.HyperlinkedRelatedField(many=True,
                                            queryset=Chirp.objects.all(),
                                            view_name='api_chirp_detail')

    class Meta:
        model = User
        fields = ('id', 'username', 'chirp_set')