from django.urls import path
from .views import SignUpView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('signup', SignUpView, name='signup'),
    path('login', LoginView.as_view(template_name='accounts/registration.html', next_page="homepage"), name='login')
]
