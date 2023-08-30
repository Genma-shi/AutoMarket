from django import forms
from .models import *
from django.forms.models import inlineformset_factory

from django import forms


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result



class CarForm(forms.ModelForm):
    mark = forms.ModelChoiceField(queryset=CarMake.objects.all(), label='Марка')
    model = forms.ModelChoiceField(queryset=CarModel.objects.all(), label='Модель')
    currency = forms.ChoiceField(choices=Currency.choices, label='Валюта')
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Цена')  
    description = forms.CharField(max_length=500 , label="описание")
    year = forms.IntegerField(max_value=4 , label='Год выпуска')
    body_type = forms.ChoiceField(choices=BodyType.choices, label='Тип кузова')
    engine = forms.ChoiceField(choices=Engine.choices, label='Топливо')
    engine_capacity = forms.DecimalField(max_digits=4, decimal_places=1, label='Объем двигателя (л)')
    drive = forms.ChoiceField(choices=DriveType.choices, label='Привод')
    gearbox = forms.ChoiceField(choices=GearboxType.choices, label='Коробка передач')
    ruletype = forms.ChoiceField(choices=RuleType.choices, label='Тип руля')
    color = forms.ChoiceField(choices=Color.choices, label='Цвет автомобиля')
    condition = forms.ChoiceField(choices=ConditionType.choices, label='Состояние')
    customs_cleared = forms.ChoiceField(choices=Customs_cleared.choices, label='Расстаможен')
    vin_code = forms.ChoiceField(choices=VINcode.choices, label='Наличие VIN кода')

    special_notes = forms.ModelMultipleChoiceField(
        queryset=Special_notes.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Особенные приметы'
    )

    photos = MultipleFileField()
    
    class Meta:
        model = Car
        
        fields = ['mark', 'model', 'year', 'description' , 'body_type', 'ruletype', 'drive', 'gearbox', 'engine',
                'engine_capacity', 'color', 'condition', 'customs_cleared', 
                'vin_code' , 'currency' , 'price' , 'special_notes' 
        ]

class CarPhotoForm(forms.ModelForm):
    class Meta:
        model = CarPhoto
        fields = ('image',)

class SpecialNotesForm(forms.ModelForm):
    class Meta:
        model = Special_notes
        fields = '__all__' 

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'avatar', 'mobile', 'favorites_list', 'currency']
        labels = {
            'username': 'Имя пользователя',
            'email': 'Email',
            'avatar': 'Аватарка',
            'mobile': 'Номер телефона',
            'favorites_list': 'Избранные автомобили',
            'currency': 'Валюта'
        }   