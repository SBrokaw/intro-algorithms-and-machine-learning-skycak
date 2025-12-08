# Skycak, J. (2021). K-Means Clustering. In Introduction to Algorithms 
# and Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/k-means-clustering/
from random import random
from dataclasses import dataclass

@dataclass
class Cluster:
    k_val: int
    data: list

    def center(self, i):
        if len(self.data) == 0: return 0
        if i > len(self.data[0]): return 0

        avg = 0
        for d in self.data:
            avg += d[i]

        return avg / len(self.data) 

    def centers(self):
        if len(self.data) == 0: return [0]

        avgs = [0] * len(self.data[0])
        for i in range(len(self.data[0])):
            for d in self.data:
                avgs[i] += d[i] 

        return [i / len(self.data) for i in avgs]

    def pretty_centers(self):
        pretty_centers = [f'{i: .3g}' for i in self.centers()]
        return pretty_centers

def distance(v1, v2):
    d = sum([(p2 - p1) ** 2 for p1, p2 in zip(v1, v2)])
    return d ** (1/2)

def distances(v1, centers):
    return [distance(v1, c) for c in centers]

def pretty_distances(v1, centers):
    return [f'{i: .3g}' for i in distances(v1, centers)]

def k_means_cluster(labels, data, k):
    # randomly assign data to k initial clusters
    clusters = [Cluster(i, []) for i in range(k)]
    print(clusters)
    for d in data:
        random_cluster = int(random() * k)
        clusters[random_cluster].data += [d]

    for c in clusters:
        print(f'cluster{c.k_val} centers:{c.pretty_centers()}')
        for item in c.data:
            print(f'  {item}')

    # calculate distances
    swapped = True
    while swapped:
        print("")
        swapped = False
        new_clusters = [Cluster(i, []) for i in range(k)]
        centers = [c.centers() for c in clusters]
        for c in clusters:
            for d in c.data:
                dists = distances(d, centers)
                new_cluster = min(range(len(dists)), key=lambda i: dists[i])
                print(  f'{d} '.ljust(30)
                      + f'dists:{pretty_distances(d, centers)} '.ljust(50)
                      + f'c{c.k_val}->c{new_cluster} '
                      + f'{"!" if c.k_val!=new_cluster else ""}') 
                new_clusters[new_cluster].data += [d]
                if c.k_val != new_cluster: 
                    swapped |= True
                    # for cc in clusters:
                    #     print(f'cluster{cc.k_val} centers:{cc.pretty_centers()}')
                    #     for item in cc.data:
                    #         print(f'  {item}')
                    # for cc in new_clusters:
                    #     print(f'new_cluster{cc.k_val} centers:{cc.pretty_centers()}')
                    #     for item in cc.data:
                    #         print(f'  {item}')
            
        clusters = new_clusters[:]
    
    column_spacing = 15
    screen_width = column_spacing * len(labels)
    print(f"".center(screen_width, ' '))
    print(f" Final Clusters ".center(screen_width, '='))
    for label in labels:
        print(f'{label}'.center(column_spacing), end='')
    print()
    print(f"".center(screen_width, '‾'))

    for c in clusters:
        print(f'cluster{c.k_val} centers:{c.pretty_centers()}')
        for item in c.data:
            for val in item:
                print(f'{val}'.center(column_spacing), end = '')
            print()

    return 0


columns = ['Portion Eggs', 'Portion Butter', 'Portion Sugar', 'Portion Flour']
data = [
    [0.14, 0.14, 0.28, 0.44],
    [0.22, 0.1,  0.45, 0.33],
    [0.1,  0.19, 0.25, 0.4 ],
    [0.02, 0.08, 0.43, 0.45],
    [0.16, 0.08, 0.35, 0.3 ],
    [0.14, 0.17, 0.31, 0.38],
    [0.05, 0.14, 0.35, 0.5 ],
    [0.1,  0.21, 0.28, 0.44],
    [0.04, 0.08, 0.35, 0.47],
    [0.11, 0.13, 0.28, 0.45],
    [0.0,  0.07, 0.34, 0.65],
    [0.2,  0.05, 0.4,  0.37],
    [0.12, 0.15, 0.33, 0.45],
    [0.25, 0.1,  0.3,  0.35],
    [0.0,  0.1,  0.4,  0.5 ],
    [0.15, 0.2,  0.3,  0.37],
    [0.0,  0.13, 0.4,  0.49],
    [0.22, 0.07, 0.4,  0.38],
    [0.2,  0.18, 0.3,  0.4 ]
]

k_means_cluster(columns, data, 3)