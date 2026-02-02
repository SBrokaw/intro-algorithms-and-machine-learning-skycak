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
    for c in cookies:
        type = c[0]
        dist = c[2]
        if type not in unique_names:
            unique_names[type] = [1, dist]
        elif type in unique_names:
            unique_names[type][0] += 1 
            unique_names[type][1] += dist 

    init_choice = list(unique_names)[0]
    most_common = init_choice
    cnt = unique_names[init_choice][0]
    dist = unique_names[init_choice][1]
    for t in unique_names:
        if unique_names[t][0] >= cnt and unique_names[t][1] < dist: 
            most_common = t 
            dist = unique_names[t][1]

    return most_common

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
guess_log = {}
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
        if type_guess == type:  correct += 1
        else:                   wrong += 1

    guess_log[k] = [correct, wrong, total_guesses]

for row in guess_log:
    print(f"k:{row} {guess_log[row]}")

    
