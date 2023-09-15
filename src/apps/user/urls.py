from django.contrib import admin
from django.urls import path , include
from src.apps.user import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/<int:user_id>/', views.profile_view, name='profile'),
    path('user_cars/', views.user_cars, name='user_cars'),
]