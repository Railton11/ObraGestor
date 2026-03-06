# gestao/forms.py
from django import forms
from .models import Obra

class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        # Não colocamos 'empresa' aqui para o usuário não poder alterar!
        fields = ['nome_obra', 'endereco']