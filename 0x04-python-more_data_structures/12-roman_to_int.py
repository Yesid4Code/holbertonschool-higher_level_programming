#!/usr/bin/python3
def roman_to_int(roman):
    summ = 0
    if roman and type(roman) is str:
        rom = {'I': 1, 'V': 5, 'X': 10,
               'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # idx = 0
        for idx, value in enumerate(roman):
            if idx < len(roman) - 1 and rom[roman[idx]] < rom[roman[idx+1]]:
                summ -= rom[roman[idx]]
            else:
                summ = summ + rom[roman[idx]]
        return summ
    return 0

# Flourish
# def roman_to_int(roman_string):
#    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#    result = 0
#    item = 0
#    roman = roman_string
#    if type(roman) is not str or len(roman) is 0:
#        return 0
#    for item in range(item, len(roman)):
#        if item < len(roman) - 1 and dic[roman[item]] < dic[roman[item + 1]]:
#            result -= dic[roman[item]]
#        else:
#            result += dic[roman[item]]
#    return result

# def roman_to_int(roman_string):
# numbers = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
#
# if not isinstance(roman_string, str) or roman_string is None:
#        return 0
#    pre, sum = 0, 0
#
#    for i in roman_string:
#        sum += numbers[i] if numbers[i] <= pre else numbers[i] - pre * 2
#        pre = numbers[i]
#    return sum
