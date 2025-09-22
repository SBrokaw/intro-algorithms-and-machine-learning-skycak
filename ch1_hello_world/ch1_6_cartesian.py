# Skycak, J. (2021). Cartesian Product. In Introduction to Algorithms and Machine Learning: 
# from Sorting to Strategic Agents. https://justinmath.com/cartesian-product/

def cartesian_product( ranges ):
    points = [None] * len(ranges)

    count = 1
    for i in range(len(ranges)):
        count *= len(ranges[i])
    result = [None] * count

    print(f'{len(points)} {points}')
    print(f'{len(result)} {result}')


cartesian_product([[1, 2],
                   [0, 0, 0, 0],
                   ['a', 'b', 'c']
                  ])
