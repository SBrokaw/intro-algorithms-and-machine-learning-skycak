from ch1_3_recursion import *

tests = [
    {
        'function' : problem1_array,
        'input' : ['b'],
        'output' : 0
    },
    {
        'function' : problem1_array,
        'input' : ['-10'],
        'output' : 0
    },
    {
        'function' : problem1_array,
        'input' : ['1'],
        'output' : [5]
    },
    {
        'function' : problem1_array,
        'input' : ['2'],
        'output' : [5, 11]
    },
    {
        'function' : problem1_array,
        'input' : ['3'],
        'output' : [5, 11, 29]
    },
    {
        'function' : problem1_recursion,
        'input' : ['b'],
        'output' : 0
    },
    {
        'function' : problem1_recursion,
        'input' : ['-10'],
        'output' : 0
    },
    {
        'function' : problem1_recursion,
        'input' : ['1'],
        'output' : 5
    },
    {
        'function' : problem1_recursion,
        'input' : ['2'],
        'output' : 11
    },
    {
        'function' : problem1_recursion,
        'input' : ['3'],
        'output' : 29
    },
    {
        'function' : problem2_array,
        'input' : ['-99'],
        'output' : 0
    },
    {
        'function' : problem2_array,
        'input' : ['$'],
        'output' : 0
    },
    {
        'function' : problem2_array,
        'input' : ['1'],
        'output' : [25]
    },
    {
        'function' : problem2_array,
        'input' : ['2'],
        'output' : [25, 74]
    },
    {
        'function' : problem2_array,
        'input' : ['3'],
        'output' : [25, 74, 37]
    },
    {
        'function' : problem2_recursion,
        'input' : ['-99'],
        'output' : 0
    },
    {
        'function' : problem2_recursion,
        'input' : ['∆'],
        'output' : 0
    },
    {
        'function' : problem2_recursion,
        'input' : ['1'],
        'output' : 0
    },
    {
        'function' : problem2_recursion,
        'input' : ['2'],
        'output' : 0
    },
    {
        'function' : problem2_recursion,
        'input' : ['3'],
        'output' : 0
    }
]


successes = 0
failures = 0

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

    if result == goal:
        successes += 1
    else:
        failures += 1
        print(f'!ch1_3_test FAIL! {function.__name__}({trial})')
        print(f'!ch1_3_test FAIL!   returned {result}')
        print(f'!ch1_3_test FAIL!   expected {goal}')

print(f'Testing complete with {successes} passes and {failures} failures')
