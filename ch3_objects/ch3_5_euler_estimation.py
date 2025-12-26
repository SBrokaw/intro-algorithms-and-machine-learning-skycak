# Skycak, J. (2021). Euler Estimation. In Introduction to Algorithms 
# and Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/euler-estimation/
from math import e
import matplotlib.pyplot as plt

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

class EulerEstimatorMultivariable():
    def __init__(self, derivatives):
        self.derivatives = derivatives

    def eval_derivative(self, key, t, p):
        return self.derivatives[key](t, p)

    def estimate_points(self, p0, dt, n):
        t = p0[0]
        p = p0[1]
        a, b, c = p['a'], p['b'], p['c']
        points = [(t, p)]
        for i in range(n):
            a += dt * self.eval_derivative('a', t, p)
            b += dt * self.eval_derivative('b', t, p)
            c += dt * self.eval_derivative('c', t, p)
            t += dt 
            p = {'a':a, 'b':b, 'c':c}
            points += [(t, p)]
            # print(f"  {t}, {p}")

        return points

def derivative_00(p):
    return p[0] + 1

# https://tutorial.math.lamar.edu/Classes/DE/EulersMethod.aspx
def derivative_01(p):
    return 2 - e ** (-4 * p[0]) - (2 * p[1])

def derivative_02(p):
    return p[0] - 2

def da_dt_03(t, p):
    val = p["a"] + 1
    # print(f"    da_dt_03 t:{t} p:{p} = {val}")
    return val

def db_dt_03(t, p):
    return p["a"] + p["b"]

def dc_dt_03(t, p):
    return 2 * p["b"] + 3 * t


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


p0_options = [(0, -2), (0, -1), (0, 0), (0, 1), (0, 2)]
n = 50
dx = 5 / n
points = []
euler = EulerEstimator(derivative_02)
for p0 in p0_options:
    points += [euler.estimate_points(p0, dx, n)]
print(f"{euler.derivative.__name__}".center(20, '—'))
# for i in range(len(points)): print(f"p{i:.3g} ({points[i][0]:.3g}, {points[i][1]:.3g})")

plt.figure()
for curve in points:
    xss = [v[0] for v in curve]
    yss = [v[1] for v in curve]
    plt.plot(xss, yss, label=f"f({xss[0]}) = {yss[0]}")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Euler Estimation: dy/dx = x - 2")
plt.legend()
plt.grid(True)

# plt.savefig("euler_estimation_02.png")
print("  figure plotted")
print()


p0 = (-0.4, {'a': -0.45, 'b': -0.05, 'c': 0})
n = 3
dt = 2
derivatives = {'a': da_dt_03, 'b': db_dt_03, 'c': dc_dt_03}
euler_mv = EulerEstimatorMultivariable(derivatives)
points = euler_mv.estimate_points(p0, dt, n)
print(f"{[euler_mv.derivatives[key].__name__ for key in derivatives]}".center(20, '—'))
# for i in range(len(points)): print(f"p{i:.3g} ({points[0]}, {points[1]})")
for p in points: print(p)
