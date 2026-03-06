from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Colaborador, Obra
from .forms import ObraForm # Importando o form que acabamos de criar

class ColaboradorListView(LoginRequiredMixin, ListView):
    model = Colaborador
    template_name = "colaboradores/lista.html"
    context_object_name = "colaboradores"

    def get_queryset(self):
        # Filtra os colaboradores apenas para a empresa logada
        return Colaborador.objects.filter(empresa=self.request.user.empresa)
    
@login_required
def criar_obra(request):
    if request.method == "POST":
        form = ObraForm(request.POST)
        if form.is_valid():
            nova_obra = form.save(commit=False)
            nova_obra.empresa = request.user.empresa # Injeta a empresa
            nova_obra.save()
            return redirect("gestao:lista_colaboradores") # Ajuste para o nome da sua URL
    else:
        form = ObraForm()

    return render(request, "obras/form.html", {'form': form})