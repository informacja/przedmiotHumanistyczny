from django.db import models

from django.forms import SelectMultiple

class Odpowiedz(models.Model):
    wiek = models.IntegerField()
    plec = models.CharField(max_length=1, choices=[
        ('k', 'Kobieta'),
        ('m', 'Mężczyzna'),
        ('i', 'Inne'),
    ])
    wyksztalcenie = models.IntegerField(choices=[
        (1, 'Podstawowe'),
        (2, 'Średnie'),
        (3, 'Wyższe'),
    ])
    Czy_lubisz_szczepienia = models.IntegerField(choices=[
        (1, 'Lubię'),
        (2, 'Średnio'),
        (3, 'Nie ufam'),
    ])

    # gender = forms.ChoiceField(choices=[
    #     (1, 'Lubię'),
    #     (2, 'Średnio')
    # ], widget=forms.RadioSelect)

     # wprowadzanie tekstu
#     multiselect
