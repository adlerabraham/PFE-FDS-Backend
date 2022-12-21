from rest_framework.routers import DefaultRouter
from django.urls import path, include
from formation.views import *



router =  DefaultRouter()

router.register('program', Program_viewset, basename='program'),
router.register('period', Period_viewset, basename='period'),
router.register('programperiod', Program_period_viewset, basename='program_period'),
router.register('level', Level_viewset, basename='level'),
router.register('programperiodlevel', Program_period_level_viewset, basename='program_period_level'),
router.register('classroom', Classe_viewset, basename='classroom'),
router.register('subject', Subject_viewset, basename='subject'),
router.register('subjectprogramperiod', Subject_program_period_viewset, basename='subject_program_period'),
router.register('course', Course_viewset, basename='course'),
router.register('lesson', Lesson_viewset, basename='lesson'),


urlpatterns= [

    path('', include(router.urls)),
  
]
