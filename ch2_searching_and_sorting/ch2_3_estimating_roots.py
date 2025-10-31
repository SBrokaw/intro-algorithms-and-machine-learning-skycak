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

calc_root_bisection( 2, 3, 0.05 )
calc_root_bisection( 2, 3, 0.005 )
calc_root_bisection( 2, 3, 0.0005 )
calc_root_bisection( 2, 3, 0.0000001 )