#!/usr/bin/python3
def roman_to_int(roman_string):
    add = 0
    if type(roman_string) is not str or len(roman_string) == 0:
        return (0)
    else:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(0, len(roman_string)):
            if i < len(roman_string) - 1 and
            dic[roman_string[i]] <
            dic[roman_string[i + 1]]:
                add -= dic[roman_string[i]]
            else:
                add += dic[roman_string[i]]
    return (add)
