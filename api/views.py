import json
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, DetailView
from updates.models import Chirp

@csrf_exempt
def chirp_list_create_view(request):
    if request.method == "GET":
        chirps = Chirp.objects.all()
        return HttpResponse(serializers.serialize("json", chirps),
                            content_type="application/json")
    elif request.method == "POST":
        user = User.objects.get(pk=1)

        if request.META['CONTENT_TYPE'] == "application/json":
            data = json.loads(request.body.decode("utf-8"))

            chirp = Chirp(message=data['message'], title=data['title'],
                          author=user, posted_at=timezone.now())
        else:
            data = request.POST
            chirp = Chirp(author=user, message=data['message'],
                          title=data['title'], posted_at=timezone.now())

        chirp.save()
        return HttpResponse(serializers.serialize("json", [chirp]),
                            status=201, content_type="application/json")

class DetailAndUpdate(View):

    def get(self, *args, **kwargs):
        chirp_id = kwargs['chirp_id']
        chirp = Chirp.objects.get(pk=chirp_id)

        response = HttpResponse(serializers.serialize("json", [chirp]),
                                status=200, content_type="application/json")
        return response

    def put(self, *args, **kwargs):
        chirp_id = kwargs['chirp_id']
        chirp = Chirp.objects.get(pk=chirp_id)

        if self.request.META['CONTENT_TYPE'] == "application/json":
            data = json.loads(self.request.body.decode('utf-8'))
            chirp.message = data['message']
            chirp.title = data['title']

        response = HttpResponse(serializers.serialize("json", [chirp]),
                                status=200, content_type="application/json")
        return response