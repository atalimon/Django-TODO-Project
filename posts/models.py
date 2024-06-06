from django.db import models
from profiles.models import CustomUser
from django.core.validators import MinValueValidator
from django.utils import timezone

class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add=True)
    target_date = models.DateTimeField(validators=[MinValueValidator(limit_value=timezone.now)])
    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title','completed','created_at', 'target_date']

