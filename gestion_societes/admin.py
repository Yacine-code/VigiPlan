from django.contrib import admin
from .models import Société

@admin.register(Société)
class SociétéAdmin(admin.ModelAdmin):
    list_display = ['nom', 'email', 'telephone', 'administrateur']
    search_fields = ['nom', 'email']
    list_filter = ['nom']
