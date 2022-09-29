from django.core  import validators
from django.core.mail import send_mail
from django import forms


class UserForm(forms.Form):
    first_name = forms.CharField(max_length=50 , blank=False)
    last_name = forms.CharField(max_length=50, blank=False)
    username = forms.CharField(max_length=30, unique=True)
    email = forms.EmailField(max_length=100, unique=True, validators=[validators.validate_email])
    password = forms.PasswordInput(max_length=50)

    def send_mail(self):
        first_name = self.cleaned_data['first_name']
        email = self.cleaned_data['email']
        

        send_mail('Welcome to Blogga')