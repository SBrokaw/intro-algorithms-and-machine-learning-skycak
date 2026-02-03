# Skycak, Justin (2022), K-Nearest Neighbors.
# in Introduction to Algorithms and Machine Learning:
# from Sorting to Strategic Agents
# 
from math import sqrt

def distance(p1, p2):
    dist = 0.0
    for i in range(len(p1)):
        dist += (p1[i] - p2[i]) ** 2
    return sqrt(dist)

# @input: array of [type, ratios, distance]
# @returns: lowest n elements of data based on `distance` field
#           if the final elements have the same distance as subsequent elements, also return those
def k_nearest(data, k):
    if k <= 0: return []
    if k > len(data): k = len(data)
    data_sorted = sorted(data, key=lambda cookie: cookie[2])
    nearest = [_ for _ in data_sorted[:k]]

    # add all elements of data_sorted that have the same distance as the last element in nearest
    for c in data_sorted[k:]:
        if c[2] <= (nearest[-1][2] + 0.001):
            nearest += [c.copy()]
        else: 
            break

    return nearest
    
# return whichever type of cookie is most common in the input array.
# If there is a tie (i.e. 2 and 2), average the distances and pick the lowest distance
def majority_type(cookies):
    unique_names = {} # one entry for each input type containing the count and avg. distance
    for c in cookies:
        type = c[0]
        dist = c[2]
        if type not in unique_names:
            unique_names[type] = [1, dist]
        elif type in unique_names:
            unique_names[type][0] += 1 
            unique_names[type][1] += dist 

    # print(unique_names)
    # for c in unique_names: print(f"    {c}")

    init_choice = list(unique_names)[0]
    most_common = init_choice
    cnt = unique_names[init_choice][0]
    dist = unique_names[init_choice][1]
    for t in unique_names:
        if unique_names[t][0] > cnt or (unique_names[t][0] == cnt and unique_names[t][1] < dist): 
            most_common = t 
            dist = unique_names[t][1]

    return most_common

datasets = [[   ["Shortbread", [0.15, 0.2]],
                ["Shortbread", [0.15, 0.3]],
                ["Shortbread", [0.2, 0.25]],
                ["Shortbread", [0.25, 0.4]],
                ["Shortbread", [0.3, 0.35]],
                ["Sugar", [0.05, 0.25]],
                ["Sugar", [0.05, 0.35]],
                ["Sugar", [0.1, 0.3]],
                ["Sugar", [0.15, 0.4]],
                ["Sugar", [0.25, 0.35]]     ],
            [   ["Shortbread", [0.6, 200]],
                ["Shortbread", [0.6, 300]],
                ["Shortbread", [0.8, 250]],
                ["Shortbread", [1.0, 400]],
                ["Shortbread", [1.2, 350]],
                ["Sugar", [0.2, 250]],
                ["Sugar", [0.2, 350]],
                ["Sugar", [0.4, 300]],
                ["Sugar", [0.6, 400]],
                ["Sugar", [1.0, 350]]       ],
            [   ["Shortbread", [0.4, 0.0]],
                ["Shortbread", [0.4, 0.5]],
                ["Shortbread", [0.6, 0.25]],
                ["Shortbread", [0.8, 1]],
                ["Shortbread", [1.0, 0.75]],
                ["Sugar", [0.0, 0.25]],
                ["Sugar", [0.0, 0.75]],
                ["Sugar", [0.2, 0.5]],
                ["Sugar", [0.4, 1.0]],
                ["Sugar", [0.8, 0.75]]       ]]

table_width = 80
print(f" Chapter 4, Lesson 6: K Nearest Neighbors ".center(table_width, '='))
new_cookie = [0.25, 0.3]
guess_log = {}
for k in range(1, 10):    
    data_distances = [[t, r, distance(new_cookie, r)] for (t, r) in datasets[0]]
    nearest_k_cookies = k_nearest(data_distances, k)
    type_guess = majority_type(nearest_k_cookies)

    guess_log[k] = [type_guess]

print(f"New Cookie:{new_cookie} Guesses")
for row in guess_log:
    print(f"  k:{row} {guess_log[row]}")
print()


## Leave One Out Cross-Validation 
## for each value of k, find how many cookie guesses would match its real classification
## the accuracy of each value of k will then determine the best value to use for new cookies
for data in datasets:
    guess_log = {}
    for k in range(1, 10):
        correct = 0
        wrong = 0
        total_guesses = len(data)

        # for each cookie, check the k-nearest neighbors to determine the type of cookie
        # check if the guess is correct based on the real type of the leave-one-out cookie
        for (cookie_type, ratios) in data:
            remaining_cookies = [(t, r) for (t, r) in data if r is not ratios]

            data_distances = [[t, r, distance(ratios, r)] for (t, r) in remaining_cookies]

            nearest_k_cookies = k_nearest(data_distances, k)
            type_guess = majority_type(nearest_k_cookies)
            # print(f"{cookie_type} {ratios} GUESS:{type_guess}")
            # for c in nearest_k_cookies: print(f"  {c}")
            if type_guess == cookie_type:  correct += 1
            else:                   wrong += 1

        guess_log[k] = [correct, wrong, total_guesses]

    print(f"Leave-One-Out Cross-Validation Accuracy")
    for row in guess_log:
        print(f"  k:{row} {guess_log[row]}")
    print()


 
