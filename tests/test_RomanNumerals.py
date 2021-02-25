"""
This module is for testing the
Roman Numeral conversion from Arabic Number
"""

import unittest
from RomanNumerals import input_validator, subtractive_notation, master_driver

MAX_ROMAN = 3999
ERROR = "Wrong Input Value. Please check the below criteria for the input" + '\n' + \
                 "1. Input value must be an Integer without float and should start with 1" + '\n' + \
                 "2. Input value should not be characters" + '\n' + \
                 "3. There is no Roman Numerals for zero" + '\n' + \
                 "4. Input value should be less than {}".format(MAX_ROMAN)


class TestConversions(unittest.TestCase):

    def test_invalid_character_input_validator(self):
        """Test the invalid characters input data and then getting an error."""
        response = input_validator(input_number='s')
        self.assertEqual(ERROR, response[0])
        self.assertEqual(False, response[1])

    def test_invalid_negative_input_validator(self):
        """Test the invalid negative input data and then getting an error."""
        response = input_validator(input_number=-1)
        self.assertEqual(ERROR, response[0])
        self.assertEqual(False, response[1])

    def test_invalid_zero_input_validator(self):
        """Test the invalid zero input data and then getting an error."""
        response = input_validator(input_number=0)
        self.assertEqual(ERROR, response[0])
        self.assertEqual(False, response[1])

    def test_invalid_decimal_input_validator(self):
        """Test the invalid decimal input data and then getting an error."""
        response = input_validator(input_number=6.0)
        self.assertEqual(ERROR, response[0])
        self.assertEqual(False, response[1])

    def test_invalid_maximum_input_validator(self):
        """Test the invalid maximum input data and then getting an error."""
        response = input_validator(input_number=6000)
        self.assertEqual(ERROR, response[0])
        self.assertEqual(False, response[1])

    def test_valid_maximum_input_validator(self):
        """Test the valid maximum input data and then getting True."""
        response = input_validator(input_number=3999)
        self.assertEqual(3999, response[0])
        self.assertEqual(True, response[1])

    def test_subtractive_notation_1(self):
        """Test with the valid input data and then getting a valid output."""
        response = subtractive_notation(value=1)
        expected_output = "The arabic number 1 equivalent value in Roman Numeral is I"
        self.assertEqual(expected_output, response)

    def test_subtractive_notation_10(self):
        """Test with the valid input data and then getting a valid output."""
        response = subtractive_notation(value=10)
        expected_output = "The arabic number 10 equivalent value in Roman Numeral is X"
        self.assertEqual(expected_output, response)

    def test_subtractive_notation_666(self):
        """Test with the valid input data and then getting a valid output."""
        response = subtractive_notation(value=666)
        expected_output = "The arabic number 666 equivalent value in Roman Numeral is DCLXVI"
        self.assertEqual(expected_output, response)

    def test_subtractive_notation_666(self):
        """Test with the valid input data and then getting a valid output."""
        response = subtractive_notation(value=666)
        expected_output = "The arabic number 666 equivalent value in Roman Numeral is DCLXVI"
        self.assertEqual(expected_output, response)

    def test_subtractive_notation_2000(self):
        """Test with the valid input data and then getting a valid output."""
        response = subtractive_notation(value=2000)
        expected_output = "The arabic number 2000 equivalent value in Roman Numeral is MM"
        self.assertEqual(expected_output, response)

    def test_subtractive_notation_3999(self):
        """Test with the valid input data and then getting a valid output."""
        response = subtractive_notation(value=3999)
        expected_output = "The arabic number 3999 equivalent value in Roman Numeral is MMMCMXCIX"
        self.assertEqual(expected_output, response)

    def test_master_driver_skipped_input_value(self):
        """Test with the skipped input data and then getting a valid output."""
        response = master_driver(n='')
        self.assertTrue(response != '')
