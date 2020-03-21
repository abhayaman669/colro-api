from django.urls import path, include

from .views import create_auth

urlpatterns = [
    path('register/', create_auth),
]
