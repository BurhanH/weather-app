from .models import City
from django.forms import ModelForm, TextInput


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name', 'country']
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'name': 'city',
                    'id': 'city',
                    'placeholder': 'Enter City'
                }
            ),
            'country': TextInput(
                attrs={
                    'class': 'form-control',
                    'name': 'country',
                    'id': 'country',
                    'placeholder': 'Enter Country. Use ISO 3166 country codes'
                }
            )

        }
