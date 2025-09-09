# Introduction to Algorithms and Machine Learning
# by Justin Skycak
# https://www.justinmath.com/some-short-introductory-coding-exercises/
import pdb

def problem1_array(terms):
    if not terms.isdecimal(): return 0
    n = int(terms)
    if n < 1: return 0

    sequence = [5]
    counter = 1

    if n == 1: return sequence

    for i in range(1, n):
        sequence.append(sequence[i-1] * 3 - 4)

    return sequence

def problem1_recursion(terms):
    if not terms.isdecimal(): return 0
    n = int(terms)
    if n < 1: return 0

    return problem1_recursion_loop(n)

def problem1_recursion_loop(n):
    if n == 1: 
        return 5
    else:
        prev_term = problem1_recursion_loop(n-1)
        return prev_term * 3 - 4

def problem2_array(terms):
    if not terms.isdecimal(): return 0
    n = int(terms)
    if n < 1: return 0

    sequence = [25]
    counter = 1

    if n == 1: return sequence

    for i in range(1, n):
        if sequence[i-1] % 2:
            sequence.append(int(sequence[i-1] * 3 - 1))
        else:
            sequence.append(int(sequence[i-1] / 2))

    return sequence

def problem2_recursion(terms):
    if not terms.isdecimal(): return 0
    n = int(terms)
    if n < 1: return 0

    return problem2_recursion_loop(n)

def problem2_recursion_loop(n):
    if n == 1:
        return 25

    prev_term = problem2_recursion_loop(n-1)
    if prev_term % 2: #odd
        return prev_term * 3 - 1
    else: #even
        return int(prev_term / 2)



