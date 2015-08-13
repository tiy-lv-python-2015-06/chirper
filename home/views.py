from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "home/index.html"

class StarterView(TemplateView):
    template_name = "home/starting.html"