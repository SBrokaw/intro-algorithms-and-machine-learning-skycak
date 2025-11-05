# Skycak, J. (2021). Single-Variable Gradient Descent. 
# In Introduction to Algorithms and Machine Learning: 
# from Sorting to Strategic Agents. 
# https://justinmath.com/single-variable-gradient-descent/
import math

def next_guess( p, m, alpha ):
    return p - alpha * m 

def point_exercise0( p ):
    return p ** 2

def point_exercise1( p ):
    return p ** 2 + p + 1

def point_exercise2( p ):
    return p ** 3 - p ** 4 - p ** 2

def point_exercise3( p ):
    return math.sin(p) / (1 + p ** 2)

def point_exercise4( p ):
    return 3 * math.cos(p) + p ** 2 * math.exp(math.sin(p))

def slope_tangent_exercise0( p ):
    return 2 * p

def slope_tangent_exercise1( p ):
    return 2 * p + 1

def slope_tangent_exercise2( p ):
    return 3 * p ** 2 - 4 * p ** 3 - 2 * p

def slope_tangent_exercise3( p ):
    return ((1 + p**2) * math.cos(p) - 2 * p * math.sin(p)) / (1 + p**2)**2

def slope_tangent_exercise4( p ):
    return -3 * math.sin(p) + 2*p*math.exp(math.sin(p)) + p**2 * math.cos(p)*math.exp(math.sin(p))

def exercise0( alpha, trials ):
    print(' Exercise0 : f(x) = x^2 '.center(50, '='))
    output_mask = {0, 1, 2, 3, 25, 50, 100, 200, 300, 400}
    x_n = -1.0
    print('n    x_n       f\'(x_n)   α∙f\'(x_n) y_n')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    for n in range(trials):
        m = slope_tangent_exercise0( x_n )
        y_n = point_exercise0( x_n )
        if n in output_mask: print(f'{n:<3g} {x_n:< 6.6f} {m:< 7.6f} {alpha * m:< 9.6f} {y_n:< 8.6f}')

        x_n -= alpha * m

    return y_n

def exercise1( alpha, trials ):
    print('')
    print(' Exercise1 : f(x) = x^2 + x + 1 '.center(50, '='))
    output_mask = {0, 1, 2, 3, 25, 50, 100, 200, 300, 400}

    lowest_x = 1.0
    lowest_y = point_exercise1( lowest_x )
    initial_guesses = range(-50, 50) # range() only supports ints. Divide by 10 inside the for: loop
    for guess in initial_guesses:
        x_n = guess / 10
        y_n = point_exercise1( x_n )
        if y_n < lowest_y:
            lowest_x = x_n
            lowest_y = y_n
        #print(f'{guess} {x_n} {y_n:<.3f} < {lowest_y:<.3f} ? {lowest_x}')

    x_n = lowest_x
    print('n    x_n       f\'(x_n)   α∙f\'(x_n) y_n')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    for n in range(trials):
        m = slope_tangent_exercise1( x_n )
        y_n = point_exercise1( x_n )
        if n in output_mask: print(f'{n:<3g} {x_n:< 6.6f} {m:< 7.6f} {alpha * m:< 9.6f} {y_n:< 8.6f}')

        x_n -= alpha * m

    return y_n

def exercise2( alpha, trials ):
    print('')
    print(' Exercise2 : f(x) = x^3 - x^4 - x^2 '.center(50, '='))
    output_mask = {0, 1, 2, 3, 25, 50, 100, 200, 300, 400}

    lowest_x = 1.0
    lowest_y = point_exercise2( lowest_x )
    initial_guesses = range(-50, 50) # range() only supports ints. Divide by 10 inside the for: loop
    for guess in initial_guesses:
        x_n = guess / 10
        y_n = point_exercise2( x_n )
        if y_n < lowest_y:
            lowest_x = x_n
            lowest_y = y_n
        #print(f'{guess} {x_n} {y_n:<.3f} < {lowest_y:<.3f} ? {lowest_x}')

    x_n = lowest_x
    print('n    x_n       f\'(x_n)   α∙f\'(x_n) y_n')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    for n in range(trials):
        m = slope_tangent_exercise2( x_n )
        y_n = point_exercise2( x_n )
        if n in output_mask: print(f'{n:<3g} {x_n:< 6.6f} {m:< 7.6f} {alpha * m:< 9.6f} {y_n:< 8.6f}')

        x_n -= alpha * m

    return y_n

def exercise3( alpha, trials ):
    print('')
    print(' Exercise3 : f(x) = sin(x) / (1 + x^2) '.center(80, '='))
    output_mask = {0, 1, 2, 3, 25, 50, 100, 200, 300, 400}

    lowest_x = 1.0
    lowest_y = point_exercise3( lowest_x )
    initial_guesses = range(-50, 50) # range() only supports ints. Divide by 10 inside the for: loop
    for guess in initial_guesses:
        x_n = guess / 10
        y_n = point_exercise3( x_n )
        if y_n < lowest_y:
            lowest_x = x_n
            lowest_y = y_n
        #print(f'{guess} {x_n} {y_n:<.3f} < {lowest_y:<.3f} ? {lowest_x}')

    x_n = lowest_x
    print('n    x_n       f\'(x_n)   α∙f\'(x_n) y_n')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    for n in range(trials):
        m = slope_tangent_exercise3( x_n )
        y_n = point_exercise3( x_n )
        if n in output_mask: print(f'{n:<3g} {x_n:< 6.6f} {m:< 7.6f} {alpha * m:< 9.6f} {y_n:< 8.6f}')

        x_n -= alpha * m

    return y_n

def exercise4( alpha, trials ):
    print('')
    print(' Exercise4 : f(x) = 3·cos(x) + x^2·e^sin(x) '.center(80, '='))
    output_mask = {0, 1, 2, 3, 25, 50, 100, 200, 300, 400}

    lowest_x = 1.0
    lowest_y = point_exercise4( lowest_x )
    initial_guesses = range(-50, 50) # range() only supports ints. Divide by 10 inside the for: loop
    for guess in initial_guesses:
        x_n = guess / 10
        y_n = point_exercise4( x_n )
        if y_n < lowest_y:
            lowest_x = x_n
            lowest_y = y_n
        #print(f'{guess} {x_n} {y_n:<.3f} < {lowest_y:<.3f} ? {lowest_x}')

    x_n = lowest_x
    print('n    x_n       f\'(x_n)   α∙f\'(x_n) y_n')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    for n in range(trials):
        m = slope_tangent_exercise4( x_n )
        y_n = point_exercise4( x_n )
        if n in output_mask: print(f'{n:<3g} {x_n:< 6.6f} {m:< 7.6f} {alpha * m:< 9.6f} {y_n:< 8.6f}')

        x_n -= alpha * m

    return y_n

exercise0( 0.01, 401 )
exercise1( 0.01, 401 )
exercise3( 0.01, 401 )
exercise4( 0.01, 401 )