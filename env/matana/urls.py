"""matana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# from archives.views import Liste_projetViewSet,Ecolage_ModelView,Liste_filiere_ModelView,Profil_Etudiant_ModelView


# router1= routers.SimpleRouter()
# router1.register( 'projetfinal', Liste_projetViewSet, basename='projetfinal')
# router= routers.SimpleRouter()
# router.register(r'ecolage', Ecolage_ModelView, basename='ecolage')
# router.register(r'profiletudiant',Profil_Etudiant_ModelView,basename='profiletudiant')
# router.register(r'filiere',Liste_filiere_ModelView,basename='filiere')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('', include('router.urls')),
    # path('', include(router.urls)),
    # path('listefiliere',Liste_filiere_APIView.as_view)
    path ('', include('archives.urls')),
]

