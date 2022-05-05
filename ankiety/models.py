from django.db import models

# from django.forms import SelectMultiple
# from django.views.generic import ListView

class Odpowiedz(models.Model):
    wiek = models.IntegerField()

    # wyksztalcenie = models.IntegerField(choices=[
    #     (1, 'Podstawowe'),
    #     (2, 'Średnie'),
    #     (3, 'Wyższe'),
    # ])
    #
    # geeks_field = models.TextField()

     # gender = forms.ChoiceField(choices=[
    #     (1, 'Lubię'),
    #     (2, 'Średnio')
    # ], widget=forms.RadioSelect)

     # wprowadzanie tekstu

