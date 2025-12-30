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
        # print(f"  {t:.3g}, {p}")
        for i in range(n):
            a += dt * self.eval_derivative('V', t, p)
            b += dt * self.eval_derivative('n', t, p)
            c += dt * self.eval_derivative('m', t, p)  
            d += dt * self.eval_derivative('h', t, p)  
            t += dt 
            p = {'V':a, 'n':b, 'm':c, 'h':d}
            points += [(t, p)]
            debug_str = [f"{t:.3g}"] + [f"{pp}:{p[pp]:.3g} " for pp in p]
            # print(f"  {debug_str}")

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

def g_Na(m, h):
    return _g_Na * (m ** 3) * h

def g_K(n):
    return _g_K * (n ** 4)

def g_L():
    return _g_L

def I_Na(t, p):
    return g_Na(p['m'], p['h']) * (p['V'] - _V_Na)

def I_K(t, p):
    return g_K(p['n']) * (p['V'] - _V_K)

def I_L(t, p):
    return _g_L * (p['V'] - _V_L)

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
    return (1 / _C) * (stimulus(t) - I_Na(t, p) - I_K(t, p) - I_L(t, p))

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
dt = 0.005
n = int((19) / dt) # t ∈ [0, 80 ms]
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
Vss = [p[1]["V"] for p in points]
nss = [p[1]["n"] for p in points]
mss = [p[1]["m"] for p in points]
hss = [p[1]["h"] for p in points]

plt1.plot(tss, sss, label="Stimulus")
plt1.plot(tss, Vss, label="Membrance Potential")
plt1.legend()
plt1.grid(True)
plt1.set_title("Hodgkin-Huxley Neuron Action Potential Model -- CH3_7")

plt2.plot(tss, nss, label="n")
plt2.plot(tss, mss, label="m")
plt2.plot(tss, hss, label="h")
plt2.legend()
plt2.grid(True)
plt2.set_xlabel("time (ms)")

plot_filename = "ch3_7_Hodgkin_Huxley.png"
plt.savefig(plot_filename)
print(f"  figure {plot_filename} generated")
print(f"  DEBUG Max V:{max(Vss)} n:{max(nss)} m:{max(mss)} Min h:{min(hss)}")

