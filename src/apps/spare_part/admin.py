from django.contrib import admin

# Register your models here.

from .models import Car_Part_Brand
admin.site.register(Car_Part_Brand)

from .models import CarPart
admin.site.register(CarPart)

from .models import CarPartImage
admin.site.register(CarPartImage)