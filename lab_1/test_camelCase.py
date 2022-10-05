import camelCase
from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        self.assertEqual('helloWorld', camelCase.camel_case('Hello World'))
        self.assertEqual('', camelCase.camel_case(''))
        self.assertEqual('helloWorld', camelCase.camel_case('    Hello     World     '))