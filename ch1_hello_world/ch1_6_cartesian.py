# Skycak, J. (2021). Cartesian Product. In Introduction to Algorithms and Machine Learning: 
# from Sorting to Strategic Agents. https://justinmath.com/cartesian-product/
import pdb

def cartesian_product( ranges ):
    points = [[]]

    for r in ranges:
        points = [p + [v] for p in points for v in r]
        #print(f'[DEBUG 10] {points}')

    print(f'[DEBUG 12] {len(points)} {points}')
    return points


# Exercise 1 — Flatten a 2D list
# Input: matrix = [[1, 2], [3, 4], [5, 6]]
# Goal: produce a flat list of all elements: [1, 2, 3, 4, 5, 6].
# Hint: single list comprehension with two for clauses.
def flatten_list( ranges ):
    points = []
    points = [[v] for r in ranges for v in r]
    print(f'[DEBUG 23] {points}')

    return 0


# Exercise 2 — Filter and transform
# Input: nums = [1, 2, 3, 4, 5, 6]
# Goal: make a list of squares of even numbers only: [4, 16, 36].
# Hint: include an if clause in the comprehension.
def squares_of_even_numbers( nums ): 
    points = []
    points = [[v**2] for v in nums if v % 2 == 0]
    print(f'[DEBUG 35] {points}')

    return 0


# Exercise 3 — Create a multiplication table
# Goal: 3×3 multiplication table as a list of tuples (i, j, i*j), for i, j in 1..3.
# Expected output:
# [(1,1,1), (1,2,2), (1,3,3), (2,1,2), (2,2,4), ... , (3,3,9)]
# Hint: nested for clauses.
def multiplication_table( i, j ):
    points = [(m+1, n+1, (m+1)*(n+1)) for m in range(i) for n in range(j)]
    print(f'[DEBUG 47] {points}')

    return 0


# Exercise 4 — Cartesian product with condition
# Input:
# A = [1, 2, 3]
# B = [4, 5]
# Goal: all (a, b) pairs where a + b is even.
# Expected: [(1,5), (2,4), (3,5)]
# Hint: add an if at the end of the comprehension.
def cartesian_product_only_evens( ranges ):
    points = [[]]
    for r in ranges:
        points = [p + [v] for p in points for v in r]

    points = [p for p in points if sum(p) % 2 == 0]

    print(f'[DEBUG 62] {points}')
    return 0



# Exercise 5 — Nested list of squares
# Input:
# nums = [1, 2, 3]
# Goal: produce [[1, 1], [2, 4], [3, 9]] — each element paired with its square.
def squares( nums ):
    points = [[]]
    points = [[v] + [v**2] for v in nums]

    print(f'[DEBUG 79] {points}')
    return 0



cartesian_product([[1, 2],
                   ['09', '08']
                  ])
cartesian_product([[1, 2]
                  ])
cartesian_product( [[1, 2, 3, 4], [10, 9, 8, 7, 6], [5, 6, 7]] )
flatten_list([[1, 2], [3, 4], [5, 6]])
squares_of_even_numbers([-8, -7, 1, 2, 3, 4, 5, 6, 7, 8])
multiplication_table(3, 3)
cartesian_product_only_evens( [[1, 2, 3], [4, 5]] )
cartesian_product_only_evens( [[1, 2, 3, 4], [10, 9, 8, 7, 6], [5, 6, 7]] )
squares([1, 2, 3])