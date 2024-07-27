from django import forms
from .models import Property


# ModelForm can automatically generate certain fields, depends on the meta class
class PropertyForm(forms.ModelForm):
    # ModelForm expects configurations to be set under the Meta name
    class Meta:
        model = Property # name of the model
        fields = ['property_name', 'buyer_1', 'buyer_2', 'buyer_3', 'buyer_4', 'buyer_5', 'seller', 'dealer_1', 'dealer_2', 'state', 'city', 'address1', 'nearby', 'total_amount', 'rate', 'expenses', 'registry_date', 'sai', 'size', 'marla', 'payment_condition'] # all the fields from the model class that I want in the form
        widgets = {
            'registry_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'size': forms.TextInput(attrs={'placeholder': 'Length x Breadth'})
        }
