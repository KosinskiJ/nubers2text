# -*- coding: utf-8 -*-
from numbers_converter import utils
from numbers_converter.exceptions import TooBigNumberException


class ConverterService:
    @staticmethod
    def number_to_text(number):
        word = ''
        minus = 0

        if type(number) is not int:
            return False

        if number == 0:
            return 'zero'

        if len(str(number)) > 21:
            raise TooBigNumberException()

        if number < 0:
            minus = 1
            number = -number

        list_number = [int(x) for x in str(number)]
        list_number = utils.cut_on_group(list_number)

        for x, y in enumerate(list_number[::-1]):
            word = utils.group_to_str(y) + utils.get_group_name(x, y) + word

        word = 'minus ' + word if minus else word

        return ' '.join(word.split())
