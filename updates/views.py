import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext
from updates.models import Chirp


def list_chirps(request):
    chirps = Chirp.objects.all().order_by('-posted_at')
    page_load = datetime.datetime.now()

    return render(request, 'updates/list_chirps.html', {'chirps': chirps, 'page_load': page_load})

def detail_chirp(request, chirp_id):
    chirp = Chirp.objects.get(pk=chirp_id)

    return render(request, 'updates/detail_chirp.html', {'chirp': chirp})