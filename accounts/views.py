from django.urls import reverse_lazy
from django.views.generic.edit import CreateView 
from django.views.generic import DetailView
from django.contrib.auth.models import User
from .forms import UserForm

# Create your views here.
class SignUpView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.set_password(form.cleaned_data['password'])
        return super(SignUpView, self).form_valid(form)

class ProfileView(DetailView):
    model = User