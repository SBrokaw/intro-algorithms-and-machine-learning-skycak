# Introduction to Algorithms and Machine Learning
# by Justin Skycak
# https://www.justinmath.com/some-short-introductory-coding-exercises/
import pdb

# Starting with 5, generate each term by multiplying the previous term by 3 and subtracting 4.
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

# Starting with 25, generate each term by taking half of the previous term if it's even, 
# or multiplying by 3 and adding 1 if it's odd. (This is an instance of a Collatz sequence.)
def problem2_array(terms):
    if not terms.isdecimal(): return 0
    n = int(terms)
    if n < 1: return 0

    sequence = [25]

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

# Starting with 0,1, generate each term by adding the previous two terms. (This is the famous Fibonacci sequence.)
def problem3_array(terms):
    if not str(terms).isdecimal(): return 0
    n = int(terms)
    if n < 2: return 0

    sequence = [0, 1]

    if n == 2: return sequence

    for i in range(2, n):
        sequence.append(sequence[i-2] + sequence[i-1])

    return sequence

def problem3_recursion(terms):
    if not str(terms).isdecimal(): return 0
    n = int(terms)
    if n < 0: return 0

    return problem3_recursion_loop(n, [0, 1])

def problem3_recursion_loop(n, terms):
    if n == 1:
        return terms[0]
    elif n == 2:
        return terms[1] 

    return problem3_recursion_loop(n-1, [terms[1], terms[0] + terms[1]])

# Starting with 2,−3, generate each term by adding the product of the previous two terms.
def problem4_array(terms):
    if not str(terms).isdecimal(): return 0
    n = int(terms)
    if n < 2: return 0

    sequence = [2, -3]

    if n == 2: return sequence

    for i in range(2, n):
        sequence.append(sequence[i-2] * sequence[i-1])

    return sequence

def problem4_recursion(terms):
    if not str(terms).isdecimal(): return 0
    n = int(terms)
    if n < 0: return 0

    return problem4_recursion_loop(n, [2, -3])

def problem4_recursion_loop(n, terms):
    if n == 1:
        return terms[0]
    elif n == 2:
        return terms[1] 

    return problem4_recursion_loop(n-1, [terms[1], terms[0] * terms[1]])