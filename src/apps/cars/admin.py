from django.contrib import admin
from .models import CarMake, CarModel, Car, CarPhoto


@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CarPhotoInline(admin.TabularInline):
    model = CarPhoto
    extra = 1

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('mark', 'model', 'year', 'owner')
    list_filter = ('mark', 'model', 'year', 'owner')
    search_fields = ('mark__name', 'model__name', 'year', 'owner__username')
    inlines = [CarPhotoInline]

@admin.register(CarPhoto)
class CarPhotoAdmin(admin.ModelAdmin):
    list_display = ('car', 'image', 'is_main')
    list_filter = ('car', 'is_main')