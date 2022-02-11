from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Animal(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    genus = models.CharField(max_length=30)
    age = models.IntegerField()
    available = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="courses/%Y/%m/%d/")
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name