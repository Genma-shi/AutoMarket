from src.apps.account.models import User
from src.apps.cars.choices import *


class CarMake(models.Model):
    name = models.CharField(max_length=100, verbose_name='Марка')
    def __str__(self):
        return self.name

class CarModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Модель')
    def __str__(self):
        return self.name

class Car(models.Model):
    mark = models.ForeignKey(CarMake, on_delete=models.CASCADE, verbose_name='Марка')
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name='Модель')
    owner = models.ForeignKey(User, on_delete=models.CASCADE , related_name= "Владелец")    

    year = models.PositiveIntegerField(verbose_name='Год выпуска')
    
    body_type = models.CharField("Тип кузова", max_length=13, choices=BodyType.choices)
    engine = models.CharField("топливо", max_length=13, choices=BodyType.choices)

    drive = models.CharField("привод", max_length=20, choices=DriveType.choices)
    gearbox = models.CharField("коробка передач", max_length=15, choices=GearboxType.choices)
    engine_capacity = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Объем двигателя л')
    ruletype = models.CharField("Тип руля", max_length=5, choices=RuleType.choices, default=RuleType.LEFT)
    color = models.CharField("цвет автомобиля", max_length=15, choices=Color.choices)
    condition = models.CharField("состояние", max_length=21, choices=ConditionType.choices)
    customs_cleared = models.BooleanField("расстаможен", max_length=25, choices=Customs_cleared.choices)
    vin_code = models.CharField("наличие вин кода",max_length=5,choices=VINcode.choices, default= False ,blank=True,)
    special_notes = models.CharField("внешние особбености", max_length=15, choices=Special_notes.choices ,null=True , blank=True)

    def __str__(self):
        return f"{self.mark} {self.model} ({self.year})"

class CarPhoto(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    image = models.ImageField("Изображение")# ,upload_to="/images/"
    is_main = models.BooleanField("Главное фото", default=False)
    class Meta:
        verbose_name_plural="Car image" 