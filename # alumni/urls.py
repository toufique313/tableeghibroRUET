# alumni/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('edit/', views.edit_profile, name='edit_profile'),
]
