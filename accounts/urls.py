from django.urls import path
from .views import SignUpView, ProfileView , verify_email, confirm_email
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('login', LoginView.as_view(template_name='accounts/registration.html', next_page="account_profile"), name='login'),
    path('profile/<int:pk>', ProfileView.as_view(), name='account_profile'),
    path('verify-email', verify_email, name='verify_email'),
    path('confirm-email/<str:username>', confirm_email, name='confirm_email')
]
