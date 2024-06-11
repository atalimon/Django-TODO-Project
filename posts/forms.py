from django.forms import ModelForm
from django import forms, forms
from django.utils import timezone
from .models import Post



class DateTimeInput(forms.DateTimeInput):
    input_type = 'text'

class PostCreationForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'target_date']
        widgets = {
            'target_date': DateTimeInput(),
        }


class PostUpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'completed', 'target_date']
        widgets = {
            'target_date': DateTimeInput(),
        }