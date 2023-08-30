from django.db import models

class RuleType(models.TextChoices):
    RIGHT = "right", "правый"
    LEFT = "left", "левый"


class DriveType(models.TextChoices):
    front_wheel = ('front wheel' , 'передний')
    rear = ('rear' , 'задний привод')
    four_wheel= ('four wheel' , 'полный привод')


class GearboxType(models.TextChoices):
    machine = ('machine' , 'автомат')
    tiptronic = ('tiptronic' , 'типтроник')
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
    cleared_by_customs = ('cleared by customs' , 'расстаможен')
    not_cleared = ('not cleared' , 'не расстаможен')

class ConditionType(models.TextChoices):
    excellent = ('excellent' , 'отличное')
    good = ('good' , 'хорошее')
    average = ('average' , 'среднее')
    satisfactory = ('satisfactory' , 'удовлетворительное')
    needs_repair = ('needs repair' , 'требует ремонт')
    emergency = ('emergency' , 'аварийное')

class Color(models.TextChoices):
    white = ('white' , 'белый')
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
    yes = ('yes' , 'есть VIN-код')
    no = ('no' , 'нет VIN-код')

class Engine(models.TextChoices):
    petrol = ('petrol' , 'бензин')
    diesel = ('diesel' , 'дизель')  
    hybrid = ('hybrid' , 'гибрид')
    electric_fuel = ('electric fuel' , 'электро')


class Currency(models.TextChoices):
    USD = ('USD' , 'В долларах')
    KGZ = ('KGZ' , 'В сомах')

class Number(models.TextChoices):
    hide = ('hide' , 'скрыть номер телефона')
    show = ('show' , 'показать номер телефона')