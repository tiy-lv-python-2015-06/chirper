import datetime
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader, RequestContext
from django.views.generic import ListView, DetailView, CreateView
from updates.forms import ChirpForm
from updates.models import Chirp


class ChirpList(ListView):
    model = Chirp
    # default = chirp_list.html
    template_name = "updates/list_chirps.html"
    queryset = Chirp.objects.all().order_by('-posted_at')
    #default = chirp_list
    context_object_name = 'chirps'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ChirpList, self).get_context_data(**kwargs)
        context['page_load'] = datetime.datetime.now()
        return context


class ChirpDetail(DetailView):
    model = Chirp
    pk_url_kwarg = 'chirp_id'
    context_object_name = 'chirp'
    # Default chirp_detail.html
    template_name = "updates/detail_chirp.html"


class ChirpCreate(CreateView):
    model = Chirp
    fields = ('title', 'message')
    success_url = reverse_lazy('list_chirps')
    # Default = chirp_form.html
    template_name = "updates/create_chirp.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.posted_at = datetime.datetime.now()
        return super(ChirpCreate, self).form_valid(form)


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