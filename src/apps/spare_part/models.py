from django.db import models

# Create your models here.

class Car_Part_Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Car part Brand"

class CarPart(models.Model):
    name = models.CharField(max_length=200)        # Название запчасти
    car_model = models.CharField(max_length=100)    # Модель автомобиля, к которой подходит запчасть
    year_from = models.PositiveIntegerField()       # Год выпуска автомобиля, начиная с которого подходит запчасть
    year_to = models.PositiveIntegerField()         # Год выпуска автомобиля, до которого подходит запчасть
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена запчасти

    manufacturer = models.CharField(max_length=100)  # Производитель запчасти
    condition = models.CharField(max_length=50)      # Состояние запчасти (новая, б/у и т.д.)
    location = models.CharField(max_length=100)      # Местонахождение запчасти (например, склад, магазин)
    is_available = models.BooleanField(default=True) # Флаг доступности запчасти

    description = models.TextField(blank=True, null=True)  # Описание запчасти
    seller_contact = models.CharField(max_length=100)       # Контактная информация продавца
    car_part_brand = models.ForeignKey(Car_Part_Brand, on_delete=models.CASCADE , related_name= "carparts") # бренд запчасти

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Car part"


class CarPartImage(models.Model):
    car_part = models.ForeignKey(CarPart, on_delete=models.CASCADE)
    image = models.ImageField("Изображение")# ,upload_to="/images/"
    is_main = models.BooleanField("Главное фото", default=False)

    class Meta:
        verbose_name_plural="Car part image"