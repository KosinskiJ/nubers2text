from django import forms
from django.core.exceptions import ValidationError


class ConverterForm(forms.Form):
    number = forms.IntegerField(label='Liczba', required=False)

    def clean_number(self):
        number = self.cleaned_data['number']

        if not number:
            raise ValidationError('Podaj liczbę...')

        if isinstance(number, int):
            return number
        else:
            raise ValidationError('Podany ciąg znaków musi być liczbą całkowitą.')
