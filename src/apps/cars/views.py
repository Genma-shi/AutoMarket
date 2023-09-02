from django.shortcuts import render , redirect
from .models import Car
from .forms import *

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from django.http.response import HttpResponse
# Create your views here.

def car_list(request):
    cars = Car.objects.all()
    
    return render(request, 'cars_list.html', {'cars': cars})

# @login_required
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        special_notes_form = SpecialNotesForm(request.POST)
        print(form.is_valid())
        if form.is_valid() and special_notes_form.is_valid():

            car = form.save(commit=False)
            car.owner = request.user
            car.save()

            special_notes = special_notes_form.save()
            car.special_notes.add(special_notes)
            photos = request.FILES.getlist('photos')
            for photo in photos:
                CarPhoto.objects.create(
                    image=photo,
                    car=car
                )
            return redirect('cars')
    else:
        form = CarForm()
        photo_form = CarPhotoForm()
        special_notes_form = SpecialNotesForm()
    return render(request, 'add_car.html',  {'form': form, 'photo_form': photo_form, 'special_notes_form': special_notes_form})

@login_required
def delete_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    car.delete()
    return redirect('profile', user_id=request.user.id) 


@login_required

def favorites_list(request):
    user = request.user
    favorites = user.favorites_list.all()
    context = {'favorites': favorites}
    return render(request, 'favorites_list.html', context)


@login_required
def detail_page(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    car_photos = car.photos.all()
    context = {
        'car': car,
        'car_photos': car_photos,
    }
    return render(request, 'detail_page.html', context)


@login_required
def profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    cars = Car.objects.filter(owner=user)

    context = {
        'profile_user': user,
        'cars': cars,
    }
    return render(request, 'profile.html', context)


@login_required
def add_to_favorites_list(request , pk):
    user = request.user
    car = get_object_or_404(Car , id = pk)
    if car in user.favorites_list.all() :
        return HttpResponse("Fail")
    else:
        user.favorites_list.add(car)
    return redirect ("cars")

@login_required
def remove_to_favorites_list(request , pk):
    user = request.user
    car = get_object_or_404(Car , id = pk)
    if car in user.favorites_list.all() :
        user.favorites_list.remove(car)
        
    else:
        return HttpResponse("Fail")
    return redirect ("favorites_list")