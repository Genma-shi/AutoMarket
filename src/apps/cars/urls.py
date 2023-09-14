from django.urls import path

from src.apps.post import views
from src.apps.cars.views import car_filter
from django.views.generic import TemplateView ,  RedirectView 

from django.urls import path , include

urlpatterns = [
    path('cars_list/', views.CarListView.car_list, name='cars'),
    path('car_list/', views.car_filter, name='car_filter'),
    path('', views.car_filter, name='car_filter'),


    path('add_car/', views.add_car, name='add_car'),
    path('favorites_list/' , views.favorites_list , name='favorites_list'),

    path('cars/<int:car_id>/', views.detail_page, name='detail_page'),
    path('profile/<int:user_id>/', views.profile_view, name='profile'),

    path('update_car/<int:car_id>/', views.update_car, name='update_car'),

    path('cars/delete/<int:car_id>/', views.delete_car, name='delete_car'),

    path('car_filter/', views.car_filter, name='car_filter'),
    path('car_filter/<int:pk>/', views.filtered_cars, name='filtered_cars'),

    path('favorites_list/add/<int:pk>' , views.add_to_favorites_list , name = 'add_to_favorites'),
    path('favorites_list/remove/<int:pk>' , views.remove_to_favorites_list , name = 'remove_to_favorites') ,


]