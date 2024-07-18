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


class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_property')
    property_name = models.CharField(max_length=100)
    role = models.CharField(max_length=6, choices=ROLES)
    # address
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address1 = models.CharField(max_length=500)
    address2 = models.CharField(max_length=500, blank=True)
    nearby = models.CharField(max_length=200, blank=True)
    total_amount = models.IntegerField()
    rate = models.IntegerField() 
    advance_payment = models.IntegerField()
    payment_condition = models.IntegerField()
    expenses = models.IntegerField()
    registry_date = models.DateField() 
    sai = models.IntegerField()
    size = models.FloatField()
    size_unit = models.CharField(max_length=5, choices=SIZE_UNITS)

    def __str__(self):
        return self.property_name