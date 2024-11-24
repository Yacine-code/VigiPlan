from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'is_company_admin', 'is_super_admin')}),
    )
    list_display = ['username', 'email', 'is_company_admin', 'is_super_admin', 'is_staff']
