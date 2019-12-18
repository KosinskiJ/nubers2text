from django.test import TestCase

from numbers_converter.exceptions import TooBigNumberException
from numbers_converter.services import ConverterService


class ConverterServiceTest(TestCase):

    def test_converter_return_zero(self):
        converted_text = ConverterService.number_to_text(0)
        self.assertEqual(converted_text, 'zero')

    def test_converter_units_or_teens(self):
        converted_text1 = ConverterService.number_to_text(1)
        converted_text2 = ConverterService.number_to_text(2)
        converted_text3 = ConverterService.number_to_text(3)
        converted_text4 = ConverterService.number_to_text(4)
        converted_text5 = ConverterService.number_to_text(5)
        converted_text6 = ConverterService.number_to_text(6)
        converted_text7 = ConverterService.number_to_text(7)
        converted_text8 = ConverterService.number_to_text(8)
        converted_text9 = ConverterService.number_to_text(9)
        converted_text11 = ConverterService.number_to_text(11)
        converted_text12 = ConverterService.number_to_text(12)
        converted_text13 = ConverterService.number_to_text(13)
        converted_text14 = ConverterService.number_to_text(14)
        converted_text15 = ConverterService.number_to_text(15)
        converted_text16 = ConverterService.number_to_text(16)
        converted_text17 = ConverterService.number_to_text(17)
        converted_text18 = ConverterService.number_to_text(18)
        converted_text19 = ConverterService.number_to_text(19)

        self.assertEqual(converted_text1, 'jeden')
        self.assertEqual(converted_text2, 'dwa')
        self.assertEqual(converted_text3, 'trzy')
        self.assertEqual(converted_text4, 'cztery')
        self.assertEqual(converted_text5, 'pięć')
        self.assertEqual(converted_text6, 'sześć')
        self.assertEqual(converted_text7, 'siedem')
        self.assertEqual(converted_text8, 'osiem')
        self.assertEqual(converted_text9, 'dziewięć')
        self.assertEqual(converted_text11, 'jedenaście')
        self.assertEqual(converted_text12, 'dwanaście')
        self.assertEqual(converted_text13, 'trzynaście')
        self.assertEqual(converted_text14, 'czternaście')
        self.assertEqual(converted_text15, 'piętnaście')
        self.assertEqual(converted_text16, 'szesnaście')
        self.assertEqual(converted_text17, 'siedemnaście')
        self.assertEqual(converted_text18, 'osiemnaście')
        self.assertEqual(converted_text19, 'dziewiętnaście')

    def test_convert_two_digit_number(self):
        converted_text1 = ConverterService.number_to_text(48)
        converted_text2 = ConverterService.number_to_text(93)

        self.assertEqual(converted_text1, 'czterdzieści osiem')
        self.assertEqual(converted_text2, 'dziewięćdziesiąt trzy')

    def test_convert_three_digit_number(self):
        converted_text1 = ConverterService.number_to_text(148)
        converted_text2 = ConverterService.number_to_text(993)

        self.assertEqual(converted_text1, 'sto czterdzieści osiem')
        self.assertEqual(converted_text2, 'dziewięćset dziewięćdziesiąt trzy')

    def test_convert_four_digit_number(self):
        converted_text1 = ConverterService.number_to_text(1000)
        converted_text2 = ConverterService.number_to_text(2361)

        self.assertEqual(converted_text1, 'jeden tysiąc')
        self.assertEqual(converted_text2, 'dwa tysiące trzysta sześćdziesiąt jeden')

    def test_convert_five_digit_number(self):
        converted_text1 = ConverterService.number_to_text(11111)
        self.assertEqual(converted_text1, 'jedenaście tysięcy sto jedenaście')

    def test_convert_six_and_more_digit_number(self):
        converted_text1 = ConverterService.number_to_text(222211)
        converted_text2 = ConverterService.number_to_text(13333111321)
        converted_text3 = ConverterService.number_to_text(111111111111111111111)

        self.assertEqual(converted_text1, 'dwieście dwadzieścia dwa tysiące dwieście jedenaście')
        self.assertEqual(converted_text2,
                         'trzynaście miliardów trzysta trzydzieści trzy miliony sto jedenaście tysięcy trzysta dwadzieścia jeden')
        self.assertEqual(converted_text3,
                         'sto jedenaście trylionów sto jedenaście biliarów sto jedenaście bilionów sto jedenaście miliardów sto jedenaście milionów sto jedenaście tysięcy sto jedenaście')

    def test_number_too_big_exception(self):
        with self.assertRaises(TooBigNumberException):
            converted_text1 = ConverterService.number_to_text(2123454353453453454351)

    def test_convert_minus_numbers(self):
        converted_text1 = ConverterService.number_to_text(-1)
        converted_text2 = ConverterService.number_to_text(-12)
        converted_text3 = ConverterService.number_to_text(-34)
        converted_text4 = ConverterService.number_to_text(-431)
        converted_text5 = ConverterService.number_to_text(-4131)
        converted_text6 = ConverterService.number_to_text(-4165656)

        self.assertEqual(converted_text1, 'minus jeden')
        self.assertEqual(converted_text2, 'minus dwanaście')
        self.assertEqual(converted_text3, 'minus trzydzieści cztery')
        self.assertEqual(converted_text4, 'minus czterysta trzydzieści jeden')
        self.assertEqual(converted_text5, 'minus cztery tysiące sto trzydzieści jeden')
        self.assertEqual(converted_text6, 'minus cztery miliony sto sześćdziesiąt pięć '
                                          'tysięcy sześćset pięćdziesiąt sześć')
