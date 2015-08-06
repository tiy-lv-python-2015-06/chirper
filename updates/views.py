import datetime
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader, RequestContext
from updates.forms import ChirpForm
from updates.models import Chirp


def list_chirps(request):
    chirps = Chirp.objects.all().order_by('-posted_at')
    page_load = datetime.datetime.now()

    return render(request, 'updates/list_chirps.html', {'chirps': chirps, 'page_load': page_load})

def detail_chirp(request, chirp_id):
    chirp = get_object_or_404(Chirp, pk=chirp_id)

    return render(request, 'updates/detail_chirp.html', {'chirp': chirp})

@login_required(login_url='/login')
def create_chirp(request):
    if request.method == 'POST':
        form = ChirpForm(request.POST)

        if form.is_valid():
            chirp = form.save(commit=False)
            chirp.author = request.user
            chirp.posted_at = datetime.datetime.now()
            chirp.save()

            return HttpResponseRedirect(reverse('list_chirps'))

    else:
        form = ChirpForm()
    return render(request, 'updates/create_chirp.html', {'form':form})