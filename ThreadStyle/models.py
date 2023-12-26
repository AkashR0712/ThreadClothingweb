from django.db import models

# Create your models here.
# models.py

#base class
class Product(models.Model):
    SIZE_CHOICES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]

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
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    available_sizes = models.CharField(max_length=10, choices=SIZE_CHOICES, blank=True, null=True)
    color = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    fit = models.CharField(max_length=10, choices=FIT_CHOICES)
    sleeve = models.CharField(max_length=10, choices=SLEEVE_CHOICES)
    wash = models.CharField(max_length=10, choices=WASH_CHOICES)
    occasion = models.CharField(max_length=255)
    neck_type = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        abstract = True

#Inheriting base class
class MenTshirt(Product):
    pass

class WomenTshirt(Product):
    pass

class MenOversizedTshirt(Product):
    pass

class WomenOversizedTshirt(Product):
    pass  

