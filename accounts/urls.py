from django.urls import path
from .views import SignUpView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('login', LoginView.as_view(template_name='accounts/registration.html', next_page='accounts/home.html'), name='login')
]
