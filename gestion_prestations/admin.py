from django.contrib import admin
from .models import Prestation

@admin.register(Prestation)
class PrestationAdmin(admin.ModelAdmin):
    list_display = ['nom', 'site', 'date_debut', 'date_fin']
    search_fields = ['nom', 'site__nom']
    list_filter = ['site']
