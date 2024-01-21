from django.urls import path, include
from rest_framework import routers
from .views import UploadViewSet

# Define rest framework router 
router = routers.DefaultRouter()

# Register routes of views 
router.register('upload', UploadViewSet, basename='upload_file')


# specific service level urls 
urlpatterns = [
    path('', include(router.urls))
]