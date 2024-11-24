from django.contrib import admin
from .models import Site

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['nom', 'ville', 'societe']
    search_fields = ['nom', 'ville']
    list_filter = ['ville', 'societe']
