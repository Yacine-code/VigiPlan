from django.urls import reverse_lazy  # Pour générer des URLs dynamiquement
from django.shortcuts import get_object_or_404, redirect, render  # Pour les opérations courantes sur les vues
from django.views.generic import ListView, CreateView, UpdateView, DeleteView  # Importation des vues génériques
from .models import Vacation  # Importation du modèle Vacation
from gestion_agents.models import Agent  # Modèle Agent pour assignation
from gestion_prestations.models import Prestation  # Modèle Prestation pour le contexte
from .forms import VacationForm  # Formulaire pour les vacations
from datetime import timedelta  # Pour manipuler les durées
from django.http import JsonResponse  # Pour répondre avec des données JSON

# Vue pour afficher la liste des vacations
class VacationListView(ListView):
    model = Vacation
    template_name = "gestion_vacations/vacation_list.html"
    context_object_name = "vacations"

# Vue pour créer une nouvelle vacation
class VacationCreateView(CreateView):
    model = Vacation
    form_class = VacationForm
    template_name = "gestion_vacations/vacation_form.html"
    success_url = "/vacations/"

# Vue pour générer automatiquement des vacations liées à une prestation
def generate_vacations(request, prestation_id):
    prestation = get_object_or_404(Prestation, pk=prestation_id)
    for i in range((prestation.date_fin - prestation.date_debut).days + 1):
        date = prestation.date_debut + timedelta(days=i)
        Vacation.objects.create(
            date=date, heure_debut="08:00", heure_fin="18:00", prestation=prestation,
        )
    return redirect("vacation-list")

# Vue pour supprimer une vacation
class VacationDeleteView(DeleteView):
    model = Vacation
    template_name = "gestion_vacations/vacation_confirm_delete.html"
    success_url = reverse_lazy('vacation-list')

# Vue pour assigner un agent à une vacation
class AssignAgentView(UpdateView):
    model = Vacation
    fields = ['agent']
    template_name = "gestion_vacations/assign_agent_form.html"
    success_url = "/vacations/"

# Vue pour mettre à jour une vacation
class VacationUpdateView(UpdateView):
    model = Vacation
    form_class = VacationForm
    template_name = "gestion_vacations/vacation_form.html"
    success_url = "/vacations/"

# API pour récupérer les vacations en format JSON
def get_vacations(request):
    vacations = Vacation.objects.all()
    events = [
        {
            "title": f"{vacation.agent or 'Non affectée'}",
            "start": f"{vacation.date}T{vacation.heure_debut}",
            "end": f"{vacation.date}T{vacation.heure_fin}",
        }
        for vacation in vacations
    ]
    return JsonResponse(events, safe=False)

# Vue pour afficher le planning
def planning_view(request):
    return render(request, 'planning.html')
