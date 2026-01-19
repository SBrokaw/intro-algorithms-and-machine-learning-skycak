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
print(f" Chapter 4 Lesson 6——K Nearest Neighbors ".center(table_width, '='))
new_cookie = [0.25, 0.3]
data_distances = [[type, ingredients, distance(new_cookie, ingredients)] for (type, ingredients) in data]
data_distance_sorted = sorted(data_distances, key=lambda cookie: cookie[2])
print(f"  data_distances:")
for d in data_distance_sorted: print(f"  {d}")

## Leave One Out Cross-Validation 
for k in range(1, 10):
    for (type, ratios) in data:
        remaining_cookies = [[type2, ratios2] for (type2, ratios2) in data if (type, ratios) != (type2, ratios2)]
        for rc in remaining_cookies: print(f"    {rc}")
        data_distances = [[type, ingredients, distance(new_cookie, ingredients)] for (type, ingredients) in data]
        data_distance_sorted = sorted(data_distances, key=lambda cookie: cookie[2])

    
