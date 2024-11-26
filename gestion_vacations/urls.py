from django.urls import path  # Pour définir les routes URL
from .views import (
    VacationListView, VacationCreateView, VacationUpdateView, VacationDeleteView, AssignAgentView, 
    generate_vacations, get_vacations, planning_view, vacations_json
)
from . import views

# Importation des vues associées aux vacations

urlpatterns = [
    path('', VacationListView.as_view(), name='vacation-list'),  # Liste des vacations
    path('create/', VacationCreateView.as_view(), name='vacation-create'),  # Création d'une vacation
    path('<int:pk>/update/', VacationUpdateView.as_view(), name='vacation-update'),  # Modification d'une vacation
    path('<int:pk>/delete/', VacationDeleteView.as_view(), name='vacation-delete'),  # Suppression d'une vacation
    path('generate/<int:prestation_id>/', generate_vacations, name='generate-vacations'),  # Génération automatique
    path('<int:pk>/assign/', AssignAgentView.as_view(), name='assign-agent'),  # Assignation d'un agent
    path('api/', get_vacations, name='get-vacations'),  # API pour récupérer les vacations
    path('planning/', planning_view, name='planning'),  # Vue pour le planning
    path('vacations-json/', views.vacations_json, name='vacations-json'),
]
