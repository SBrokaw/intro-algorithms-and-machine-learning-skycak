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

def selection_sort( arr ):
    print(f'{str(arr).center(80, '-')}')
    sorted = []
    unsorted = list(arr.copy())

    for i in range(len(unsorted)):
        [idx, n] = min_arr( unsorted )
        sorted.append(n)
        unsorted.pop(idx)
        print(f'  {str(sorted).rjust(35)} -- {str(unsorted).ljust(35)}')

    print(f'{str(" ..sorted " + str(sorted)).center(80)}')
    return sorted

def bubble_sort( arr ):
    print(f'{str(arr)}')
    unsorted = list(arr.copy())

    swap = bool(unsorted) # false if unsorted is empty
    while swap:
        swap = False
        print(f'  {str(unsorted)}')
        for i in range(len(unsorted) - 1):
            if unsorted[i] > unsorted[i+1]:
                unsorted[i:i+2] = [unsorted[i+1], unsorted[i]]
                print(f'    {str(unsorted)}')
                swap = True
    
    print(f'  ..sorted {str(unsorted)}')
    return unsorted

def selection_sort( arr ):
    print(f'{str(arr)}')
    unsorted = list(arr.copy())

    swap = bool(unsorted) # false if unsorted is empty
    while swap:
        swap = False
        print(f'  {str(unsorted)}')
        for i in range(len(unsorted) - 1):
            if unsorted[i] > unsorted[i+1]:
                unsorted[i:i+2] = [unsorted[i+1], unsorted[i]]

    return 0

test_arrays = [[],
               [-1, -2, 0, 1000, 0, -2, 200],
               [-1.9, -2.1, 0, 1000, 0, -2, 200],
               [200, 2, 0, -2, -200, -10]]

print(f' Array '.center(35, '=') + ' -- ' + f' Minimum '.center(20, '='))
for trial in test_arrays:
    minimum = min_arr( trial )
    print(f'{str(trial).rjust(35)} -- {minimum}')

print('')
print(f' Selection Sort '.center(80, '='))
for trial in test_arrays:
    selection_sort( trial )

print('')
print(f' Bubble Sort '.center(80, '='))
for trial in test_arrays:
    bubble_sort( trial )