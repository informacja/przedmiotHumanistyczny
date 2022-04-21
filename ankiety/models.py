from django.db import models

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
