from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import CarMake, CarModel, Car, CarPhoto, Special_notes
from django.db import models


@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CarPhotoInline(admin.TabularInline):
    model = CarPhoto
    extra = 1

class SpecialNotesInline(admin.TabularInline):
    model = Car.special_notes.through
    extra = 1

@admin.register(Special_notes)
class Special_notesAdmin(admin.ModelAdmin):
    list_display = ('name',) 

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('mark', 'model', 'year', 'owner', 'price')
    list_filter = ('mark', 'model', 'year', 'owner')
    search_fields = ('mark__name', 'model__name', 'year', 'owner__username')
    inlines = [SpecialNotesInline, CarPhotoInline]
    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple("Special notes", is_stacked=False)},
    }
    
@admin.register(CarPhoto)
class CarPhotoAdmin(admin.ModelAdmin):
    list_display = ('car', 'image', 'is_main')
    list_filter = ('car', 'is_main')

