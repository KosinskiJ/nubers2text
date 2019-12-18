from django.core.exceptions import ValidationError
from django.test import TestCase

from numbers_converter.forms import ConverterForm


class ConverterFormTest(TestCase):

    def test_form_valid(self):
        form = ConverterForm({
            'number': 1,
        })

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['number'], 1)

    def test_form_not_valid_characters_typed(self):
        form = ConverterForm({
            'number': 'aa1',
        })

        self.assertFalse(form.is_valid())
        self.assertRaises(ValidationError)

    def test_form_not_valid_no_data_typed(self):
        form = ConverterForm({
            'number': '',
        })

        self.assertFalse(form.is_valid())
        self.assertRaises(ValidationError)
