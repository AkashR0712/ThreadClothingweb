from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.postgres.fields import ArrayField

# Create your models here.
# models.py

# Base class
class Product(models.Model):
   

    FIT_CHOICES = [
        ('regular', 'Regular Fit'),
        ('slim', 'Slim Fit'),
        ('loose', 'Loose Fit'),
    ]

    SLEEVE_CHOICES = [
        ('short', 'Short Sleeve'),
        ('long', 'Long Sleeve'),
    ]

    WASH_CHOICES = [
        ('machine', 'Machine Wash'),
        ('hand', 'Hand Wash'),
    ]

    
    name = models.CharField(max_length=255) 
    image = models.ImageField(upload_to='pics', default=None)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    available_sizes = models.TextField()
    color = models.TextField()
    material = models.CharField(max_length=255)
    fit = models.CharField(max_length=10, choices=FIT_CHOICES)
    sleeve = models.CharField(max_length=10, choices=SLEEVE_CHOICES)
    wash = models.CharField(max_length=10, choices=WASH_CHOICES)
    occasion = models.CharField(max_length=255)
    neck_type = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        abstract = True

# Inheriting base class
class MenTshirt(Product):
    pass

class WomenTshirt(Product):
    pass

class MenOversizedTshirt(Product):
    pass

class WomenOversizedTshirt(Product):
    pass
