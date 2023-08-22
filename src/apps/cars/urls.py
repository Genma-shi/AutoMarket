from django.urls import path

from src.apps.post import views

from django.views.generic import TemplateView ,  RedirectView

from django.urls import path , include

urlpatterns = [
    # path('cars/', views.cars_view, name='cars'),
    path('add_car/', views.add_car, name='add_car'),
]