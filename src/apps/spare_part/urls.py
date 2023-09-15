from django.contrib import admin
from django.urls import path , include
from src.apps.post import views
from .views import CarpartListView

urlpatterns = [
    path('', CarpartListView.as_view(), name='car_part'),
    path('', views.CarpartListView.show_all_car_parts, name='car_part'),
    path('add_part/', views.add_car_part, name='add_car_part'),
    path('detail/<int:pk>/', views.carpart_detail_view, name='carpart-detail'),  
    path('filter/', views.part_filter, name='part_filter'),
    ]