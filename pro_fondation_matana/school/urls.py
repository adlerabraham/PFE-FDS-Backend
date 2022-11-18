from rest_framework.routers import DefaultRouter
from django.urls import path, include
from school.views import *



router =  DefaultRouter()

router.register('ecole', Ecole_viewset, basename='ecole'),



urlpatterns= [

    path('', include(router.urls)),
  
]
