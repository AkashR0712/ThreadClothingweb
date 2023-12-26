from django.db import models
from django import forms

from django.db import models
from django import forms

class MultiSelectField(models.Field):
    def __init__(self, *args, **kwargs):
        self.max_length = kwargs.pop('max_length', None)
        kwargs['blank'] = True
        kwargs['null'] = True
        super(MultiSelectField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(MultiSelectField, self).deconstruct()
        kwargs['max_length'] = self.max_length
        return name, path, args, kwargs

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return value.split(',')

    def to_python(self, value):
        if isinstance(value, list):
            return value
        elif value is None:
            return value
        return value.split(',')

    def get_prep_value(self, value):
        if value is None:
            return value
        return ','.join(value)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.MultipleChoiceField,
            'choices': self.choices,
            'widget': forms.CheckboxSelectMultiple,
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)

    def db_type(self, connection):
        return 'text'
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
    image = models.ImageField(upload_to='pics', default=None)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    available_sizes = MultiSelectField(choices=SIZE_CHOICES)
    color = MultiSelectField(choices=[
        ('black', 'Black'),
        ('green', 'Green'),
        ('blue', 'Blue'),
        ('pink', 'Pink'),
        ('white', 'White'),
        ('yellow', 'Yellow'),
    ])
    material = models.CharField(max_length=255)
    fit = models.CharField(max_length=10, choices=FIT_CHOICES)
    sleeve = models.CharField(max_length=10, choices=SLEEVE_CHOICES)
    wash = models.CharField(max_length=10, choices=WASH_CHOICES)
    occasion = models.CharField(max_length=255)
    neck_type = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        abstract = True

class MenTshirt(Product):
    pass

class WomenTshirt(Product):
    pass

class MenOversizedTshirt(Product):
    pass

class WomenOversizedTshirt(Product):
    pass
