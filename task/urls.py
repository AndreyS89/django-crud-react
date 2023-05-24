from django.urls import path
from rest_framework import routers

# api version
router = routers.DefaultRouter()

urlpatterns = [
    path("api/v1")
]
