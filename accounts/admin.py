# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Empresa, Usuario

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('razao_social', 'cnpj')
    search_fields = ('razao_social', 'cnpj')

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    # Adicionamos o campo 'empresa' nos formulários do Admin do Django
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Corporativas', {'fields': ('empresa',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações Corporativas', {'fields': ('empresa',)}),
    )
    list_display = ('username', 'email', 'empresa', 'is_staff')
    list_filter = ('empresa', 'is_staff', 'is_superuser')