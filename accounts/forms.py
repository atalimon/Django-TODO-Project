from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    user_name = forms.CharField(max_length=30,error_messages={'required':'please enter a valid username'})
    email = forms.EmailField(max_length=30 ,
        error_messages={'required':'please enter a valid email'})
    
    password1 = forms.CharField()
    password2 = forms.CharField()


    class Meta:
        model = CustomUser
        fields = ( 'email', 'user_name' ,'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomAuthForm(AuthenticationForm):
    email = forms.EmailField() 
    password = forms.CharField()

    class Meta:
        model = CustomUser
        fields = ['email', 'password']