from ch1_3_recursion.py import *

tests = [
    {
        'function' = 'problem1_array',
        'input' = ['3'],
        'output' = ''
    }
]



print("=".center(50, '='))
print(" Chapter 1.3 Tests ".center(50, '='))
print("=".center(50, '='))

for test in tests:
    function = test['function']
    trial = test['input']
    goal = test['output']

    if isinstance(trial, (list, tuple)):
        result = function(*trial)
    else:
        result = function(trial)