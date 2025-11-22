#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
            'D': 500, 'M': 1000
            }
    total = 0
    pval = 0

    for char in reversed(roman_string):
        value = roman_dict[char]
        if value < pval:
            total -= value
        else:
            total += value
        pval = value
    return total
