from django import forms
from django.core.exceptions import ValidationError
from django.forms import models

from ankiety.models import Odpowiedz

class Formularz(models.ModelForm):
    wiek = forms.IntegerField(min_value=18)
    # plec = forms.ChoiceField(choices=[
    #     ('k', 'Kobieta'),
    #     ('m', 'Mężczyzna'),
    #     ('i', 'Inne'),
    # ])
    #
    # wyksztalcenie = forms.ChoiceField(choices=[
    #     (1, 'Podstawowe'),
    #     (2, 'Średnie'),
    #     (3, 'Wyższe'),
    # ])

    class Meta:
        model = Odpowiedz
        fields = '__all__'

    def clean_wiek(self):
        wiek = self.cleaned_data.get('wiek', 0)
        if wiek % 2:
            raise ValidationError('Wiek musi być parzysty')
        return wiek