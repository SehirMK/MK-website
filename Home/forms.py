from django import forms
from django.core import validators
from Home.models import User

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name must start with z')

class FormName(forms.ModelForm):
    """
    fname = forms.CharField(label='First Name',validators=[check_for_z])
    sname = forms.CharField(label='Surname', validators=[check_for_z])
    email = forms.EmailField(label='Email Address')
    verify_email = forms.EmailField(label='Verify Email Address')
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
    """
    class Meta:
        model = User
        fields = '__all__'
