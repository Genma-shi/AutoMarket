from .forms import CarPartForm, CarPartPhotoForm , CarPartImage
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404

from django.shortcuts import render , redirect  
from .models import CarPart
from django.core.paginator import Paginator

class CarpartListView(ListView):
    paginate_by = 5
    model = CarPart

    def show_all_car_parts(request):
        all_car_parts = CarPart.objects.all()
        paginator = Paginator(all_car_parts, 1)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, 'car_part.html', {'page': page_obj})

def add_car_part(request):
    if request.method == 'POST':
        car_part_form = CarPartForm(request.POST, request.FILES)
        print(car_part_form.is_valid())
        print(car_part_form.errors)
        if car_part_form.is_valid():
            car_part = car_part_form.save(commit=False)
            car_part.save()  

            for image in request.FILES.getlist('part_photos'):
                CarPartImage.objects.create(car_part=car_part, image=image)

            return redirect('spare_part')  
    else:
        car_part_form = CarPartForm()

    return render(request, 'add_car_part.html', {'car_part_form': car_part_form})


def carpart_detail_view(request, pk):
    carpart = get_object_or_404(CarPart, pk=pk)

    return render(request, 'part_detail.html', {'part': carpart})