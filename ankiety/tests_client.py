from http import HTTPStatus

from django.test import TestCase
# from unittest import TestCase
from ankiety.models import Odpowiedz


class SimpleTest(TestCase):
    def test_wyswietlania(self):
        response = self.client.get('/wypelnij/')
        self.assertIn(b'Resetuj', response.content)
        self.assertIn('Resetuj', str(response.content))
        self.assertEqual(len(response.context['form'].fields), 3)
        self.assertEqual(response.status_code, 200)


    def test_zapisu_z_powodzeniem(self):
        self.assertEqual(Odpowiedz.objects.count(), 0)
        response = self.client.post("/wypelnij/", data={
            "wiek": '20',
            'plec': 'k',
            'wyksztalcenie': '3'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/dziekuje/")
        self.assertEqual(Odpowiedz.objects.count(), 1)
        odp = Odpowiedz.objects.first()
        self.assertEqual(odp.wiek, 20)
        self.assertEqual(odp.plec, 'k')
        self.assertEqual(odp.wyksztalcenie, 3)

    def test_zapisu_z_niepowodzeniem(self):
        response = self.client.post("/wypelnij/", data={
            "wiek": 10,
            'plec': 'z'
        })
        self.assertEqual(response.context['form'].errors['wiek'][0],
                         'Ensure this value is greater than or equal to 18.')
        self.assertEqual(response.context['form'].errors['plec'][0],
                         'Select a valid choice. z is not one of the available choices.')

        response = self.client.post("/wypelnij/", data={
            "wiek": 21,
        })
        self.assertEqual(response.context['form'].errors['wiek'][0],
                         'Wiek musi być parzysty')
    # def test_index(self):
    #     response = self.client.get('/customer/index/')
    #
    # def test_post_error(self):
    #     response = self.client.post("/books/add/", data={"title": "Dombey & Son"})
    #
    #     self.assertEqual(response.status_code, HTTPStatus.OK)
    #     self.assertContains(response, "Use 'and' instead of '&'", html=True)
