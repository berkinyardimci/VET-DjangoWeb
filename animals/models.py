from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name

class Genus(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name

class Animal(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    type = models.ForeignKey(Type,on_delete=models.DO_NOTHING, related_name='type')
    genus = models.ForeignKey(Genus,on_delete=models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    available = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="courses/%Y/%m/%d/")
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name