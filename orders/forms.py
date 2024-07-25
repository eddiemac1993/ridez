from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['restaurant', 'delivery_address']
        widgets = {
            'restaurant': forms.TextInput(attrs={'placeholder': 'Enter restaurant name'}),
            'delivery_address': forms.TextInput(attrs={'placeholder': 'Enter delivery address'}),
        }