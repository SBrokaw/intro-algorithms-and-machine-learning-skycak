# Skycak, J. (2021). Roulette Wheel Selection. 
# In Introduction to Algorithms and Machine Learning: 
# from Sorting to Strategic Agents. 
# https://justinmath.com/roulette-wheel-selection/

import random

def pdf_to_cdf(f):
    cdf = []
    sum = sum_pdf(f)
    if sum < 0.99 or sum > 1.01:
        return -1
    for i in range(len(f)):
        cdf[i] = sum_pdf(f[:i+1])
    return cdf

def sum_pdf(f):
    if not f: return 0 
    if not isinstance(f, (list, tuple, range)): return 0

    return sum_pdf_loop(f)

def sum_pdf_loop(f):
    if not f: return 0 # base case return 0 when f is empty
    sum = f[0] + sum_pdf_loop(f[1:])
    return sum
