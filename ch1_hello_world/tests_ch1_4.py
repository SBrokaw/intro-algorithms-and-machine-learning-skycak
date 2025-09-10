# Skycak, J. (2021). Simulating Coin Flips. In Introduction to Algorithms 
# and Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/simulating-coin-flips/

import random
from ch1_4_coinflips import *

tests = [
    {
        'function': sim_probability
        'iterations': 1000
        'input': [3, 4]
        'output': 0
    }
]

trials = 1000

for test in tests:
    function = test['function']
    iterations = test['iterations']
    trial = test['input']
    goal = test['output']
    successes = 0

    for i in range(int(iterations)):
        if isinstance(trial, (list, tuple)):
            successes += bool(function(*trial)) 
        else:
            successes += bool(function(trial)) 

    print(f'{successes / int(iterations)} = {function}({*trial}) over {iterations} trials')


