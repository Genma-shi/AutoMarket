from src.apps.cars.urls import * 


urlpatterns.append(
    path('', TemplateView.as_view(template_name='base.html'), name='empty-path'),
)