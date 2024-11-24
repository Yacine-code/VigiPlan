from django.contrib import admin
from .models import Vacation

@admin.register(Vacation)
class VacationAdmin(admin.ModelAdmin):
    list_display = ['date', 'heure_debut', 'heure_fin', 'agent', 'prestation']
    list_filter = ['date', 'prestation']
    search_fields = ['agent__nom', 'prestation__nom']
