# Skycak, J. (2021). Merge Sort and Quicksort. In Introduction to Algorithms 
# and Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/merge-sort-and-quicksort/

def merge( arr1, arr2 ):
    sorted = []
    for i in range(len(arr1 + arr2)):
        if arr1[0] <= arr2[0]: 
            sorted += arr1[0]
            arr1.pop(0)

        else: 
            sorted += arr2[0]
            arr2.pop(0)

    return sorted

def merge_sort( arr ):
    n = len(arr)
    split = int(n/2)

    #base case
    if n <= 1: return [arr] 

    merge_sort(arr[0:split])
    merge_sort(arr[split:n])

    return 0

print(merge([6, 7], [2]))

trials = [[6, 9, 7, 4, 2, 1, 8, 5]]

print(str(" Merge Sort ".center(80, '=')))
for t in trials:
    merge_sort(t)
