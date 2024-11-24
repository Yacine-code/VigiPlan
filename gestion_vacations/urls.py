from django.urls import path
from .views import (
    VacationListView,
    VacationCreateView,
    VacationUpdateView,
    VacationDeleteView,
    AssignAgentView,
    generate_vacations,
    get_vacations,
    planning_view,
)

urlpatterns = [
    path('', VacationListView.as_view(), name='vacation-list'),
    path('create/', VacationCreateView.as_view(), name='vacation-create'),
    path('<int:pk>/update/', VacationUpdateView.as_view(), name='vacation-update'),
    path('<int:pk>/delete/', VacationDeleteView.as_view(), name='vacation-delete'),
    path('generate/<int:prestation_id>/', generate_vacations, name='generate-vacations'),
    path('<int:pk>/assign/', AssignAgentView.as_view(), name='assign-agent'),
    path('vacations/api/', get_vacations, name='get-vacations'),
    path('planning/', planning_view, name='planning'),
    path('api/', get_vacations, name='get-vacations'),  # Corrigez ici si nécessaire
]
