# Skycak, J. (2021). SIR Model For the Spread of Disease. In Introduction
# to Algorithms and Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/sir-model-for-the-spread-of-disease/

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
        val = self.derivatives[key](t, p)
        # print(f"  {self.derivatives[key].__name__}({t}, {p}) = {val}")
        return val

    def estimate_points(self, p0, dt, n):
        t = p0[0]
        p = p0[1]
        a, b, c = p['S'], p['I'], p['R']
        points = [(t, p)]
        for i in range(n):
            a += dt * self.eval_derivative('S', t, p)
            b += dt * (self.eval_derivative('I', t, p) - self.eval_derivative('R', t, p))
            c += dt * self.eval_derivative('R', t, p)  
            t += dt 
            p = {'S':a, 'I':b, 'R':c}
            points += [(t, p)]
            print(f"  {t}, {p}")

        return points


def dS_dt(t, p):
    return -1 * dI_dt(t, p)

def dI_dt(t, p):
    return 0.01 * p["S"] * p["I"] * 0.03

def dR_dt(t, p):
    return 0.02 * p["I"]


p0 = (0, {'S': 1000, 'I': 1, 'R': 0})
dt = 5
n = int((365) / dt)
derivatives = {'S': dS_dt, 'I': dI_dt, 'R': dR_dt}
euler_mv = EulerEstimatorMultivariable(derivatives)
points = euler_mv.estimate_points(p0, dt, n)
print(f"{[euler_mv.derivatives[key].__name__ for key in derivatives]}".center(40, '—'))
# for i in range(len(points)): print(f"p{i:.3g} ({points[0]}, {points[1]})")
# for p in points: print(p)

plt.figure()
tss = [p[0] for p in points]
Sss = [int(p[1]["S"]) for p in points]
Iss = [int(p[1]["I"]) for p in points]
Rss = [int(p[1]["R"]) for p in points]
plt.semilogx(tss, Sss, label="Susceptible")
plt.semilogx(tss, Iss, label="Infected")
plt.semilogx(tss, Rss, label="Recovered")

plt.title("SIR Infection Model -- Problem CH3_6")
plt.xlabel("time (days)")
plt.ylabel("Number of People")
plt.legend()
plt.grid(True)

plot_filename = "ch3_6_SIR_model.png"
plt.savefig(plot_filename)
print(f"  figure {plot_filename} generated")
