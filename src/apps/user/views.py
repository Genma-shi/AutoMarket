from django.shortcuts import render , redirect
from .forms import CustomUserChangeForm
from .models import User
from src.apps.cars.models import Car

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
# Create your views here.
def login_view(request):
    return render(request, 'login.html')

@login_required
def  profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    cars = Car.objects.filter(owner=user)

    context = {
        'profile_user': user,
        'cars': cars,
    }
    return render(request, 'profile.html', context)

def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # Вы можете выполнить дополнительные действия после изменения данных пользователя
            profile_url = reverse('profile', args=[request.user.pk])
            # Перенаправляем пользователя на страницу профиля
            return redirect(profile_url)
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})


def user_cars(request):
    user = request.user
    cars = Car.objects.filter(owner=user)
    return render(request, 'user_cars.html', {'cars': cars})