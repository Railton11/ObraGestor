from django.shortcuts import render, redirect
from .forms import CadastroEmpresaForm
from django.contrib.auth import login

def registrar_empresa(request):
    if request.method == 'POST':
        form = CadastroEmpresaForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Loga o usuário automaticamente após o cadastro
            return redirect('gestao:lista_colaboradores')
    else:
        form = CadastroEmpresaForm()
    return render(request, 'registration/registrar.html', {'form': form})