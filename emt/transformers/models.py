from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    

class Transformer(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=150, unique=True)
    alternate_mode = models.CharField(
        max_length=250,
        blank=True,
        null=True)
    description = models.CharField(
        max_length=500,
        blank=True,
        null=True)
    alive = models.BooleanField(default=False)
  
    class Meta:
        ordering = ('name',)
  
    def __str__(self):
        return self.name
