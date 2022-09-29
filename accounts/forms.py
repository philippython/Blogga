from django.core  import validators
from django.core.mail import send_mail
from django import forms


class UserForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    username = forms.CharField(required=True)
    email = forms.EmailField(max_length=100, validators=[validators.validate_email])
    password = forms.PasswordInput()

    def send_email(self):
        first_name = self.cleaned_data['first_name']
        email = self.cleaned_data['email']
        send_mail('Welcome to Blogga', "Hello %s Welcome to Blogga" % (first_name), 'odulajaphilip@gmail.com', email)
