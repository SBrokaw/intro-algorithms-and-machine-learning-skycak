from hello_world import * #check_if_symmetric, convert_to_numbers, convert_to_chars, get_intersection, get_union, count_characters

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
    },
    {
        'function': count_characters,
        'input': ['aabbccddefghijkzxyw'],
        'output': {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'z': 1, 'x': 1, 'y': 1, 'w': 1}
    },
    {
        'function': is_prime,
        'input': ['1092'],
        'output':  False
    },
    {
        'function': is_prime,
        'input': ['3'],
        'output':  True
    },
    {
        'function': is_prime,
        'input': ['2'],
        'output':  True
    },
    {
        'function': is_prime,
        'input': ['1'],
        'output':  False
    },
    {
        'function': is_prime,
        'input': ['huehue'],
        'output':  False
    },
    {
        'function': binary_to_decimal,
        'input': ['aabbccddefghijkzxyw'],
        'output': '0'
    },
    {
        'function': binary_to_decimal,
        'input': ['0b1000111'],
        'output': '0'
    },
    {
        'function': binary_to_decimal,
        'input': ['1100'],
        'output': '12'
    },
    {
        'function': binary_to_decimal,
        'input': ['11010'],
        'output': '26'
    },
    {
        'function': binary_to_decimal,
        'input': ['1000000111111010001111'],
        'output': '2129551'
    },
    {
        'function': decimal_to_binary,
        'input': ['111010001111'],
        'output': '1100111011000101101100011000011010111'
    },
    {
        'function': binary_to_decimal,
        'input': ['4000000151911010001811'],
        'output': '2129551'
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
        print(f'!ch1_test FAIL! {function.__name__}({trial})')
        print(f'!ch1_test FAIL!   returned {result}')
        print(f'!ch1_test FAIL!   expected {goal}')

print(f'Testing complete with {successes} passes and {failures} failures')


