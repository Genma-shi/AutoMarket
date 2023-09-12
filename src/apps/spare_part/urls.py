from django.contrib import admin
from django.urls import path , include
from src.apps.post import views


urlpatterns = [
    path('',  views.show_all_car_parts, name='car_part'),
    path('add_part/', views.add_car_part, name='add_car_part'),
    ]