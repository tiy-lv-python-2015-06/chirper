import datetime
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader, RequestContext
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
from updates.forms import ChirpForm
from updates.models import Chirp


class ChirpList(ListView):
    model = Chirp
    # default = chirp_list.html
    template_name = "updates/list_chirps.html"
    #default = chirp_list
    # context_object_name = 'chirps' Would change the list of chirps to be passed at chirps
    queryset = Chirp.objects.select_related().all().order_by('-posted_at')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ChirpList, self).get_context_data(**kwargs)
        context['page_load'] = datetime.datetime.now()
        return context

class ChirpDetail(DetailView):
    model = Chirp
    pk_url_kwarg = 'chirp_id'
    # Default chirp_detail.html
    template_name = 'updates/detail_chirp.html'

    def get_context_data(self, **kwargs):
        context = super(ChirpDetail, self).get_context_data(**kwargs)

        # Add the title to the session
        if 'viewed' not in self.request.session.keys():
            self.request.session['viewed'] = []

        if self.object.title not in self.request.session['viewed']:
            self.request.session['viewed'].append(self.object.title)
            self.request.session.modified = True

        return context


class ChirpCreate(CreateView):
    model = Chirp
    form_class = ChirpForm
    success_url = reverse_lazy('list_chirps')
    # Default = chirp_form.html
    template_name = "updates/create_chirp.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ChirpCreate, self).form_valid(form)

class ChirpUpdate(UpdateView):
    model = Chirp
    fields = ['title', 'message']
    template_name = "updates/create_chirp.html"