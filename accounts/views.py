from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import BlogUser 
from .forms import UserForm

# Create your views here.
class SignUpView(CreateView):
    model = BlogUser
    form_class = UserForm
    template_name = 'accounts/user_create_form.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form ):

        form.send_email
        return super().form_valid(form)