import django_filters
from .models import *

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Row, Column

class CarFilter(django_filters.FilterSet):
                
    make = django_filters.ModelChoiceFilter(
        field_name='mark',
        queryset=CarMake.objects.all(),
        label='Марка'
    )

    model = django_filters.ModelChoiceFilter(
        field_name='model',
        queryset=CarModel.objects.all(),
        label='Модель'
    )

    year_min = django_filters.NumberFilter(
        field_name='year',
        lookup_expr='gte',
        label='Год от:'
    )

    year_max = django_filters.NumberFilter(
        field_name='year',
        lookup_expr='lte',
        label='Год до:'
    )

    price_min = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte',
        label='Цена от:'
    )

    price_max = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte',
        label='Цена до:'
    )

    class Meta:
        model = Car
        fields = []
