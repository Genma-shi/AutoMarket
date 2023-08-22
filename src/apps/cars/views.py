from django.shortcuts import render
from .models import Car
from .forms import CarForm

# Create your views here.
# def cars_view(request):
#     return render(request, 'cars.html')


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            
            # Можно добавить дополнительную логику после сохранения формы
    else:
        form = CarForm()
    return render(request, 'add_car.html', {'form': form})