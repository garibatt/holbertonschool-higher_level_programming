#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    for index, char in enumerate(roman_string):
        if index == len(roman_string) - 1:
            total += roman.get(char, 0)
        elif roman[char] < roman[roman_string[index + 1]]:
            total -= roman[char]
        else:
            total += roman[char]

    return total
