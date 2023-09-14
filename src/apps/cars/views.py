from django.shortcuts import render , redirect
from django.http import HttpResponseBadRequest

from src.apps.cars.filter import CarFilter
from .models import Car
from .forms import *
from django.core.paginator import Paginator, Page

from django.views.generic import View , ListView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from django.http.response import HttpResponse
# Create your views here.
class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'  # Шаблон для отображения списка элементов
    context_object_name = 'list'  # Имя переменной контекста для списка элементов
    paginate_by = 30

    def car_list(request):
        cars = Car.objects.all()
        cars_per_page = 10
        paginator = Paginator(cars, cars_per_page)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

        return render(request, 'cars_list.html', {'page': page})

@login_required
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        print(form.is_valid())
        # print(special_notes_form.is_valid())
        if form.is_valid():

            car = form.save(commit=False)
            car.owner = request.user
            car.save()

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
    return render(request, 'add_car.html',  {'form': form})

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
    car.views_count += 1 
    car.save()  

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
    
# второй вариант 
@login_required    
def car_filter(request):
    # Создайте объект фильтрации на основе GET-параметров
    filter = CarFilter(request.GET, queryset=Car.objects.all())
    
    # Если форма отправлена, примените фильтр к запросу
    if filter.is_valid():
        cars = filter.qs
    else:
        cars = Car.objects.all()  # Если форма не валидна, покажите все машины
        
    return render(request, 'car_filter.html', {'filter': filter, 'cars': cars})

def filtered_cars(request, pk=None):
    # Получите объект машины по ее Primary Key (pk)
    if pk:
        car = get_object_or_404(Car, pk=pk)
    else:
        car = None

    # Создайте объект фильтрации на основе GET-параметров
    filter = CarFilter(request.GET, queryset=Car.objects.all())
    
    # Если форма отправлена, примените фильтр к запросу
    if filter.is_valid():
        cars = filter.qs
    else:
        cars = Car.objects.all()

    return render(request, 'car_filter.html', {'filter': car, 'cars': cars})


def update_car(request, car_id):
    car_instance = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        form = CarForm(request.POST, instance=car_instance)
        if form.is_valid():
            form.save()
            return redirect('detail_page', car_id=car_id)  # Redirect to car detail page
    else:
        form = CarForm(instance=car_instance)

    return render(request, 'car_update_form.html', {'form': form})