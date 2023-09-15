import django_filters
from .models import *

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Row, Column

class CarPartFilter(django_filters.FilterSet):
    car_part_brand = django_filters.ModelChoiceFilter(
        field_name='car_part_brand',
        queryset=Car_Part_Brand.objects.all(),
        label='Фирма'
    )

    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label='Название'
    )

    car_model = django_filters.ModelChoiceFilter(
        field_name='car_model',
        queryset=CarMake.objects.all(),
        label='Модель автомобиля'
    )

    year_from = django_filters.NumberFilter(
        field_name='year',
        lookup_expr='gte',
        label='Год от:'
    )

    year_to = django_filters.NumberFilter(
        field_name='year',
        lookup_expr='lte',
        label='Год до:'
    )

    price_from = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte',
        label='Цена от:'
    )

    price_to = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte',
        label='Цена до:'
    )

    condition = django_filters.ChoiceFilter(
        field_name='condition',
        choices=Condition.choices,
        label='Состояние'
    )

    location = django_filters.CharFilter(
        field_name='location',
        lookup_expr='icontains',
        label='Местонахождение'
    )

    is_available = django_filters.BooleanFilter(
        field_name='is_available',
        label='В наличии'
    )


    # Add more filter fields as needed for other fields in the CarPart model.

    class Meta:
        model = CarPart
        fields = []