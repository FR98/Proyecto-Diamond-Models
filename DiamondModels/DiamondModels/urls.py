"""DiamondModels URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
#from marcas import views as marcas_views
#from agencias import views as agencias_views
#from modelos import views as modelos_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', auth_views.login, name='home'),

    url(r'^marcas/(?P<marca_pk>[0-9]+)', 
        marcas_views.detalle_marca, 
        name = "detalle_marca"),


    url(r'^agencias/(?P<agencia_pk>[0-9]+)', 
        agencias_views.detalle_agencia, 
        name = "detalle_agencia"),

    url(r'^marcas/$', 
        marcas_views.mi_marca, 
        name = "mi_marca"),

    url(r'^agencias/$', 
        agencias_views.mi_agencia, 
        name = "mi_agencia"),

    url(r'^modelos/$', 
        modelos_views.lista_modelos, 
        name = "lista_modelos"),


]