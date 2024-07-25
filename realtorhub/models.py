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
    buyer_1 = models.CharField(max_length=50, blank=True, verbose_name='Buyers')
    buyer_2 = models.CharField(max_length=50, blank=True)
    buyer_3 = models.CharField(max_length=50, blank=True)
    buyer_4 = models.CharField(max_length=50, blank=True)
    buyer_5 = models.CharField(max_length=50, blank=True)
    seller = models.CharField(max_length=50, blank=True)
    dealer_1 = models.CharField(max_length=50, blank=True, verbose_name='Dealers')
    dealer_2 = models.CharField(max_length=50, blank=True)
    # address
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    address1 = models.CharField(max_length=500, blank=True)
    nearby = models.CharField(max_length=200, blank=True)
    total_amount = models.IntegerField(blank=True, null=True)
    rate = models.CharField(max_length=20, blank=True, null=True) 
    expenses = models.IntegerField(blank=True, null=True)
    registry_date = models.DateField() 
    sai = models.IntegerField(blank=True, null=True)
    size = models.CharField(max_length=10)
    size_unit = models.CharField(max_length=5, choices=SIZE_UNITS)
    payment_condition = models.TextField(max_length=4000, default='', blank=True)

    def __str__(self):
        return self.property_name