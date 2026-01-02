# Skycak, J. (2021). Hash Tables. 
# In Introduction to Algorithms and Machine Learning: 
# from Sorting to Strategic Agents. 
# https://justinmath.com/hash-tables/

def print_hash_table(table):
    print('[')
    for bucket in table:
        print(f"  {bucket},")
    print(']')

def hash(string):
    bucket = sum([ord(c) - 97 for c in string.lower()]) % 5
    return bucket

def insert(array, key, value):
    array[hash(key)].append((key, value))
    return 0

def find(array, key):
    bucket = hash(key)
    for item in array[bucket]:
        if item[0] == key: 
            return item[1]

    return None


array = [[], [], [], [], []] # 5 buckets
print(array)
insert(array, 'a', [0, 1])
insert(array, 'b', "abcd")
insert(array, 'c', 3.14)
print_hash_table(array)
print()

insert(array, 'd', 0)
insert(array, 'e', 0)
insert(array, 'f', 0)
print_hash_table(array)
print()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i, char in enumerate(alphabet):
    key = 'someletters'+char
    value = [i, i**2, i**3]
    insert(array, key, value)

for i, char in enumerate(alphabet):
    key = 'someletters'+char
    output_value = find(array, key)
    desired_value = [i, i**2, i**3]
    assert output_value == desired_value
