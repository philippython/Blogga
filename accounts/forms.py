from django.core  import validators
from django.core.mail import send_mail
from .models import BlogUser
from django import forms


class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=100, validators=[validators.validate_email])
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model  = BlogUser
        fields = ['first_name', 'last_name', 'username']

    def send_email(self):
        first_name = self.cleaned_data['first_name']
        email = self.cleaned_data['email']
        send_mail('Welcome to Blogga', "Hello %s Welcome to Blogga" % (first_name), 'odulajaphilip@gmail.com', email)
