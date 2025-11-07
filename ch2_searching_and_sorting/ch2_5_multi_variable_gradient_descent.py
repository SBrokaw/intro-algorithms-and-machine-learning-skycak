# Skycak, J. (2021). Multivariable Gradient Descent. In Introduction to 
# Algorithms and Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/multivariable-gradient-descent/
import math

const_PI = 3.141592654
const_e = 2.718281828

def factorial( n ):
    sum = 1
    for i in range(n):
        sum *= (n - i)

    return sum

# Maclaurin expansion 
def sin( p ):
    sum = 0
    for n in range(20):
        sum += (-1) ** n * p ** (2 * n + 1) / factorial(2 * n + 1)

    return sum

# Maclaurin expansion 
def cos( p ):
    sum = 0
    for n in range(20):
        sum += (-1) ** n * p ** (2 * n) / factorial(2 * n)

    return sum

def next_guess( v, gradient, alpha ):
    w = [v[i] - alpha * gradient[i] for i in range(len(v))]
    return w

def point_exercise0( v ):
    return v[0] * sin(v[1]) + v[0] ** 2

def gradient_exercise0( x_n ):
    return [sin(x_n[1]) + 2 * x_n[0], x_n[0] * cos(x_n[1])]

def point_exercise1( v ):
    return (v[0] - 1) ** 2 + 3 * v[1] ** 2

def gradient_exercise1( v ):
    return [2 * (v[0] - 1), 6 * v[1]]

def point_exercise2( v ):
    return v[1] ** 2 + v[1] * cos(v[0])

def gradient_exercise2( v ):
    return [-1 * v[1] * sin(v[0]), 2 * v[1] + cos(v[0])]

def point_exercise3( v ):
    return (v[0] - 1) ** 2 + 3 * (v[1] - 2) ** 2 + 4 * (v[2] + 1) ** 2

def gradient_exercise3( v ):
    return [2 * (v[0] - 1), 6 * (v[1] - 2), 8 * (v[2] + 1)]

def point_exercise4( v ):
    x = v[0]; y = v[1]; z = v[2]
    return x ** 2 + 3 * y ** 2 + 4 * z ** 2 + math.cos(x*y*z)

def gradient_exercise4( v ):
    x = v[0]; y = v[1]; z = v[2]
    return [2 * x - y * z * math.cos(x*y*z), 6 * y + x * z * math.cos(x*y*z), 8 * z + x * y * math.cos(x*y*z)]

def exercise0( alpha, trials ):
    print(' Exercise0 : f(x,y) = x∙sin(y) + x² '.center(60, '='))
    output_mask = {0, 1, 2, 3, 25, 50, 100, 250, 500, 1000, 2000, 3000}
    x_n = [1, 2]
    print('n     x_n                   ∇f\'(x_n)             f(x_n)')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    for n in range(trials):
        m = gradient_exercise0( x_n )
        p = point_exercise0( x_n )
        if n in output_mask: print(f'{n:<4g} <{x_n[0]:<6.6f}, {x_n[1]:<6.6f}> <{m[0]:<6.6f}, {m[1]:<6.6f}> {p:<6.6f}')

        x_n = next_guess( x_n, m, alpha )

    return p

def exercise1( alpha, trials ):
    print('')
    print(' Exercise1 : f(x,y) = (x-1)² + 3y² '.center(60, '='))
    output_mask = {0, 1, 2, 3, 25, 50, 100, 250, 500, 1000, 2000, 3000}

    lowest_v = [1, 2]
    lowest_w = point_exercise1(lowest_v)
    for i in range(-50, 50):
        for j in range(-50, 50):
            v = [i / 10, j / 10]
            w = point_exercise1(v)
            if w < lowest_w:
                lowest_v = v
                lowest_w = w
                #print(f'[{v[0]:< 3.2f}, {v[1]:< 3.2f}] {w:<.3f}')

    v = lowest_v
    print('n     x_n                   ∇f\'(x_n)             f(x_n)')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    for n in range(trials):
        m = gradient_exercise1( v )
        w = point_exercise1( v )
        if n in output_mask: print(f'{n:<4g} <{v[0]:<6.6f}, {v[1]:<6.6f}> <{m[0]:<6.6f}, {m[1]:<6.6f}> {w:<6.6f}')

        v = next_guess( v, m, alpha )

    return w

def exercise2( alpha, trials ):
    print('')
    print(' Exercise2 : f(x,y) = y² + x∙cos(x) '.center(60, '='))
    output_mask = {0, 1, 2, 3, 25, 50, 100, 250, 500, 1000, 2000, 3000}

    lowest_v = [1, 2]
    lowest_w = point_exercise2(lowest_v)
    for i in range(-50, 50):
        for j in range(-50, 50):
            v = [i / 10, j / 10]
            w = point_exercise2(v)
            if w < lowest_w:
                lowest_v = v
                lowest_w = w
                #print(f'[{v[0]:< 3.2f}, {v[1]:< 3.2f}] {w:<.3f}')

    v = lowest_v
    print('n     x_n                   ∇f\'(x_n)             f(x_n)')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    for n in range(trials):
        m = gradient_exercise2( v )
        w = point_exercise2( v )
        if n in output_mask: print(f'{n:<4g} <{v[0]:<6.6f}, {v[1]:<6.6f}> <{m[0]:<6.6f}, {m[1]:<6.6f}> {w:<6.6f}')

        v = next_guess( v, m, alpha )

    return w

def exercise3( alpha, trials ):
    print('')
    print(' Exercise3 : f(x,y,z) = (x-1)² + 3(y-2)² + 4(z+1)² '.center(60, '='))
    output_mask = {0, 1, 2, 3, 25, 50, 100, 250, 500, 1000, 2000, 3000}

    lowest_v = [1, 2, 0]
    lowest_w = point_exercise3(lowest_v)
    for i in range(-50, 50):
        for j in range(-50, 50):
            for k in range(-50, 50):
                v = [i / 10, j / 10, k / 10]
                w = point_exercise3(v)
                if w < lowest_w:
                    lowest_v = v
                    lowest_w = w
                    #print(f'[{v[0]:< 3.2f}, {v[1]:< 3.2f}] {w:<.3f}')

    v = lowest_v
    print('n     x_n                   ∇f\'(x_n)             f(x_n)')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    for n in range(trials):
        m = gradient_exercise3( v )
        w = point_exercise3( v )
        if n in output_mask: print(f'{n:<4g} <{v[0]:<4.3f}, {v[1]:<4.3f}, {v[2]:<4.3f}> '
                                   f'<{m[0]:<4.3f}, {m[1]:<4.3f}, {m[2]:<4.3f}> '
                                   f'{w:<6.6f}')

        v = next_guess( v, m, alpha )

    return w

def exercise4( alpha, trials ):
    print('')
    print(' Exercise4 : f(x,y,z) = x² + 3y² + 4z² + cos(xyz) '.center(60, '='))
    output_mask = {0, 1, 2, 3, 25, 50, 100, 250, 500, 1000, 2000, 3000}

    lowest_v = [1, 2, 0]
    lowest_w = point_exercise4(lowest_v)
    for i in range(-50, 50):
        for j in range(-50, 50):
            for k in range(-50, 50):
                v = [i / 10, j / 10, k / 10]
                w = point_exercise4(v)
                if w < lowest_w:
                    lowest_v = v
                    lowest_w = w
                    #print(f'[{v[0]:< 3.2f}, {v[1]:< 3.2f}, {v[2]:< 3.2f}] {w:<.3f}')

    v = lowest_v
    print('n     x_n                   ∇f\'(x_n)             f(x_n)')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    for n in range(trials):
        m = gradient_exercise4( v )
        w = point_exercise4( v )
        if n in output_mask: print(f'{n:<4g} <{v[0]:<4.3f}, {v[1]:<4.3f}, {v[2]:<4.3f}> '
                                   f'<{m[0]:<4.3f}, {m[1]:<4.3f}, {m[2]:<4.3f}> '
                                   f'{w:<6.6f}')

        v = next_guess( v, m, alpha )

    return w




exercise0( 0.01, 3001)
exercise1( 0.01, 3001)
exercise2( 0.01, 3001)
exercise3( 0.01, 3001)
exercise4( 0.01, 3001)
