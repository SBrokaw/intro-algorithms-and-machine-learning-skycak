# Skycak, J. (2022). Regression via Gradient Descent.
# In Introduction to Algorithms and Machine Learning: 
# from Sorting to Strategic Agents. 
# https://justinmath.com/regression-via-gradient-descent/
from math import log

const_PI = 3.141592654
const_e = 2.718281828
table_width = 90
col_width = table_width // 3

def next_guess( v, gradient, alpha ):
    w = [v[i] - alpha * gradient[i] for i in range(len(v))]
    return w

def point_exercise0( v ):
    a, b = v[0], v[1]
    return (a * 0.001 ** b - 0.01) ** 2 + (a * 2 ** b - 4) ** 2 + (a * 3 ** b - 9) ** 2

def gradient_exercise0( x_n ):
    a, b = x_n[0], x_n[1]
    return [
        2 * (a * (0.001) ** b - 0.01) * 0.001 ** b 
            + 2 * (a * 2 ** b - 4) * 2 ** b 
            + 2 * (a * 3 ** b - 9) * 3 ** b,
        2 * (a * 0.001 ** b - 0.01) * (a * 0.001 ** b * log(0.001)) 
            + 2 * (a * 2 ** b - 4) * (a * 2 ** b * log(2))
            + 2 * (a * 3 ** b - 9) * (a * 3 ** b * log(3))
    ]

def exercise0( alpha, trials ):
    print(' Exercise0 : Power Regression y = a∙x^b '.center(table_width, '='))
    output_mask = {0, 1, 2, 3, 50, 100, 500, 1000, 5000, 10000}
    x_n = [1, 1]
    print(f"  n    " + f"x_n".center(col_width) + f"∇f\'(x_n)".center(col_width) + f"f(x_n)".center(col_width))
    print(f''.center(table_width, '‾'))
    for n in range(trials):
        m = gradient_exercise0( x_n )
        p = point_exercise0( x_n )
        if n in output_mask: 
            print(f"  {n}".ljust(7) 
                  + f"<{x_n[0]:.6g}, {x_n[1]:.6g}>".center(col_width) 
                  + f"<{m[0]:6.6f}, {m[1]:6.6f}>".center(col_width)
                  + f"{p:.6f}".center(col_width))

        x_n = next_guess( x_n, m, alpha )

    return p


exercise0( 0.001, 10001)
