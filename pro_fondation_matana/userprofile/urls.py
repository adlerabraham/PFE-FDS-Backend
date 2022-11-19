from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView



router =  DefaultRouter()


router.register('superadminprofile', Super_admin_viewset, basename='superadminprofile'),
router.register('adminprofile', Admin_viewset, basename='adminprofile'),
router.register('teacherprofile', Teacher_viewset, basename='teacherprofile'),
router.register('studentprofile', Student_viewset, basename='studentprofile'),

urlpatterns= [

    path('', include(router.urls)),
    path('updatestudent/<int:pk>/',Update_student_view.as_view(), name='updatestudent'),


]

    
    