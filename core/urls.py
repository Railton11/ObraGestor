from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Suas URLs customizadas (registrar)
    path('accounts/', include('accounts.urls')), 

    # Isso adiciona login, logout, reset de senha, etc.
    path('accounts/', include('django.contrib.auth.urls')),

    # Dizendo ao Django: "Tudo que começar com 'sistema/', procure no app gestao"
    path('sistema/', include('management.urls')),
]
