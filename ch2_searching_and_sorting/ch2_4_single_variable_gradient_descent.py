# Skycak, J. (2021). Single-Variable Gradient Descent. 
# In Introduction to Algorithms and Machine Learning: 
# from Sorting to Strategic Agents. 
# https://justinmath.com/single-variable-gradient-descent/
import math

def next_guess( p, m, alpha ):
    return p - alpha * m 

def point_exercise0( p ):
    return p ** 2

def slope_tangent_exercise0( p ):
    return 2 * p

def slope_tangent_exercise1( p ):
    return 2 * p + 1

def slope_tangent_exercise2( p ):
    return 3 * p ** 2 - 4 * p ** 3 - 2 * p

def slope_tangent_exercise3( p ):
    return 0

def exercise0( alpha, trials ):
    output_mask = {0, 1, 2, 3, 25, 50, 100, 200, 300, 400}
    x_n = 1.0
    print('n   x_n      f\'(x_n)  α∙f\'(x_n) y_n')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    for n in range(trials):
        m = slope_tangent_exercise0( x_n )
        y_n = point_exercise0( x_n )
        if n in output_mask: print(f'{n:<3g} {x_n:<6.6f} {m:<7.6f} {alpha * m:<9.6f} {y_n:<8.6f}')

        x_n -= alpha * m

    return y_n

exercise0( 0.01, 401 )