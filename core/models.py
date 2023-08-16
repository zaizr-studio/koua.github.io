from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    verified_email = models.BooleanField(default=False)

class Product(models.Model):
    TYPES = [
        ('N', 'None'),
        ('E', 'Electronics'),
        ('F', 'Furnitures'),
        ('H', 'Houseware'),
        ('T', 'Toys'),
        ('B', 'Books')
    ]
    title = models.CharField(max_length=255)
    label = models.CharField(max_length=750, default='')
    image = models.FileField(null=True)
    category = models.CharField(max_length=1, choices=TYPES, default='N')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)