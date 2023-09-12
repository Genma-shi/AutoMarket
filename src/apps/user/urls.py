from django.contrib import admin
from django.urls import path , include
from src.apps.user import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
]