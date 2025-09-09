# Introduction to Algorithms and Machine Learning
# by Justin Skycak
# https://www.justinmath.com/some-short-introductory-coding-exercises/
import pdb

def check_if_symmetric2(s):
    original_s = s.lower()
    backward_s = ''
    for i in range(len(s)):
        backward_s += s[len(s)- i - 1]

    return backward_s == s

def check_if_symmetric(s):
    original_s = s.lower()
    backward_s = original_s[::-1]

    return backward_s == original_s

def convert_to_numbers(s):
    number_string = []
    for i in range(len(s)):
        #print(f'{s[i]} {ord(s[i])}')
        number_string.append(ord(s[i]))

    return number_string

def convert_to_chars(s):
    char_string = ''
    for i in range(len(s)):
        char_string += chr(s[i])

    return char_string

def get_intersection(s1, s2): 
    match = 0
    set1 = frozenset(s1)
    set2 = frozenset(s2)
    set_intersection = set()
    intersection = []
    first_appr_intersect = []
    unique = set()

    # set comprehension method https://docs.python.org/3/library/stdtypes.html#set
    set_intersection_fancy = {c for c in s1 if c in s2}

    # set method with order of first appearance maintained
    for c in s1:
        if c in set2 and c not in unique:
            first_appr_intersect.append(c)
            unique.add(c)

    # set method O(n) https://docs.python.org/3/library/stdtypes.html#set
    for c in set1:
        if c in set2:
            set_intersection.add(c)
    
    # array method O(n^2) for s1, s2 with length n
    for i in range(len(s1)):
        match = 0
        for k in range(len(s2)):
            if s1[i] == s2[k]: match |= 1 

        if len(intersection) > 0: 
            for n in range(len(intersection)):
                if s1[i] == intersection[n]: match = 0 
        
        if match == 1: 
            intersection.append(s1[i])

    # sort set
    sorted_intersection = sorted(list(set_intersection_fancy))

    return intersection


def get_union(s1, s2):
    return set(s1 + s2)

def count_characters(s):
    ordered_unique = []
    unique = set()
    char_w_cnt = dict()
    set1 = frozenset(s)

    # set method with order of first appearance maintained
    for c in s:
        if c not in unique:
            ordered_unique.append(c) 
            unique.add(c)
            char_w_cnt[c] = 1
        else:
            char_w_cnt[c] += 1

    return char_w_cnt

def is_prime(n):
    if not n.isdecimal(): return False

    num = int(n)
    if num < 2: return False
    limit = num // 2    # // is floor division (returns int)
    for i in range(3, limit):
        if num % i == 0: 
            return False
    
    return True


def decimal_to_base_b(s, b):
    remaining = int(s)
    count = []
    exponent = 1
    # find largest exponent
    while( b**exponent < remaining ): exponent += 1

    # go from largest exponent of b to 1
    counter = range(exponent)[::-1]
    for i in counter:
        val = remaining // b**(int(i))
        # convert to characters for numbers > 9
        if int(val) > 9:
            if val == 10: val = 'A'
            elif val == 11: val = 'B'
            elif val == 12: val = 'C'
            elif val == 13: val = 'D'
            elif val == 14: val = 'E'
            elif val == 15: val = 'F'
            elif val == 16: val = 'G'
            elif val == 17: val = 'H'
            elif val == 18: val = 'I'
            elif val == 19: val = 'J'
            elif val == 20: val = 'K'
            elif val == 21: val = 'L'
            elif val == 22: val = 'M'
            elif val == 23: val = 'N'
            elif val == 24: val = 'O'
            elif val == 25: val = 'P'
            elif val == 26: val = 'Q'
            elif val == 27: val = 'R'
            elif val == 28: val = 'S'
            elif val == 29: val = 'T'
            elif val == 30: val = 'U'
            elif val == 31: val = 'V'
            elif val == 32: val = 'W'
            elif val == 33: val = 'X'
            elif val == 34: val = 'Y'
            elif val == 35: val = 'Z'

        count.append(str(val))
        remaining %= b**int(i)

    return ''.join(count)

def base_b_to_decimal(s, b):
    count = 0
    num = 0
    s_little_endian = s[::-1] # flip input s so we iterate through little-endian

    # handles bases 11 to 34 (mostly only hex will be used but I wanted to support base-12 as well)
    for i in range(len(s_little_endian)):
        if( b > 10 ):
            if s_little_endian[i].isdecimal(): num = int(s_little_endian[i])
            elif s_little_endian[i].lower() == 'a': num = 10 if 10 < b else 0
            elif s_little_endian[i].lower() == 'b': num = 11 if 11 < b else 0
            elif s_little_endian[i].lower() == 'c': num = 12 if 12 < b else 0
            elif s_little_endian[i].lower() == 'd': num = 13 if 13 < b else 0
            elif s_little_endian[i].lower() == 'e': num = 14 if 14 < b else 0
            elif s_little_endian[i].lower() == 'f': num = 15 if 15 < b else 0
            elif s_little_endian[i].lower() == 'g': num = 16 if 16 < b else 0
            elif s_little_endian[i].lower() == 'h': num = 17 if 17 < b else 0
            elif s_little_endian[i].lower() == 'i': num = 18 if 18 < b else 0
            elif s_little_endian[i].lower() == 'j': num = 19 if 19 < b else 0
            elif s_little_endian[i].lower() == 'k': num = 20 if 20 < b else 0
            elif s_little_endian[i].lower() == 'l': num = 21 if 21 < b else 0
            elif s_little_endian[i].lower() == 'm': num = 22 if 22 < b else 0
            elif s_little_endian[i].lower() == 'n': num = 23 if 23 < b else 0
            elif s_little_endian[i].lower() == 'o': num = 24 if 24 < b else 0
            elif s_little_endian[i].lower() == 'p': num = 25 if 25 < b else 0
            elif s_little_endian[i].lower() == 'q': num = 26 if 26 < b else 0
            elif s_little_endian[i].lower() == 'r': num = 27 if 27 < b else 0
            elif s_little_endian[i].lower() == 's': num = 28 if 28 < b else 0
            elif s_little_endian[i].lower() == 't': num = 29 if 29 < b else 0
            elif s_little_endian[i].lower() == 'u': num = 30 if 30 < b else 0
            elif s_little_endian[i].lower() == 'v': num = 31 if 31 < b else 0
            elif s_little_endian[i].lower() == 'w': num = 32 if 32 < b else 0
            elif s_little_endian[i].lower() == 'x': num = 33 if 33 < b else 0
            elif s_little_endian[i].lower() == 'y': num = 34 if 34 < b else 0
            elif s_little_endian[i].lower() == 'z': num = 35 if 35 < b else 0
            else: num = 0
        else: num = int(s_little_endian[i]) if int(s_little_endian[i]) < b else b-1
        count += num * b**(i)

    return str(count)


def binary_to_decimal(s):
    if not s.isdecimal(): return '0'

    ones = list(s)
    for i in range(len(s)):
        if s[i] != '0': ones[i] = '1'    # convert all numbers to 1s, leave 0s

    return base_b_to_decimal(ones, 2)

def hexadecimal_to_decimal(s):
    return base_b_to_decimal(s, 16)

def decimal_to_binary(s):
    if not s.isdecimal(): return '0'

    return decimal_to_base_b(s, 2)


def decimal_to_hexadecimal(s):
    if not s.isdecimal(): return '0'

    return decimal_to_base_b(s, 16)

def binary_to_hexadecimal(s):
    decimal = 0
    if not s.isdecimal(): return '0'

    ones = list(s)
    for i in range(len(s)):
        if s[i] != '0': ones[i] = '1'    # convert all numbers to 1s, leave 0s

    decimal = base_b_to_decimal(ones, 2)

    return decimal_to_hexadecimal(decimal)

def hexadecimal_to_binary(s):
    decimal = hexadecimal_to_decimal(s)

    return decimal_to_binary(decimal)