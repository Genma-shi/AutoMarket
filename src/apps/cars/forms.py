from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Row, Column
from django.forms.models import inlineformset_factory

from datetime import datetime
from django import forms
now_year = datetime.now().year

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput)
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result



class CarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                Fieldset(
                    '',
                    Row(
                        Column('mark', css_class='col-md-6 my-field-class'),  
                        Column('model', css_class='col-md-6 my-field-class'),  
                    ),
                    Row(
                        Column('price', css_class='col-md-6 my-field-class'),  
                        Column('currency', css_class='col-md-6 my-field-class'),  
                    ),
                    Row(
                        Column('mileage' , css_class='col-md-6 my-field-class' ) ,
                        Column('year' , css_class='col-md-6 my-field-class')
                    ),
                    Row(
                    Column('description', css_class='col-md-6 my-field-class'),
                    Column('vin_code',css_class='col-md-6'),
                    )   
                     
                ),

            Fieldset(
                '',
                Row(
                    Column('body_type', css_class='form-group col-md-4 mb-0'),
                    Column('engine', css_class='form-group col-md-4 mb-0'),
                    Column('engine_capacity', css_class='form-group col-md-4 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('drive', css_class='form-group col-md-4 mb-0'),
                    Column('gearbox', css_class='form-group col-md-4 mb-0'),
                    Column('ruletype', css_class='form-group col-md-4 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('color', css_class='form-group col-md-4 mb-0'),
                    Column('condition', css_class='form-group col-md-4 mb-0'),
                    Column('customs_cleared', css_class='form-group col-md-4 mb-0'),
                    css_class='form-row'
                ),

                 Fieldset(
                'Фотографии',
                Row(
                    Column(
                        'photos',
                        css_class='col-md-12',
                    ),
                ),

            ),
                Fieldset(
                    'Особенные приметы',
                    Row(
                        Column(
                            'special_notes',
                            css_class='col-md-12',
                        ),
                    ),
                    Row(
                        Column('additional_note', css_class='col-md-6 my-field-class'),
                    ),
                ),
            ) ,
                Div(
                Submit('submit', 'Сохранить'))
            )
        
            
    
    mark = forms.ModelChoiceField(queryset=CarMake.objects.all(), label='Марка' )
    model = forms.ModelChoiceField(queryset=CarModel.objects.all(), label='Модель')
    currency = forms.ChoiceField(choices=Currency.choices, label='Валюта')
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Цена')  
    description = forms.CharField(max_length=500 , label="описание")
    mileage = forms.IntegerField(label='Пробег', min_value=0, required=True)
    year = forms.IntegerField(max_value=now_year, label='Год выпуска')
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
        
        fields = ['mark', 'model', 'year', 'mileage' ,'description' , 'body_type', 'ruletype', 
                'drive', 'gearbox', 'engine',
                'engine_capacity', 'color', 'condition', 'customs_cleared', 
                'vin_code' , 'currency' , 'price' , 'special_notes' , 'photos' , 'additional_note' ,
        ]

class CarPhotoForm(forms.ModelForm):             
    class Meta:
        model = CarPhoto
        fields = ['image',]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'avatar', 'mobile', 'favorites_list', 'currency']
        labels = {
            'email': 'Email',
            'avatar': 'Аватарка',
            'mobile': 'Номер телефона',
            'favorites_list': 'Избранные автомобили',
            'currency': 'Валюта'
        }   

class CarFilterForm(forms.Form):
    makes = CarMake.objects.all().values_list('name', 'name').distinct()
    models = CarModel.objects.all().values_list('name', 'name').distinct()
    years = Car.objects.values_list('year', 'year').distinct()
    # Другие поля формы

    make = forms.ChoiceField(choices=[('', 'Все')] + list(makes), required=False)
    model = forms.ChoiceField(choices=[('', 'Все')] + list(models), required=False)
    year = forms.ChoiceField(choices=[('', 'Все')] + list(years), required=False)
    min_price = forms.DecimalField(min_value=0, required=False, widget=forms.NumberInput(attrs={'placeholder': 'Минимальная цена'}))
    max_price = forms.DecimalField(min_value=0, required=False, widget=forms.NumberInput(attrs={'placeholder': 'Максимальная цена'}))
    # Другие поля формы