from django import forms
from .models import Ride

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['pickup_location', 'dropoff_location']
        widgets = {
            'pickup_location': forms.TextInput(attrs={'placeholder': 'Enter pickup location'}),
            'dropoff_location': forms.TextInput(attrs={'placeholder': 'Enter dropoff location'}),
        }