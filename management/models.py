from django.db import models
from django.conf import settings
from accounts.models import Empresa

class TenantModel(models.Model):
    empresa = models.ForeignKey('accounts.Empresa', on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Obra(TenantModel):
    nome_obra = models.CharField(max_length=150)
    endereco = models.TextField()

    def __str__(self):
        return self.nome_obra
    
class Colaborador(TenantModel):
    nome = models.CharField(max_length=150)
    cargo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome