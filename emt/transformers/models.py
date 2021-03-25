from django.db import models
from django.contrib.auth.models import User

class Transformer(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
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
