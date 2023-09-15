from .forms import CarPartForm, CarPartPhotoForm , CarPartImage
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404

from django.shortcuts import render , redirect  
from .models import CarPart
from django.core.paginator import Paginator
from .filter import CarPartFilter

class CarpartListView(ListView):
    paginate_by = 5
    model = CarPart
    template_name = 'car_part.html'

    def show_all_car_parts(self, request):
        all_car_parts = CarPart.objects.all()
        paginator = Paginator(all_car_parts, self.paginate_by)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return page_obj

    def get(self, request, *args, **kwargs):
        page_obj = self.show_all_car_parts(request)
        return render(request, self.template_name, {'page': page_obj})

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
    carpart.views_count += 1 
    carpart.save()  
    part_photos = carpart.part_photos.all()  # Если у вас используется related_name='part_photos' в ForeignKey

    return render(request, 'part_detail.html', {'part': carpart, 'part_photos': part_photos})


def part_filter(request):
    filter = CarPartFilter(request.GET, queryset=CarPart.objects.all())
    
    if filter.is_valid():
        parts = filter.qs
    else:
        parts = CarPart.objects.all()  
        
    return render(request, 'part_filter.html', {'filter': filter, 'parts': parts})


