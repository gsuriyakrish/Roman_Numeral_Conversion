"""
This program is developed for conversion of Arabic numbers to Roman Numerals.
DATE : 25-02-2021
DEVELOPER : SURIYA KRISHNAN
"""
"""
   Subtractive Notation method is useful for converting Arabic numbers into corresponding Roman Numerals
   1. Range of Roman Numerals from 1 to 3999
   2. There is no negative Roman Numerals and there is no roman numeral for Zero
   3. The Roman numerals never repeat a symbol more than three times
"""

import random

# Global Variables
# Tuples are immutable, so using it in the indirect mapping of arabic_numerals
# Arabic_Roman Mappings are initialized only for certain subtracting pairs (IV,IX,XL,XC,CD,CM)
# Rest all are addition anyway but to make the code easier we are initializing certain other values

MAX_ROMAN = 3999
ARABIC_NUMERALS = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
ROMAN_NUMERALS = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")


# Function to convert the arabic number to RomanNumerals
def subtractive_notation(value):
    i = 0
    list_output = []
    # Validating the input
    output_validator = input_validator(value)
    if not output_validator[1]:
        return output_validator[0]
    else:
        arabic_number = output_validator[0]
    # Roman Conversion Logic
    while arabic_number > 0:
        if arabic_number - ARABIC_NUMERALS[i] >= 0:
            list_output.append(ROMAN_NUMERALS[i])
            arabic_number -= ARABIC_NUMERALS[i]
        else:
            i += 1
    output_value = "The arabic number {} equivalent value in Roman Numeral is {}".format(value,
                                                                                         "".join(list_output))
    return output_value


# Function to validate the input values before starting Roman Numeral conversion
def input_validator(input_number):
    if str(input_number).isalpha() or not str(input_number).isdecimal() \
            or int(input_number) <= 0 or int(input_number) > MAX_ROMAN:
        output = "Wrong Input Value. Please check the below criteria for the input" + '\n' + \
                 "1. Input value must be an Integer without float and should start with 1" + '\n' + \
                 "2. Input value should not be characters" + '\n' + \
                 "3. There is no Roman Numerals for zero" + '\n' + \
                 "4. Input value should be less than {}".format(MAX_ROMAN)
        return output, False
    else:
        output = int(input_number)
        return output, True


# Pilot for the program which guides
def master_driver(n):
    if not n:
        n = random.randint(1, MAX_ROMAN)
    return subtractive_notation(n)
