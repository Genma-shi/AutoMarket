from django import forms
from .models import CarPart , CarPartImage


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Row, Column
from crispy_forms.bootstrap import Field, InlineRadios, StrictButton

from django.forms.widgets import ClearableFileInput

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
 


class CarPartForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                '',
                Row(
                    Column('car_model', css_class='col-md-3 my-field-class'),
                    Column('car_part_brand', css_class='col-md-3 my-field-class'),
                    Column('condition', css_class='col-md-3 my-field-class'),
                    Column('is_available', css_class='col-md-3 my-field-class'),
                ),
                Row(
                    Column('name', css_class='col-md-4 my-field-class'),
                    Column('year', css_class='col-md-4 my-field-class'),
                    Column('price', css_class='col-md-4 my-field-class'),
                ),
                Row(
                    Column('vendor_code', css_class='col-md-4 my-field-class'),
                    Column('seller_contact', css_class='col-md-4 my-field-class'),
                    Column('location', css_class='col-md-4 my-field-class'),
                ),
                Row(
                    Column('description', css_class='col-md-10 my-field-class'),
                ),
            ),
            Fieldset(
                'Photos',
                Row(
                    Column(
                        'part_photos', css_class='col-md-10',
                    ),
                ),
            ),
            Div(
                Submit('submit', 'Сохранить')
            )
        )

    part_photos = MultipleFileField(widget=MultipleFileInput)

    class Meta:
        model = CarPart
        fields = ['name','car_model','year','price','vendor_code','condition','location',
                'is_available','description','seller_contact','car_part_brand',]
    widgets = {
        'description': forms.Textarea(attrs={'rows': 4}),
    }

class CarPartPhotoForm(forms.ModelForm):
    class Meta:
        model = CarPartImage
        fields = ('image',)