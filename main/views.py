from django.views.generic import ListView, DetailView
from .models import Page
from django.shortcuts import render


class Index(ListView):
    model = Page
    template_name = 'main/index.html'

    def get_queryset(self):
        return Page.objects.all()


class PageDetail(DetailView):
    model = Page
    slug_field = 'url_page'
    template_name = 'main/services/warmGlass.html'


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')