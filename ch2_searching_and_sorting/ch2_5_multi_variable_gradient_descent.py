# Skycak, J. (2021). Multivariable Gradient Descent. In Introduction to 
# Algorithms and Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/multivariable-gradient-descent/

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
    return [v[0] - alpha * gradient[0], v[1] - alpha * gradient[1]]

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
                print(f'[{v[0]:< 3.2f}, {v[1]:< 3.2f}] {w:<.3f}')

    v = lowest_v
    print('n     x_n                   ∇f\'(x_n)             f(x_n)')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    for n in range(trials):
        m = gradient_exercise2( v )
        w = point_exercise2( v )
        if n in output_mask: print(f'{n:<4g} <{v[0]:<6.6f}, {v[1]:<6.6f}> <{m[0]:<6.6f}, {m[1]:<6.6f}> {w:<6.6f}')

        v = next_guess( v, m, alpha )

    return w


exercise0( 0.01, 3001)
exercise1( 0.01, 3001)
exercise2( 0.01, 3001)
