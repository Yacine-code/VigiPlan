from django.urls import reverse_lazy  # Utilisé pour générer les URL dynamiquement
from django.views.generic import ListView, CreateView, UpdateView, DeleteView  # Importation des vues génériques
from .models import Prestation  # Importation du modèle Prestation
from .forms import PrestationForm  # Importation du formulaire personnalisé

# Vue pour afficher la liste des prestations
class PrestationListView(ListView):
    model = Prestation  # Modèle utilisé pour récupérer les données
    template_name = "gestion_prestations/prestation_list.html"  # Template utilisé pour le rendu
    context_object_name = "prestations"  # Nom du contexte passé au template

# Vue pour créer une nouvelle prestation
class PrestationCreateView(CreateView):
    model = Prestation
    form_class = PrestationForm  # Formulaire personnalisé utilisé
    template_name = "gestion_prestations/prestation_form.html"  # Template du formulaire
    success_url = reverse_lazy('prestation-list')  # Redirection après succès

# Vue pour mettre à jour une prestation existante
class PrestationUpdateView(UpdateView):
    model = Prestation
    form_class = PrestationForm
    template_name = "gestion_prestations/prestation_form.html"
    success_url = reverse_lazy('prestation-list')

# Vue pour supprimer une prestation
class PrestationDeleteView(DeleteView):
    model = Prestation
    template_name = "gestion_prestations/prestation_confirm_delete.html"  # Template pour confirmer la suppression
    success_url = reverse_lazy('prestation-list')
