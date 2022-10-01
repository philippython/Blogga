from django.urls import reverse_lazy
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render
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
        
        subject, from_email, to = 'Welcome to Blogga', settings.EMAIL_HOST_USER , form.cleaned_data['email']
        text_content = 'hello %s , welcome to Blogga' % (form.cleaned_data['first_name'])
        html_content = 'accounts/verification.html'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        form.instance.set_password(form.cleaned_data['password'])
        form.instance.is_active = False
        form.instance.save()
        return super(SignUpView, self).form_valid(form)


class ProfileView(LoginRequiredMixin, DetailView):

    template_name = 'accounts/index.html'


    def get_object(self):
        user = get_object_or_404(User, pk=self.request.user.id)
        return user
    
def verify_email(request):

    return render(request, 'accounts/verification.html')