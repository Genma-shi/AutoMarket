from django import forms
from .models import *

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['mark', 'model', 'owner', 'year', 'body_type', 'engine', 'drive', 'gearbox', 'engine_capacity', 'ruletype', 'color', 'condition', 'customs_cleared', 'vin_code', 'special_notes']

    mark = forms.ModelChoiceField(queryset=CarMake.objects.all(), label='Марка')
    model = forms.ModelChoiceField(queryset=CarModel.objects.all(), label='Модель')
    owner = forms.ModelChoiceField(queryset=User.objects.all(), label='Владелец')
    year = forms.IntegerField(label='Год выпуска')
    body_type = forms.ChoiceField(choices=BodyType.choices, label='Тип кузова')
    engine = forms.ChoiceField(choices=Engine.choices, label='Топливо')
    drive = forms.ChoiceField(choices=DriveType.choices, label='Привод')
    gearbox = forms.ChoiceField(choices=GearboxType.choices, label='Коробка передач')
    engine_capacity = forms.DecimalField(max_digits=4, decimal_places=1, label='Объем двигателя (л)')
    ruletype = forms.ChoiceField(choices=RuleType.choices, label='Тип руля')
    color = forms.ChoiceField(choices=Color.choices, label='Цвет автомобиля')
    condition = forms.ChoiceField(choices=ConditionType.choices, label='Состояние')
    customs_cleared = forms.ChoiceField(choices=Customs_cleared.choices, label='Расстаможен')
    vin_code = forms.ChoiceField(choices=VINcode.choices, label='Наличие VIN кода')
    special_notes = forms.MultipleChoiceField(choices=Special_notes.choices, label='Внешние особенности', widget=forms.CheckboxSelectMultiple)