from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Prestation
from .forms import PrestationForm

class PrestationListView(ListView):
    model = Prestation
    template_name = "gestion_prestations/prestation_list.html"
    context_object_name = "prestations"

class PrestationCreateView(CreateView):
    model = Prestation
    form_class = PrestationForm
    template_name = "gestion_prestations/prestation_form.html"
    success_url = reverse_lazy('prestation-list')

class PrestationUpdateView(UpdateView):
    model = Prestation
    form_class = PrestationForm
    template_name = "gestion_prestations/prestation_form.html"
    success_url = reverse_lazy('prestation-list')


class PrestationDeleteView(DeleteView):
    model = Prestation
    template_name = "gestion_prestations/prestation_confirm_delete.html"
    success_url = reverse_lazy('prestation-list')
