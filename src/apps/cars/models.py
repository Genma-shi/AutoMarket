from src.apps.user.models import User
from src.apps.cars.choices import *

class CarMake(models.Model):
    name = models.CharField(max_length=100, verbose_name='Марка')
    
    def __str__(self):
        return self.name

class CarModel(models.Model):
    cars = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name="models",null=True)
    name = models.CharField(max_length=100, verbose_name='Модель')
    
    def __str__(self):
        return self.name
    

class Special_notes(models.Model):
    name = models.CharField(max_length=150, verbose_name='Особенные приметы' , null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.name}"

class Car(models.Model):
    mark = models.ForeignKey(CarMake, on_delete=models.CASCADE, verbose_name='Марка')
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name='Модель')
    owner = models.ForeignKey(User, on_delete=models.CASCADE , related_name= "Владелец")    
    description = models.CharField("Описание" , max_length=500 , null=True)
    year = models.PositiveIntegerField(verbose_name='Год выпуска')
    
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    body_type = models.CharField("Тип кузова", max_length=13, choices=BodyType.choices)
    engine = models.CharField("топливо", max_length=13, choices=Engine.choices)
    
    views_count = models.PositiveIntegerField("Количество просмотров", default=0)
    mileage = models.PositiveIntegerField(verbose_name='Пробег', default=0, help_text="Км")
   
    drive = models.CharField("привод", max_length=20, choices=DriveType.choices)
    gearbox = models.CharField("коробка передач", max_length=15, choices=GearboxType.choices)
    engine_capacity = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Объем двигателя л')
    ruletype = models.CharField("Тип руля", max_length=5, choices=RuleType.choices, default=RuleType.LEFT)
    color = models.CharField("цвет автомобиля", max_length=15, choices=Color.choices)

    location = models.URLField("Адрес" ,max_length=200 , null=True , blank=True)

    condition = models.CharField("состояние", max_length=21, choices=ConditionType.choices)
    customs_cleared = models.CharField("расстаможен", max_length=25, choices=Customs_cleared.choices)
    vin_code = models.CharField("наличие вин кода",max_length=5,choices=VINcode.choices, default= False ,blank=True,)
    currency = models.CharField("валюта" , max_length=11 , choices=Currency.choices , default= Currency.USD)
    special_notes = models.ManyToManyField(Special_notes  , blank=True)
    additional_note = models.CharField("Дополнительние приметы", max_length=255, null=True, blank=True)


    def __str__(self):
        return f"{self.mark} {self.model} ({self.year})"


class CarPhoto(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='photos', null=True)
    image = models.ImageField("Изображение",
          upload_to="cars/images/", 
          null=True,blank=True
          )
    is_main = models.BooleanField("Главное фото", default=False)
    
    
    class Meta:
        verbose_name_plural="Car image" 


    def __str__(self):
        return "Photos"