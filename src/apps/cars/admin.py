from django.contrib import admin

# Register your models here.
from .models import Car
admin.site.register(Car)

from .models import Country
admin.site.register(Country)

from .models import CarPhoto
admin.site.register(CarPhoto)