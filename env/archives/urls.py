from django.urls import path,include
from rest_framework import routers
from archives.views import ArchivesViewSet

router= routers.SimpleRouter()
router.register(r'archives', ArchivesViewSet, basename='archives')

urlpatterns = [
    path('api/', include(router.urls)),
            ]
    