from django.contrib import admin
from .models import Obra, Colaborador

@admin.register(Obra)
class ObraAdmin(admin.ModelAdmin):
    list_display = ('nome_obra', 'empresa')
    list_filter = ('empresa',)
    search_fields = ('nome_obra',)

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'empresa')
    list_filter = ('empresa', 'cargo')
    search_fields = ('nome', 'cpf')