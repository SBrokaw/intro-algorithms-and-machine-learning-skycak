# Skycak, J. (2021). Selection, Bubble, Insertion, and 
# Counting Sort. In Introduction to Algorithms and Machine 
# Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/selection-bubble-insertion-and-counting-sort/

def min_arr( arr ):
    if len(arr) < 1: return [None, None]
    idx_min = 0
    num_min = arr[0]

    for n in range(len(arr)):
        if arr[n] < num_min: idx_min = n; num_min = arr[n]

    return [idx_min, num_min]

test_arrays = [[],
               [-1, -2, 0, 1000, 0, -2, 200],
               [-1.9, -2.1, 0, 1000, 0, -2, 200],
               [200, 2, 0, -2, -200, -10]]

for trial in test_arrays:
    minimum = min_arr( trial )
    print(f'{str(trial).rjust(40)} -- {minimum}')