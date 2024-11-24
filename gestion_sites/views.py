from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Site

class SiteListView(ListView):
    model = Site
    template_name = "gestion_sites/site_list.html"
    context_object_name = "sites"

class SiteCreateView(CreateView):
    model = Site
    fields = ['nom', 'adresse', 'ville', 'societe']
    template_name = "gestion_sites/site_form.html"
    success_url = reverse_lazy('site-list')

class SiteUpdateView(UpdateView):
    model = Site
    fields = ['nom', 'adresse', 'ville', 'societe']
    template_name = "gestion_sites/site_form.html"
    success_url = reverse_lazy('site-list')

class SiteDeleteView(DeleteView):
    model = Site
    template_name = "gestion_sites/site_confirm_delete.html"
    success_url = reverse_lazy('site-list')
