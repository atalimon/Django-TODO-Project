from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, CustomAuthForm
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = CustomAuthForm
    success_url = reverse_lazy('register')

class CustomRegisterForm(CreateView):
    template_name = 'accounts/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')