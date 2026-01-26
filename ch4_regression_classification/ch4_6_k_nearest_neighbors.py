# Skycak, Justin (2022), K-Nearest Neighbors.
# in Introduction to Algorithms and Machine Learning:
# from Sorting to Strategic Agents
# 

from dataclasses import dataclass
from math import sqrt

@dataclass
class Cookie:
    type: str # e.g. Shortbread, Sugar, etc.
    ingredients_ratios: list # [Portion Butter, Portion Sugar]
    distance: float

def distance(p1, p2):
    dist = 0.0
    for i in range(len(p1)):
        dist += (p1[i] - p2[i]) ** 2
    return sqrt(dist)


# @input: array of [[], [], distance]
# @returns: lowest n elements of data based on `distance` field
#           if the final element has the same distance as subsequent elements, also return those
def k_nearest(data, k):
    if k <= 0: return []
    if k > len(data): k = len(data)
    data_sorted = sorted(data, key=lambda cookie: cookie[2])
    nearest = [_ for _ in data_sorted[:k]]

    while(len(nearest) < len(data_sorted) and data_sorted[len(nearest)][2] <= nearest[-1][2]):
        nearest += [data_sorted[len(nearest)]]

    return nearest
    

def majority_type(cookies):
    unique_names = {}
    for 

data = [   ["Shortbread", [0.15, 0.2]],
           ["Shortbread", [0.15, 0.3]],
           ["Shortbread", [0.2, 0.25]],
           ["Shortbread", [0.25, 0.4]],
           ["Shortbread", [0.3, 0.35]],
           ["Sugar", [0.05, 0.25]],
           ["Sugar", [0.05, 0.35]],
           ["Sugar", [0.1, 0.3]],
           ["Sugar", [0.15, 0.5]],
           ["Sugar", [0.25, 0.35]]]

table_width = 80
print(f" Chapter 4, Lesson 6: K Nearest Neighbors ".center(table_width, '='))
new_cookie = [0.25, 0.3]
data_distances = [[type, ingredients, distance(new_cookie, ingredients)] for (type, ingredients) in data]

## Leave One Out Cross-Validation 
## for each value of k, find how many cookie guesses would match its real classification
## the accuracy of each value of k will then determine the best value to use for new cookies
for k in range(1, 10):
    correct = 0
    wrong = 0
    total_guesses = len(data)

    # for each cookie, check the k-nearest neighbors to determine the type of cookie
    # check if the guess is correct based on the real type of the leave-one-out cookie
    for (type, ratios) in data:
        remaining_cookies = [[type2, ratios2] for (type2, ratios2) in data if (type, ratios) != (type2, ratios2)]

        data_distances = [[type, ingredients, distance(ratios, ingredients)] for (type, ingredients) in remaining_cookies]

        nearest_k_cookies = k_nearest(data_distances, k)
        type_guess = majority_type(nearest_k_cookies)
        # print(f"  Nearest {k} Cookies to {type}, {ratios}:")
        # for c in nearest_k_cookies: print(f"    {c}")

    
