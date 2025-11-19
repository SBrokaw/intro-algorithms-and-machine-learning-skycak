# Skycak, J. (2021). Merge Sort and Quicksort. In Introduction to Algorithms 
# and Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/merge-sort-and-quicksort/

import random

def merge_s( arr1_arg, arr2_arg ):
    arr1 = arr1_arg.copy()
    arr2 = arr2_arg.copy()
    sorted = []

    while len(arr1) > 0 and len(arr2) > 0:
        if arr1[0] <= arr2[0]: sorted += [arr1.pop(0)]
        elif arr2[0] < arr1[0]: sorted += [arr2.pop(0)]

    sorted += arr1 if arr1 else arr2

    return sorted

def merge( arr1, arr2 ):
    # sorted = [i for i in arr1] + [j for j in arr2]
    # sorted.sort()

    # return sorted
    return merge_s(arr1, arr2)

def merge_qs( arr1, arr2, arr3 ):
    sorted = [i for i in arr1] + [j for j in arr2] + [k for k in arr3]
    sorted.sort()

    return sorted

def merge_sort( arr ):
    n = len(arr)
    split = int(n/2)

    #base case
    if n <= 1: return arr

    arr1 = merge_sort(arr[0:split])
    arr2 = merge_sort(arr[split:n])
    sorted = merge(arr1, arr2)

    # print(f'\t{arr} .. {arr1} .. {arr2} .. {sorted}')
    return sorted

def quicksort( arr ):
    arr1 = arr.copy()
    if len(arr1) <= 1: return arr1

    pivot = random.choice(arr1)
    lesser = [i for i in arr1 if i < pivot]
    greater = [i for i in arr1 if i > pivot]
    equal = [i for i in arr1 if i == pivot]

    sorted = equal
    sorted += quicksort(lesser)
    sorted += quicksort(greater)
    sorted.sort()

    return sorted



trials = [[9, 6],
          [-10, 20, 30],
          [-1, 2],
          [6, 9, 7, 4, 2, 1, 8, 5]]

print(str(" Merge Sort ".center(80, '=')))
for t in trials:
    print(f'{t} BEGIN')
    sorted = merge_sort(t)
    print(f'\t{t} --> {sorted}')

print(merge_s([6, 9], [1]))
print(merge_s([6, 9, 13], [1]))
print(merge_s([6], [1]))

print(str(" Quicksort ".center(80, '=')))
for t in trials:
    print(f'{t} BEGIN')
    sorted = quicksort(t)
    print(f'\t{t} --> {sorted}')
