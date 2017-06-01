from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name must start with z')

class FormName(forms.Form):
    fname = forms.CharField(label='First Name',validators=[check_for_z])
    sname = forms.CharField(label='Surname', validators=[check_for_z])
    email = forms.EmailField(label='Email Address')
    verify_email = forms.EmailField(label='Verify Email Address')
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if mail != vmail:
            raise forms.ValidationError('Make Sure Emails Match!')
