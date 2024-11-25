from django.urls import reverse_lazy  # Utilisé pour générer des URL dynamiquement
from django.views.generic import ListView, CreateView, UpdateView, DeleteView  # Importation des vues génériques
from .models import Site  # Importation du modèle Site

# Vue pour afficher la liste des sites
class SiteListView(ListView):
    model = Site  # Modèle utilisé pour récupérer les données
    template_name = "gestion_sites/site_list.html"  # Template utilisé pour le rendu
    context_object_name = "sites"  # Nom du contexte passé au template

# Vue pour créer un nouveau site
class SiteCreateView(CreateView):
    model = Site
    fields = ['nom', 'adresse', 'ville', 'societe']  # Champs inclus dans le formulaire de création
    template_name = "gestion_sites/site_form.html"  # Template utilisé pour le formulaire
    success_url = reverse_lazy('site-list')  # Redirection après succès

# Vue pour mettre à jour un site existant
class SiteUpdateView(UpdateView):
    model = Site
    fields = ['nom', 'adresse', 'ville', 'societe']  # Champs modifiables dans le formulaire
    template_name = "gestion_sites/site_form.html"
    success_url = reverse_lazy('site-list')

# Vue pour supprimer un site
class SiteDeleteView(DeleteView):
    model = Site
    template_name = "gestion_sites/site_confirm_delete.html"  # Template pour confirmer la suppression
    success_url = reverse_lazy('site-list')  # Redirection après suppression
