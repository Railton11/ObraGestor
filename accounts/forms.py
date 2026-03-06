from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Empresa
from django.db import transaction

class CadastroEmpresaForm(UserCreationForm):
    razao_social = forms.CharField(max_length=200, label="Nome da Construtora")
    cnpj = forms.CharField(max_length=18, label="CNPJ")

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = UserCreationForm.Meta.fields + ('email', 'razao_social', 'cnpj')

    # Usamos transaction.atomic para garantir que ou cria os dois (Empresa e User) ou nenhum
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        # 1. Cria a empresa primeiro
        empresa = Empresa.objects.create(
            razao_social=self.cleaned_data['razao_social'],
            cnpj=self.cleaned_data['cnpj']
        )
        # 2. Vincula o usuário à empresa recém-criada
        user.empresa = empresa
        if commit:
            user.save()
        return user