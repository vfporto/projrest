"""projrest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from localizacoes.api.viewsets import LocalizacaoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from reviews.api.viewsets import ReviewViewSet

router = routers.DefaultRouter()
router.register(r'ponto_turistico', PontoTuristicoViewSet)
router.register(r'localizacoes', LocalizacaoViewSet)
router.register(r'atracoes', AtracaoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'reviews', ReviewViewSet)




urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
