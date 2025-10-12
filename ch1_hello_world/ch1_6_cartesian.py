# Skycak, J. (2021). Cartesian Product. In Introduction to Algorithms and Machine Learning: 
# from Sorting to Strategic Agents. https://justinmath.com/cartesian-product/
import pdb

def cartesian_product( ranges ):
    points = [[]]

    count = 1
    extended = []

    for i in range(len(ranges)):
        for item in points:
            extended.append(item)
        print(f'[DEBUG 14] {extended}')

        for u in range(len(extended)):
            extended[u].append(ranges[i][u])
        print(f'[DEBUG 19] {extended}')
        
        for item in extended:
            points.append(item)
        print(f'[DEBUG 23] {points}')


    print(f'{len(points)} {points}')


cartesian_product([[1, 2],
                   ['09', '08']
                  ])

cartesian_product([[1, 2]
                  ])