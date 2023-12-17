from django import forms
from .models import Booking,Hotel, Packages

from django.forms.widgets import DateInput
from django.utils import timezone

class DateInput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    hotel = forms.ModelChoiceField(queryset=Hotel.objects.all(), empty_label="-- Select a Hotel --")
    package = forms.ModelChoiceField(queryset=Packages.objects.all(), empty_label="-- Select a Package --")
    class Meta:
        model=Booking
        fields = '__all__'
      
        widgets = {
            'checkin': DateInput(attrs={'type': 'date', 'min': timezone.now().date().isoformat()}),
            'checkout': DateInput(attrs={'type': 'date', 'min': timezone.now().date().isoformat()}),
        }
        
        labels={
            'firstname':"First Name",
            'lastname':"Last Name",
            'phonenumber':"Phone Number",
            'email':"Email",
            'checkin':"Check-in",
            'checkout':"Check-out",
            'guests':"No. of Guests",
            'room_type':"Room Type",
        }

class CancelBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['canceled']
        
        





