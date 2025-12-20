# Skycak, J. (2021). Euler Estimation. In Introduction to Algorithms 
# and Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/euler-estimation/
from math import e

class EulerEstimator():
    def __init__(self, derivative):
        self.derivative = derivative

    def eval_derivative(self, p0):
        return self.derivative(p0)

    def estimate_points(self, p0, dx, n):
        x, y = p0
        points = [p0]
        for i in range(n):
            y += dx * self.eval_derivative((x, y))
            x += dx
            points += [(x, y)]

        return points


def derivative_00(p):
    return p[0] + 1

# https://tutorial.math.lamar.edu/Classes/DE/EulersMethod.aspx
def derivative_01(p):
    return 2 - e ** (-4 * p[0]) - (2 * p[1])

def derivative_02(p):
    return p[0] - 2


p0 = (1, 4)
dx = 0.5
n = 4
euler = EulerEstimator(derivative_00)
points = euler.estimate_points(p0, dx, n)
print(f"{euler.derivative.__name__}".center(20, '—'))
for i in range(len(points)): print(f"p{i:.3g} ({points[i][0]:.3g}, {points[i][1]:.3g})")

p0 = (0, 1)
dx = 0.1
n = 5
euler = EulerEstimator(derivative_01)
points = euler.estimate_points(p0, dx, n)
print(f"{euler.derivative.__name__}".center(20, '—'))
for i in range(len(points)): print(f"p{i:.3g} ({points[i][0]:.3g}, {points[i][1]:.3g})")