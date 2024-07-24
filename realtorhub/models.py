from django.contrib.auth.models import AbstractUser
from django.db import models


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
    buyer = models.CharField(max_length=50, blank=True)
    seller = models.CharField(max_length=50, blank=True)
    dealer = models.CharField(max_length=50, blank=True)
    # address
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address1 = models.CharField(max_length=500)
    address2 = models.CharField(max_length=500, blank=True)
    nearby = models.CharField(max_length=200, blank=True)
    total_amount = models.IntegerField()
    rate = models.IntegerField() 
    advance_payment = models.IntegerField()
    expenses = models.IntegerField()
    registry_date = models.DateField() 
    sai = models.IntegerField()
    size = models.CharField(max_length=10)
    size_unit = models.CharField(max_length=5, choices=SIZE_UNITS)

    def __str__(self):
        return self.property_name