from django.forms import ModelForm
from django import forms
from .mixins import TargetDateValidationMixin
from django.utils import timezone
from .models import Post
from django.contrib.admin.widgets import AdminDateWidget


class DateInput(forms.DateInput):
    input_type = 'datetime-local'

class PostCreationForm(TargetDateValidationMixin, ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'target_date']
        widgets = {
            'target_date': DateInput(),
        }


class PostUpdateForm(TargetDateValidationMixin, ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'completed', 'target_date']
        widgets = {
            'target_date': forms.DateInput(),
        }

        

   
