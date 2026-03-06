# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_empresa, name='registrar_empresa'),
]