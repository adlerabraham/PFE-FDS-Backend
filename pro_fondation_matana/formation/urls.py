from rest_framework.routers import DefaultRouter
from django.urls import path, include
from formation.views import *



router =  DefaultRouter()

router.register('programme', Programme_viewset, basename='programme'),
router.register('periode', Periode_viewset, basename='periode'),
router.register('programmeperiode', Programme_periode_viewset, basename='programme_periode'),
router.register('niveau', Niveau_viewset, basename='niveau'),
router.register('programmeperiodeniveau', Programme_periode_niveau_viewset, basename='programme_periode_niveau'),
router.register('classe', Classe_viewset, basename='classe'),
router.register('matiere', Matiere_viewset, basename='matieres'),
router.register('matiereprogrammeperiode', Matiere_programme_periode_viewset, basename='matieres'),
router.register('cours', Cours_viewset, basename='cours'),
router.register('lecons', Lecon_viewset, basename='lecons'),


urlpatterns= [

    path('', include(router.urls)),
  
]
