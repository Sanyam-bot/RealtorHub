from django.contrib.auth.models import AbstractUser
from django.db import models


ROLES = (
    ('buyer', 'BUYER'),
    ('seller', 'SELLER'),
    ('dealer', 'DEALER'),
)

SIZE_UNITS = (
    ('sqrt', 'Square Feet'),
    ('marla', 'Marla'),
)

# Create your models here.
class User(AbstractUser):
    pass
    

class Address(models.Model):
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address1 = models.CharField(max_length=500)
    address1 = models.CharField(max_length=500, blank=True)
    nearby = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.state}, {self.city}, {self.address1}'


class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_property')
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=6, choices=ROLES)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='address_property')
    price = models.IntegerField()
    sai = models.IntegerField()
    size = models.FloatField()
    size_unit = models.CharField(max_length=5, choices=SIZE_UNITS)

    def __str__(self):
        return self.name
