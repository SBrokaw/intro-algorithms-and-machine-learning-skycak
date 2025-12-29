# Skycak, J. (2021). Hodgkin-Huxley Model of Action Potentials in Neurons. 
# In Introduction to Algorithms and Machine Learning: 
# from Sorting to Strategic Agents. 
# https://justinmath.com/hodgkin-huxley-model-of-action-potentials-in-neurons/

import matplotlib.pyplot as plt

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
        a, b, c, d = p['V'], p['n'], p['m'], p['h']
        points = [(t, p)]
        for i in range(n):
            a += 0 #dt * self.eval_derivative('S', t, p)
            b += 0 #dt * (self.eval_derivative('I', t, p) - self.eval_derivative('R', t, p))
            c += 0 #dt * self.eval_derivative('R', t, p)  
            d += 0 #dt * self.eval_derivative('R', t, p)  
            t += dt 
            p = {'V':a, 'n':b, 'm':c, 'h':d}
            points += [(t, p)]
            print(f"  {t}, {p}")

        return points

def stimulus(t):
    intervals = [(10, 11),
                 (20, 21),
                 (30, 40),
                 (50, 51),
                 (53, 54),
                 (56, 57),
                 (59, 60),
                 (62, 63),
                 (65, 66)]
    stim = 150 if any(lo <= t and t <= hi for lo, hi in intervals) else 0

    return stim

def dV_dt(t, p):
    return 0

def dn_dt(t, p):
    return 0

def dm_dt(t, p):
    return 0

def dh_dt(t, p):
    return 0


p0 = (0, {'V': 0, 'n': 1, 'm': 0, 'h': 0})
dt = 1
n = int((80) / dt) # t ∈ [0, 80 ms]
derivatives = {'V': dV_dt, 'n': dn_dt, 'm': dm_dt, 'h': dh_dt}
euler_mv = EulerEstimatorMultivariable(derivatives)
points = euler_mv.estimate_points(p0, dt, n)
print(f"{[euler_mv.derivatives[key].__name__ for key in derivatives]}".center(40, '—'))
# for i in range(len(points)): print(f"p{i:.3g} ({points[0]}, {points[1]})")
# for p in points: print(p)

plt.figure()
tss = [p[0] for p in points]
sss = [stimulus(p[0]) for p in points]
Vss = [int(p[1]["V"]) for p in points]
nss = [int(p[1]["n"]) for p in points]
mss = [int(p[1]["m"]) for p in points]
hss = [int(p[1]["h"]) for p in points]
plt.plot(tss, sss, label="Stimulus")
plt.plot(tss, Vss, label="Membrance Potential")
plt.plot(tss, nss, label="n")
plt.plot(tss, mss, label="m")
plt.plot(tss, hss, label="h")

plt.title("Hodgkin-Huxley Neuron Action Potential Model -- Problem CH3_7")
plt.xlabel("time (ms)")
plt.ylabel("Voltage (mV)")
plt.legend()
plt.grid(True)

plot_filename = "ch3_7_Hodgkin_Huxley.png"
plt.savefig(plot_filename)
print(f"  figure {plot_filename} generated")
