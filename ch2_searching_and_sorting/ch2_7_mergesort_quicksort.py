# Skycak, J. (2021). Merge Sort and Quicksort. In Introduction to Algorithms 
# and Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/merge-sort-and-quicksort/

def merge_s( arr1_arg, arr2_arg ):
    arr1 = arr1_arg.copy()
    arr2 = arr2_arg.copy()
    sorted = []

    if len(arr1 + arr2) > 2:
        for i in range( len(arr1 + arr2) - 3 ):
            if arr1[0] < arr2[0]:
                sorted[i] = arr1[0]
            elif arr2[0] <= arr1[0]:
                sorted[i] = arr2[0]

    if len(arr1 + arr2) == 2:
        if arr1[0] < arr2[0]:
            sorted = [arr1[0], arr2[0]]
        elif arr2[0] <= arr1[0]:
            sorted = [arr2[0], arr1[0]]

    return sorted



def merge( arr1, arr2 ):
    sorted = [i for i in arr1] + [j for j in arr2]
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
print(merge_s([6, 9, 3], [1]))
print(merge_s([6], [1]))