from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField()

