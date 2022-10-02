from django.urls import reverse_lazy
from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from .forms import UserForm

# Create your views here.
class SignUpView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('verify_email')

    def form_valid(self, form):
        
        html_content = 'accounts/verify.html'
        context_data = {'name' : form.cleaned_data['first_name'], 'username' : form.cleaned_data.get('username')}
        email_html_template =get_template(html_content).render(context_data)
        msg = EmailMessage('Welcome to Blogga', email_html_template, settings.EMAIL_HOST_USER, [form.cleaned_data['email']])
        msg.content_subtype = 'html'
        msg.send(fail_silently=False)

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


def confirm_email(request):
    
    if request.method == 'GET':
        user = get_object_or_404(User, username=request.username)
        user.is_active = True
        user.save()
        return redirect('login')