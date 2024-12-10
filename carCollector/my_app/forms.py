from django import forms
from .models import Filling

class FillingForm(forms.ModelForm):
    class Meta:
        model = Filling
        fields = ['date', 'gas']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }