from django.db import models
from profiles.models import CustomUser

class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title','completed','created_at']

