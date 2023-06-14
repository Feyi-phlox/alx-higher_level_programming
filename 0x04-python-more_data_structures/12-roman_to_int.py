#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    result = 0
    n = len(roman_string)

    for i in range(n):
        current_value = roman_values.get(roman_string[i], 0)
        next_value = roman_values.get(roman_string[i + 1], 0)

        if current_value < next_value:
            result -= current_value
        else:
            result += current_value

    return result
