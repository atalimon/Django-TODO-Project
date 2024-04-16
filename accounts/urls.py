from django.urls import path
from . import views
from .views import CustomLoginView, CustomRegisterForm

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', CustomRegisterForm.as_view(), name='register'),
]