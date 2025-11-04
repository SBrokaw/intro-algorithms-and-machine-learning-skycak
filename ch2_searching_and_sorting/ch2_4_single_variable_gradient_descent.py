# Skycak, J. (2021). Single-Variable Gradient Descent. 
# In Introduction to Algorithms and Machine Learning: 
# from Sorting to Strategic Agents. 
# https://justinmath.com/single-variable-gradient-descent/
import math

def next_guess( p, m, alpha ):
    return p - alpha * m 

def slope_tangent_exercise0( p ):
    return 2 * p

def slope_tangent_exercise1( p ):
    return 2 * p + 1

def slope_tangent_exercise2( p ):
    return 3 * p ** 2 - 4 * p ** 3 - 2 * p

def slope_tangent_exercise3( p ):
    return 0

def exercise0( alpha, trials ):
    output_mask = {1, 2, 3, 25, 50, 100, 200, 300, 400}
    initial_guess = 1.0
    print('n   x_n       f\'(x_n)  α∙f\'(x_n)')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    for n in range(trials):
        if n+1 in output_mask: print(f'{n+1:<4g}')

    return 0

exercise0( 0.01, 400 )