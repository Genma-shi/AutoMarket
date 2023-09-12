from .forms import CarPartForm, CarPartPhotoForm , CarPartImage


from django.shortcuts import render , redirect  
from .models import CarPart

def show_all_car_parts(request):
    all_car_parts = CarPart.objects.all()
    return render(request, 'car_part.html', {'car_parts': all_car_parts})

def add_car_part(request):
    if request.method == 'POST':
        car_part_form = CarPartForm(request.POST, request.FILES)
        print(car_part_form.is_valid())
        if car_part_form.is_valid():
            car_part = car_part_form.save(commit=False)
            car_part.save()  

            for image in request.FILES.getlist('part_photos'):
                CarPartImage.objects.create(car_part=car_part, image=image)

            return redirect('car_part.html')  
    else:
        car_part_form = CarPartForm()

    return render(request, 'add_car_part.html', {'car_part_form': car_part_form})