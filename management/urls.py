# gestao/urls.py
from django.urls import path
from . import views

# Opcional, mas muito recomendado: criar um "namespace" para o app
app_name = 'gestao'

urlpatterns = [
    # Rota para a Class-Based View (repare no .as_view())
    # O "name" aqui tem que ser igual ao que usamos no redirect("lista_colaboradores") da view anterior!
    path('colaboradores/', views.ColaboradorListView.as_view(), name='lista_colaboradores'),
    
    # Rota para a Function-Based View
    path('obras/nova/', views.criar_obra, name='criar_obra'),
]