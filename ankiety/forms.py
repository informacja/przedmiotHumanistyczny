from django import forms
from django.core.exceptions import ValidationError
from django.forms import models
from django.db.models import Model
from ankiety.models import Odpowiedz

class Formularz0(models.ModelForm):  # Przykładowy formularz
    wiek = forms.IntegerField(min_value=18)
    #
    # COLORS = (
    #     ('R', 'Red'),
    #     ('B', 'Yellow'),
    #     ('G', 'White'),
    # )
    # color = forms.MultipleChoiceField(choices=COLORS)
    Jakie_jest_twoje_zaufanie_do_szczepien = forms.ChoiceField(choices=[
        ('R',"lubię"),
        ('2',"Nie ufam"),
    ], widget=forms.RadioSelect)

    # geeks_field = models.TextField()

    Ile_masz_lat = forms.IntegerField(min_value=18)
    COLORS = (
        ('R', 'Red'),
        ('B', 'Yellow'),
        ('G', 'White'),
    )
    color = forms.MultipleChoiceField(choices=COLORS)

    # Jakie_jest_toje_zaufanie_do_szczepień = forms.RadioSelect([
    CHOICES = [
        ('R',"lubię"),
        ('2',"Nie ufam"),
    ]

    Jakie_jest_twoje_zaufanie_do_szczepien = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    # Jakie_jest_twoje_zaufanie_do_szczepień = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Odpowiedz
        fields = '__all__'

    def clean_wiek(self):
        wiek = self.cleaned_data.get('wiek', 0)
        if wiek % 2:
            raise ValidationError('Wiek musi być parzysty')
        return wiek

    def clean_color(self):
        color = self.cleaned_data['color']
        if not color:
            raise forms.ValidationError("...")

        if len(color) > 2:
            raise forms.ValidationError("...")

        color = ''.join(color)
        return color

class Formularz1(models.ModelForm):
    wiek = forms.IntegerField(min_value=18)


    class Meta:
        model = Odpowiedz
        fields = '__all__'

    def clean_wiek(self):
        wiek = self.cleaned_data.get('wiek', 0)
        if wiek % 2:
            raise ValidationError('Wiek musi być parzysty')
        return wiek

    def clean_color(self):
        color = self.cleaned_data['color']
        if not color:
            raise forms.ValidationError("...")

        if len(color) > 2:
            raise forms.ValidationError("...")

        color = ''.join(color)
        return color

class Formularz2(models.ModelForm):

    class Meta:
        model = Odpowiedz
        fields = '__all__'


class Formularz3(models.ModelForm):
    class Meta:
        model = Odpowiedz
        fields = '__all__'


class Formularz4(models.ModelForm):
    class Meta:
        model = Odpowiedz
        fields = '__all__'


class Formularz5(models.ModelForm):
    class Meta:
        model = Odpowiedz
        fields = '__all__'




