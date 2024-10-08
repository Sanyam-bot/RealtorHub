from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Property

class PropertyAdmin(admin.ModelAdmin):
    list_display = ['user', 'property_name', 'total_amount', 'sai']

class AddressAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Property, PropertyAdmin)