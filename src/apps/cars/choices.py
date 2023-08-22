from django.db import models

class RuleType(models.TextChoices):
    RIGHT = "right", "Правый"
    LEFT = "left", "Левый"


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

class Engine(models.TextChoices):
    petrol = ('petrol' , 'бензин')
    diesel = ('diesel' , 'дизель')
    gas = ('gas' , 'газ')
    hybrid = ('hybrid' , 'гибрид')
    electric_fuel = ('electric fuel' , 'электро')
