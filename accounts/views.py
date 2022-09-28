from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

# Create your views here.
class SignUpView(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'password', 'email']
    template_name = 'accounts/user_create_form.html'