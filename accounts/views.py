from django.urls import reverse_lazy
from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template.loader import get_template
from django.template import Context
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
    success_url = reverse_lazy('verify_email')

    def form_valid(self, form):
        
        subject, from_email, to = 'Welcome to Blogga', settings.EMAIL_HOST_USER , form.cleaned_data['email']
        template = get_template('accounts/verification.html')
        context = dict({'user': form.cleaned_data['first_name']})
        content = template.render(context)
        msg = EmailMessage(subject, content, from_email, to=[to])
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