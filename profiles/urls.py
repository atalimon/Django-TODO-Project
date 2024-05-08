from django.urls import path
from . import views
from .views import CustomLoginView, CustomRegisterForm
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', CustomRegisterForm.as_view(), name='register'),
]