# Skycak, J. (2021). Estimating Roots via Bisection Search and Newton-Raphson Method. 
# In Introduction to Algorithms and Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/estimating-roots-via-bisection-search-and-newton-raphson-method/


# calculates the x^(1/y) within precision
def calc_root_bisection(x, y, precision):
    if x <= 0 or y <= 0: return 0
    a = 0.0                # lower bound
    b = float(x)           # upper bound
    c = float((b - a) / 2) # midpoint
    err = float(abs(precision)) # error tolerance

    print('x    y    a     b     c     b-c    trial')
    print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    trial = c ** y - x
    while( abs(trial) > err ):
        trial = c ** y - x
        print(f'{x:<4} {y:<4} {a:<5.3g} {b:<5.3g} {c:<5.3g} {b-c:<5.3g} {trial:<4.3g}')
        if trial > (0 + err): b = c
        elif trial < (0 - err): a = c

        c = (b + a) / 2 # update midpoint

    print(f'[{a:.7g}, {c:.7g}, {b:.7g}], {y}√{x} = {c:.7g}')
    return c


# slope of tangent of f^(-1)(x^(1/y)) at point p
# ex. 3√2,  f(x) = x^3 - 2, f'(x) = 3x^2
def slope_tangent_inverse(x, y, p):
    return y * p ** (y-1)


# y value of f^-1(x^(1/y)) at point p
# ex. 3√2,  f(x) = x^3 - 2, f'(x) = 3x^2
def inverse_point(x, y, p):
    return p ** y - x


# x value of root of tangent line y - y0 = m(x - x0)
def root_tangent(m, x0, y0):
    return ((-1 * y0) / m ) + x0


# Newton-Raphson calculates the x^(1/y) within precision
def calc_root_nr(x, y, precision):
    if x <= 0 or y <= 0: return 0
    guess = float(x)
    err = float(abs(precision)) # error tolerance

    print('x    y    guess m     x0    y0     trial_b')
    print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    x0 = guess
    y0 = inverse_point( x, y, guess )
    m = slope_tangent_inverse( x, y, guess )
    trial_a = 0.0
    trial_b = root_tangent( m, x0, y0 )
    for i in range(3): #TODO: implement precision logic here -- while( trial_b.decimals < precision.decimals )
        print(f'{x:<4} {y:<4} {guess:<5.3g} {m:<5.3g} {x0:<5.3g} {y0:<5.3g} {trial_b:<4.3g}')
        return trial_b



calc_root_bisection( 2, 3, 0.05 )
calc_root_bisection( 2, 3, 0.005 )
calc_root_bisection( 2, 3, 0.0005 )
calc_root_bisection( 2, 3, 0.0000001 )
calc_root_nr( 2, 3, 0.001 )