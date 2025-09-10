# Skycak, J. (2021). Simulating Coin Flips. In Introduction to Algorithms 
# and Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/simulating-coin-flips/

import random
from ch1_4_coinflips import *

tests = [
    [
    {
        'function': sim_probability,
        'iterations': 1000,
        'input': [0, 4],
        'output': 0
    },
    {
        'function': sim_probability,
        'iterations': 1000,
        'input': [1, 4],
        'output': 0
    },
    {
        'function': sim_probability,
        'iterations': 1000,
        'input': [2, 4],
        'output': 0
    },
    {
        'function': sim_probability,
        'iterations': 1000,
        'input': [3, 4],
        'output': 0
    },
    {
        'function': sim_probability,
        'iterations': 1000,
        'input': [4, 4],
        'output': 0
    },
    {
        'function': sim_probability,
        'iterations': 1000,
        'input': [5, 4],
        'output': 0
    }
    ],
    [
    {
        'function': sim_probability,
        'iterations': 1000,
        'input': [0, 2],
        'output': 0
    },
    {
        'function': sim_probability,
        'iterations': 1000,
        'input': [1, 2],
        'output': 0
    },
    {
        'function': sim_probability,
        'iterations': 1000,
        'input': [2, 2],
        'output': 0
    },
    {
        'function': sim_probability,
        'iterations': 1000,
        'input': [3, 2],
        'output': 0
    },
    {
        'function': sim_probability,
        'iterations': 1000,
        'input': [-1, 2],
        'output': 0
    }
    ]
]


for sequence in tests:
    cdf = 0
    for test in sequence:
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

        cdf += successes / int(iterations)
        print(f'{(successes / int(iterations)):.3f} = {function.__name__}({trial}) over {iterations} trials')

    print(f'  {cdf:.3f} = CDF of sequence')


