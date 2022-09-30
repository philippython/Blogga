from django.urls import reverse_lazy
from django.views.generic.edit import CreateView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
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

class ProfileView(LoginRequiredMixin, DetailView):

    template_name = 'accounts/index.html'


    def get_object(self):
        user = get_object_or_404(User, pk=self.request.user.id)
        return user
    