# Skycak, J. (2021). Simulating Coin Flips. In Introduction to Algorithms 
# and Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/simulating-coin-flips/

import random

def sim_probability(heads, flips):
    if not str(flips).isdecimal(): return 0
    flips = int(flips)
    if flips < 1: return 0

    successes = 0

    for i in range(flips):
        if random.random() < 0.5: successes += 1
    
    return successes == heads