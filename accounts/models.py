from django.db import models
from django.contrib.auth.models import AbstractUser

class Empresa(models.Model):
    razao_social = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return self.razao_social
    
class Usuario(AbstractUser):
    # O null=True, blank=True é útil caso você tenha um "Super Admin" do sistema 
    # que não pertence a nenhuma construtora específica.
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.username    