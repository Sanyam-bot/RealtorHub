from django.contrib.auth.models import AbstractUser
from django.db import models


ROLES = (
    ('buyer', 'BUYER'),
    ('seller', 'SELLER'),
    ('dealer', 'DEALER'),
)


# Create your models here.
class User(AbstractUser):
    pass


class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_property')
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=6, choices=ROLES)
    # adrress
    price = models.IntegerField()
    sai = models.IntegerField()

    def __str__(self):
        return self.name