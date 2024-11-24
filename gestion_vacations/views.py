from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Vacation
from gestion_agents.models import Agent
from gestion_prestations.models import Prestation
from .forms import VacationForm
from datetime import datetime, date, timedelta
from django.http import JsonResponse
from gestion_vacations.models import Vacation


class VacationListView(ListView):
    model = Vacation
    template_name = "gestion_vacations/vacation_list.html"
    context_object_name = "vacations"

class VacationCreateView(CreateView):
    model = Vacation
    form_class = VacationForm
    template_name = "gestion_vacations/vacation_form.html"
    success_url = "/vacations/"

def generate_vacations(request, prestation_id):
    prestation = get_object_or_404(Prestation, pk=prestation_id)

    # Exemple de génération automatique de vacations
    for i in range((prestation.date_fin - prestation.date_debut).days + 1):
        date = prestation.date_debut + timedelta(days=i)
        Vacation.objects.create(
            date=date,
            heure_debut="08:00",
            heure_fin="18:00",
            prestation=prestation,
        )
    return redirect("vacation-list")

class VacationDeleteView(DeleteView):
    model = Vacation
    template_name = "gestion_vacations/vacation_confirm_delete.html"
    success_url = reverse_lazy('vacation-list')
    
class AssignAgentView(UpdateView):
    model = Vacation
    fields = ['agent']
    template_name = "gestion_vacations/assign_agent_form.html"
    success_url = "/vacations/"
    

class VacationUpdateView(UpdateView):
    model = Vacation
    form_class = VacationForm
    template_name = "gestion_vacations/vacation_form.html"
    success_url = "/vacations/"


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

def planning_view(request):
    return render(request, 'planning.html')