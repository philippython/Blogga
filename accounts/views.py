from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserForm

# Create your views here.
def SignUpView(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})