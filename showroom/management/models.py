from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    ROLE_CHOICES = [
        ('Manager', 'Manager'),
        ('Employee', 'Employee'),
        ('Mechanic', 'Mechanic'),
        ('Customer', 'Customer'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class Car(models.Model):
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)

class Service(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=100)

class Insurance(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    policy_number = models.CharField(max_length=100)
    expiry_date = models.DateField()
    status = models.CharField(max_length=50)
