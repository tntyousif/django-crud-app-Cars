from django import forms
from .models import Filling

class FillingForm(forms.ModelForm):
    class Meta:
        model = Filling
        fields = ['date', 'gas']
        widgets = {
            'date': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }