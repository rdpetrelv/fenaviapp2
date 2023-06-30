from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    bodegas_choices = [
        ("MO", 'Monterilla'),
        ("CR", 'Crucero'),
        ("PE", 'Pescador'),
        ("SN", 'San Nicolas'),
    ]
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    bodega =  models.CharField(max_length=2, choices=bodegas_choices, default="MO")
