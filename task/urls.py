from django.urls import path
from rest_framework import routers
from task import views

# api version
router = routers.DefaultRouter()
router.register(r'task', views.TaskView, 'tasks')

urlpatterns = [
    path("api/v1")
]
