from django.contrib import admin
from .models import CarPart, CarPartImage, Car_Part_Brand
from django.contrib.admin.widgets import FilteredSelectMultiple
# Register your models here.

class CarPartImageInline(admin.TabularInline):
    model = CarPartImage
    extra = 1  # Количество пустых строк для добавления новых изображений


@admin.register(Car_Part_Brand)
class CarPartBrandAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(CarPart)
class CarPartAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'price', 'condition', 'location', 'is_available', 'views_count')
    list_filter = ('condition', 'is_available', 'year', 'car_part_brand')
    search_fields = ('name', 'car_part_brand__name')
    filter_horizontal = ('car_model',)
    inlines = [CarPartImageInline]  # Добавляем изображения в админ-панель


@admin.register(CarPartImage)
class CarPartImageAdmin(admin.ModelAdmin):
    list_display = ('car_part', 'image')
