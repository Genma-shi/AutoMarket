from django.db import models
from src.apps.cars.models import CarMake
# Create your models here.



class Condition(models.TextChoices):
    new = ('new' , 'новая')
    used = ('used' , 'б/у')

class Car_Part_Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Car part Brand"

class CarPart(models.Model):
    name = models.CharField('название',max_length=200)        # Название запчасти
    car_model = models.ManyToManyField(CarMake)    # Модель автомобиля, к которой подходит запчасть
    year = models.PositiveIntegerField('год' )       
    price = models.DecimalField('цена',max_digits=10, decimal_places=2)  # Цена запчасти
    vendor_code = models.CharField('сериный номер',max_length=20 , null=True)                # артикуль 
    condition = models.CharField("состояние", max_length=10, choices=Condition.choices)      # Состояние запчасти (новая, б/у и т.д.)
    location = models.CharField(max_length=100)      # Местонахождение запчасти (например, склад, магазин)
    is_available = models.BooleanField('в наличий' , default=True) # Флаг доступности запчасти

    views_count = models.PositiveIntegerField("Количество просмотров", default=0)
    description = models.TextField('описание' , blank=True, null=True)  # Описание запчасти
    seller_contact = models.CharField('номер телефона' ,max_length=100)       # Контактная информация продавца
    car_part_brand = models.ForeignKey(Car_Part_Brand, on_delete=models.CASCADE , related_name= "carparts") # бренд запчасти

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Car part"


class CarPartImage(models.Model):
    car_part = models.ForeignKey(CarPart, on_delete=models.CASCADE , related_name='part_photos')
    image = models.ImageField("Изображение",
          upload_to="car_part/images/", 
          null=True,blank=True
          )
    is_main = models.BooleanField("Главное фото", default=False)
    class Meta:
        verbose_name_plural="Car part image"