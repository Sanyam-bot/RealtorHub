from django import forms
from .models import Property, ROLES, SIZE_UNITS


# ModelForm can automatically generate certain fields, depends on the meta class
class PropertyForm(forms.ModelForm):
    # ModelForm expects configurations to be set under the Meta name
    class Meta:
        model = Property # name of the model
        fields = ['property_name', 'role', 'state', 'city', 'address1', 'address2', 'nearby', 'total_amount', 'rate', 'advance_payment', 'payment_condition', 'expenses', 'sai', 'size', 'size_unit'] # all the fields from the model class that I want in the form