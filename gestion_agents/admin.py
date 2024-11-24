from django.contrib import admin
from .models import Agent

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'email', 'telephone', 'societe']
    search_fields = ['nom', 'prenom', 'email']
    list_filter = ['societe']
