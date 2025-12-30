# Skycak, J. (2021). Hodgkin-Huxley Model of Action Potentials in Neurons. 
# In Introduction to Algorithms and Machine Learning: 
# from Sorting to Strategic Agents. 
# https://justinmath.com/hodgkin-huxley-model-of-action-potentials-in-neurons/

import matplotlib.pyplot as plt
from math import exp

# _CONSTS
_C = 1.0
_V_Na = 115
_V_K = -12
_V_L = 10.6
_g_Na = 120
_g_K = 36
_g_L = 0.3

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

def alpha_n(V):
    return 0.01 * (10 - V) / (exp(0.1 * (10 - V)) - 1)

def alpha_m(V):
    return 0.01 * (25 - V) / (exp(0.1 * (25 - V)) - 1)

def alpha_h(V):
    return 0.07 * exp(-1 * V / 20)

def Beta_n(V):
    return 0.125 * exp(-1 * V / 80)

def Beta_m(V):
    return 4 * exp(-1 * V / 18)

def Beta_h(V):
    return 1 / (exp(0.1 * (30 - V)) + 1)

def dV_dt(t, p):
    return (1 / _C) * (stimulus(t))

def dn_dt(t, p):
    return alpha_n(p['V']) * (1 - p['n']) - Beta_n(p['V']) * p['n']

def dm_dt(t, p):
    return alpha_m(p['V']) * (1 - p['m']) - Beta_m(p['V']) * p['m']

def dh_dt(t, p):
    return alpha_h(p['V']) * (1 - p['h']) - Beta_h(p['V']) * p['h']

V_0 = 0
n_0 = alpha_n(V_0) / (alpha_n(V_0) + Beta_n(V_0)) 
m_0 = alpha_m(V_0) / (alpha_m(V_0) + Beta_m(V_0))
h_0 = alpha_h(V_0) / (alpha_h(V_0) + Beta_h(V_0))
p0 = (0, {'V': V_0, 'n': n_0, 'm': m_0, 'h': h_0})
dt = 1.1
n = int((80) / dt) # t ∈ [0, 80 ms]
derivatives = {'V': dV_dt, 'n': dn_dt, 'm': dm_dt, 'h': dh_dt}
euler_mv = EulerEstimatorMultivariable(derivatives)
points = euler_mv.estimate_points(p0, dt, n)
print(f"{[euler_mv.derivatives[key].__name__ for key in derivatives]}".center(40, '—'))
print(f"  p0: {p0}")
# for i in range(len(points)): print(f"p{i:.3g} ({points[0]}, {points[1]})")
# for p in points: print(p)

figure, (plt1, plt2) = plt.subplots(2, 1)
tss = [p[0] for p in points]
sss = [stimulus(p[0]) for p in points]
Vss = [int(p[1]["V"]) for p in points]
nss = [int(p[1]["n"]) for p in points]
mss = [int(p[1]["m"]) for p in points]
hss = [int(p[1]["h"]) for p in points]
plt1.plot(tss, sss, label="Stimulus")
plt1.plot(tss, Vss, label="Membrance Potential")
# plt.title("Hodgkin-Huxley Neuron Action Potential Model -- Problem CH3_7")
# plt.ylabel("Voltage (mV)")
# plt.legend()
# plt.grid(True)

plt2.plot(tss, nss, label="n")
plt2.plot(tss, mss, label="m")
plt2.plot(tss, hss, label="h")

plt.xlabel("time (ms)")
plt.legend()
plt.grid(True)

plot_filename = "ch3_7_Hodgkin_Huxley.png"
plt.savefig(plot_filename)
print(f"  figure {plot_filename} generated")
