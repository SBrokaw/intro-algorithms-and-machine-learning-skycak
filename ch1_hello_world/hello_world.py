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
    num = int(n)
    print(f'is_prime({num})'')
    for i in range(floor(num/2)):
        return True if num % i == 0
    
    return false




print('\n' + " Problem 1 - check_if_symmetric(string)".center(50, '-'))
print(check_if_symmetric('firetruck'))

print('\n' + " Problem 2 - convert_to_numbers(string)".center(50, '-'))
print(check_if_symmetric2('raceCaR'))

print('\n' + " Problem 3 - convert_to_letters(array)".center(50, '-'))
print(convert_to_numbers('for once in your life, Donny, pay attention !! 1230983'))

print('\n' + " Problem 4 - get_intersection(array1, array2)".center(50, '-'))
print(convert_to_chars(convert_to_numbers('for once in your life, Donny, pay attention !! 1230983')))

print('\n' + " Problem 5 - get_union(array1, array2)".center(50, '-'))
print(get_intersection('aabbccddefghijkzxyw', 'zxybbbbbbcccdefghijklmnopzxwynbw'))

print('\n' + " Problem 6  count_characters(string)".center(50, '-'))
print(count_characters('aabbccddefghijkzxyw'))

print('\n' + " Problem 7  is_prime(n)".center(50, '-'))
print(is_prime(109733))
