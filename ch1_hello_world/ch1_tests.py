from hello_world import check_if_symmetric, convert_to_numbers, convert_to_chars, get_intersection

tests = [
    {
        'function': check_if_symmetric,
        'input': ['a'*1000 + 'b'*1000 + 'a'*1000],
        'output': True
    },
    {
        'function': check_if_symmetric,
        'input': ["A man, a plan, a canal, Panama"],
        'output': False
    },
    {
        'function': check_if_symmetric,
        'input': [' '],
        'output': True
    },
    {
        'function': check_if_symmetric,
        'input': ['!!'],
        'output': True
    },
    {
        'function': check_if_symmetric,
        'input': [''],
        'output': True
    },
    {
        'function': check_if_symmetric,
        'input': ['NaN'],
        'output': True
    },
    {
        'function': check_if_symmetric,
        'input': ['1e1'],
        'output': True
    },
    {
        'function': check_if_symmetric,
        'input': ['Infinity'],
        'output': False
    },
    {
        'function': check_if_symmetric,
        'input': ['-42'],
        'output': False
    },
    {
        'function': check_if_symmetric,
        'input': ['hello'],
        'output': False
    },
    {
        'function': check_if_symmetric,
        'input': ['raceCAr'],
        'output': True
    },
    {
        'function': convert_to_numbers,
        'input': ['NaN'],
        'output': [78, 97, 78]
    },
    {
        'function': convert_to_numbers,
        'input': ['Infinity'],
        'output': [73, 110, 102, 105, 110, 105, 116, 121]
    },
    {
        'function': convert_to_numbers,
        'input': ['12,345'],
        'output': [49, 50, 44, 51, 52, 53]
    },
    {
        'function': convert_to_numbers,
        'input': ['!@#$%'],
        'output': [33, 64, 35, 36, 37]
    },
    {
        'function': convert_to_numbers,
        'input': ['12345'],
        'output': [49, 50, 51, 52, 53]
    },
    {
        'function': convert_to_numbers,
        'input': ['0x1A3F'],
        'output': [48, 120, 49, 65, 51, 70]
    },
    {
        'function': convert_to_chars,
        'output': 'Infinity',
        'input': [[73, 110, 102, 105, 110, 105, 116, 121]]
    },
    {
        'function': convert_to_chars,
        'output': '12,345',
        'input': [[49, 50, 44, 51, 52, 53]]
    },
    {
        'function': convert_to_chars,
        'output': '!@#$%',
        'input': [[33, 64, 35, 36, 37]]
    },
    {
        'function': convert_to_chars,
        'output': '12345',
        'input': [[49, 50, 51, 52, 53]]
    },
    {
        'function': convert_to_chars,
        'output': '0x1A3F',
        'input': [[48, 120, 49, 65, 51, 70]]
    },
    {
        'function': get_intersection,
        'input': ['0x1A3F', '0xffFF'],
        'output': ['0', 'x', 'F']
    }
]

successes = 0
failures = 0

print("=".center(50, '='))
print(" Chapter 1 Tests ".center(50, '='))
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
        print(f'!FAIL! {function.__name__}({trial})')
        print(f'!FAIL!   returned {result}')
        print(f'!FAIL!   expected {goal}')

print(f'Testing complete with {successes} passes and {failures} failures')


