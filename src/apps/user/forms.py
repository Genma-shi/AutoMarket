from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Row, Column



class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Profile Details',
                Row(
                    Column('first_name', css_class='col-md-6 my-field-class'),  
                    Column('last_name', css_class='col-md-6 my-field-class'),  
                ),
                Row(
                    Column('mobile', css_class='col-md-6 my-field-class'),  
                    Column('email', css_class='col-md-6 my-field-class'),  
                ),
                Row(
                    Column('currency', css_class='col-md-6 my-field-class'),  
                ),
            ),
            Div(
                Submit('submit', 'Сохранить', css_class='btn btn-primary')
            )
        )

    class Meta:
        model = User    
        fields = ['email', 'avatar', 'mobile', 'currency', 'first_name', 'last_name']