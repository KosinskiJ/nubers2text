from django.test import TestCase
from django.urls import reverse


class ConverterIntegrationTest(TestCase):
    def test_post_form(self):
        res = self.client.post(reverse('converter_home'), data={'number': 12}, follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'dwanaście')

    def test_post_empty_form(self):
        res = self.client.post(reverse('converter_home'), data={'number': ''})
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'Podaj liczbę...')
