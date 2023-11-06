from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('api/register/', views.register_user, name='register_user'),
    path('api/login/', views.login_user, name='login_user'),
]

# localhost:8000/api/v1.0/user/test
