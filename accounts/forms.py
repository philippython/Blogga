from django.core import validators
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(max_length=100, validators=[validators.validate_email])
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model  = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    