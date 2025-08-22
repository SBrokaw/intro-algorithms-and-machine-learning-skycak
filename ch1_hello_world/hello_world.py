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

    print(f'sorted              {sorted_intersection}')
    print(f'set intersection    {set_intersection_fancy}')
    print(f'order preserved     {first_appr_intersect}')
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
    limit = num // 2
    print(f'checking {num} to {limit}')
    for i in range(3, limit):
        if num % i == 0: 
            print(f'  Not prime. Divisor {i} found')
            return False
    
    return True


# TODO finish this and test it
def decimal_to_base_b(s, b):
    count = 0
    for i in range(len(s)):
        count += int(s[i]) * b**i

    return str(count)

def base_b_to_decimal(s, b):
    count = 0
    for i in range(len(s)):
        count += int(s[i]) * b**i

    return str(count)


def binary_to_decimal(s):
    if not s.isdecimal(): return '0'

    ones = list(s)
    for i in range(len(s)):
        if s[i] != '0': ones[i] = 1    # convert all numbers to 1s, leave 0s

    return base_b_to_decimal(ones, 2)

def decimal_to_binary(s):
    if not s.isdecimal(): return '0'

    return decimal_to_base_b(s, 2)




print(binary_to_decimal('100000111000101001'))
