from django.db import models
from src.apps.account.models import User

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Country"


class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE , related_name= "cars")   # владелец автомобиля    

    make = models.CharField(max_length=100)         # Марка автомобиля (например, Toyota)
    model = models.CharField(max_length=100)        # Модель автомобиля (например, Corolla)
    year = models.PositiveIntegerField()           # Год выпуска
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена автомобиля
    mileage = models.PositiveIntegerField()        # Пробег автомобиля в километрах

    color = models.CharField(max_length=50)         # Цвет автомобиля
    transmission = models.CharField(max_length=50)  # Тип трансмиссии (автоматическая, механическая)
    fuel_type = models.CharField(max_length=50)     # Тип топлива (бензин, дизель и т.д.)
    engine_capacity = models.DecimalField(max_digits=4, decimal_places=2)  # Объем двигателя

    description = models.TextField(blank=True, null=True)  # Описание автомобиля
    country = models.ForeignKey(Country, on_delete=models.CASCADE , related_name= "cars") # страна производителя

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
    class Meta:
        verbose_name_plural="Car"


class RuleType(models.TextChoices):
    RIGHT = "right", "Правый"
    LEFT = "left", "Левый"

class CarPhoto(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    image = models.ImageField("Изображение")# ,upload_to="/images/"
    is_main = models.BooleanField("Главное фото", default=False)
    class Meta:
        verbose_name_plural="Car image" 



class DriveType(models.TextChoices):
    front_wheel = ('front wheel' , 'передний')
    rear = ('rear' , 'задний привод')
    four_wheel= ('four wheel' , 'полный привод')


class GearboxType(models.TextChoices):
    tiptronic = ('tiptronic' , 'типтроник')
    machine = ('machine' , 'автомат')
    mechanics = ('mechanics' , 'механика')
    variable_speed = ('variable speed' , 'вариатор')
    rotbot = ('robot' , 'робот')
   

class BodyType(models.TextChoices):
    sedan = ('sedan', 'седан')
    hatchback = ('hatchback', 'хэтчбек')
    SUV = ('SUV', 'внедорожник')
    coupe = ('coupe', 'купе')
    universal = ('universal', 'универсал')
    crossover = ('crossover' , 'кроссовер')
    minivan = ('minivan' , 'минивен')
    truck = ('truck' , 'грузовик')

    def __str__(self):
        return self.name

class Customs_cleared(models.TextChoices):
    cleared_by_customs = True #('cleared by customs' , 'расстаможен')
    not_cleared = False #('not cleared' , 'не расстаможен')

class ConditionType(models.TextChoices):
    excellent = ('excellent' , 'отличное')
    good = ('good' , 'хорошее')
    average = ('average' , 'среднее')
    satisfactory = ('satisfactory' , 'удовлетворительное')
    needs_repair = ('needs repair' , 'требует ремонт')
    emergency = ('emergency' , 'аварийное')

    def __str__(self):
        return self.name
    
class Color(models.TextChoices):
    red = ('red', 'красный')
    blue = ('blue', 'синий')
    black = ('black', 'черный')
    silver = ('silver', 'серебристый')
    gray = ('gray', 'серый')
    green = ('green', 'зеленый')
    yellow = ('yellow', 'желтый')
    orange = ('orange', 'оранжевый')
    brown = ('brown', 'коричневый')
    gold = ('gold', 'золотистый')
    pink = ('pink', 'розовый')
    beige = ('beige', 'бежевый')
    violet = ('violet', 'фиолетовый')
    burgundy = ('burgundy', 'бордовый')

class VINcode(models.TextChoices):
    yes = True
    no = False

class Special_notes(models.TextChoices):
    body_kit = ('body kit' , 'обвес')
    gas_equipment = ('gas equipment' , 'газовое оборудование')
    whole_car_tint = ('whole car tint' , 'тонировка')
    spoiler = ('spoiler' , 'спойлер')
    luke = ('luke' , 'люк')


    
class Car(models.Model):
    MARK_AND_MODEL_MAX_LENGTH = 100
    ENGINE_MAX_LENGTH = 50
    VIN_CODE_MAX_LENGTH = 17
    COLOR_MAX_LENGTH = 50   
    SPECIAL_NOTES_MAX_LENGTH = 200

    mark = models.CharField(max_length=MARK_AND_MODEL_MAX_LENGTH, verbose_name='Марка')

    model = models.CharField(max_length=MARK_AND_MODEL_MAX_LENGTH, verbose_name='Модель')
    
    year = models.PositiveIntegerField(verbose_name='Год выпуска')
    
    body_type = models.CharField("Тип кузова", max_length=13, choices=BodyType.choices)
    engine = models.CharField(max_length=ENGINE_MAX_LENGTH, verbose_name='Двигатель')

    drive = models.CharField("привод", max_length=20, choices=DriveType.choices)
    gearbox = models.CharField("коробка передач", max_length=15, choices=GearboxType.choices)
    engine_volume = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Объем двигателя л')
    ruletype = models.CharField("Тип руля", max_length=5, choices=RuleType.choices, default=RuleType.LEFT)
    color = models.CharField("цвет автомобиля", max_length=15, choices=Color.choices)
    condition = models.CharField("состояние", max_length=21, choices=ConditionType.choices)
    customs_cleared = models.BooleanField("расстаможен", max_length=25, choices=Customs_cleared.choices)
    vin_code = models.CharField(models.CharField("наличие вин кода", max_length=5, choices=VINcode.choices , default=VINcode.no))
    special_notes = models.CharField("внешние особбености", max_length=15, choices=Special_notes.choices)
    def __str__(self):
        return f"{self.mark} {self.model} ({self.year})"