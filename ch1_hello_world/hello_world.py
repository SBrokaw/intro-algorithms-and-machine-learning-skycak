# Introduction to Algorithms and Machine Learning
# by Justin Skycak
# https://www.justinmath.com/some-short-introductory-coding-exercises/

def check_if_symmetric(s):
    original_s = s.lower()
    backward_s = ''
    for i in range(len(s)):
        backward_s += s[len(s)- i - 1]

    print(f'{s} {backward_s}')
    return backward_s == s

def check_if_symmetric2(s):
    original_s = s.lower()
    backward_s = original_s[::-1]

    print(f'{original_s} {backward_s}')
    return backward_s == original_s

def convert_to_numbers(s):
    number_string = []
    for i in range(len(s)):
        print(f'{s[i]} {ord(s[i])}')
        number_string.append(ord(s[i]))

    return number_string

def convert_to_chars(s):
    char_string = ''
    for i in range(len(s)):
        char_string += chr(s[i])

    return char_string


print(check_if_symmetric('firetruck'))
print(check_if_symmetric2('raceCaR'))
print(convert_to_numbers('for once in your life, Donny, pay attention !! 1230983'))
print(convert_to_chars(convert_to_numbers('for once in your life, Donny, pay attention !! 1230983')))