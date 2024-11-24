from django.contrib import admin
from django.urls import path, include
from gestion_vacations.views import planning_view  # Importez votre vue ici

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agents/', include('gestion_agents.urls')),
    path('sites/', include('gestion_sites.urls')),
    path('prestations/', include('gestion_prestations.urls')),
    path('vacations/', include('gestion_vacations.urls')),
    
]
