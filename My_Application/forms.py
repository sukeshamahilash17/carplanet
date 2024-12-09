from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'car_type', 'pick_up_location', 'drop_off_location', 'pick_up_date', 'drop_off_date']
