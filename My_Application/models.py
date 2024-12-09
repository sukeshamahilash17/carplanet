# models.py
from django.db import models

# Contact Model (storing basic contact information)
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    
    
    def __str__(self):
        return self.name

# Booking Model (storing booking details)
class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    car_type = models.CharField(max_length=20)
    pick_up_location = models.CharField(max_length=255)
    drop_off_location = models.CharField(max_length=255)
    pick_up_date = models.DateField()
    drop_off_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.car_type}"
