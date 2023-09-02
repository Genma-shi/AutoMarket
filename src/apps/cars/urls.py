from django.urls import path

from src.apps.post import views

from django.views.generic import TemplateView ,  RedirectView

from django.urls import path , include

urlpatterns = [
    path('cars_list/', views.car_list, name='cars'),
    path('add_car/', views.add_car, name='add_car'),
    path('favorites_list/' , views.favorites_list , name='favorites_list'),

    path('cars/<int:car_id>/', views.detail_page, name='detail_page'),
    path('profile/<int:user_id>/', views.profile_view, name='profile'),

    path('cars/delete/<int:car_id>/', views.delete_car, name='delete_car'),

    path('favorites_list/add/<int:pk>' , views.add_to_favorites_list , name = 'add_to_favorites'),
    path('favorites_list/remove/<int:pk>' , views.remove_to_favorites_list , name = 'remove_to_favorites') ,
]