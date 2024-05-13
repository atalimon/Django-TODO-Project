from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, CustomAuthForm
from django.contrib.auth.views import LoginView, LogoutView

# log in, logout, reg, password change. 
class CustomLoginView(LoginView):
    template_name = 'profiles/login.html'
    form_class = CustomAuthForm
    success_url = reverse_lazy('posts')

class CustomRegisterForm(CreateView):
    template_name = 'profiles/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
