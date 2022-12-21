from rest_framework.routers import DefaultRouter
from django.urls import path, include
from school.views import *



#router =  DefaultRouter()

#router.register('ecole', Ecole_viewset, basename='ecole'),



urlpatterns= [

    #path('', include(router.urls)),
    path('ecole/<int:pk>/', Ecole_view.as_view(http_method_names=['get','put',]), name='ecole'),
    path('ecole/', Ecole_view.as_view(http_method_names=['post'])),

  
]
