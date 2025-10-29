# Skycak, J. (2021). Estimating Roots via Bisection Search and Newton-Raphson Method. 
# In Introduction to Algorithms and Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/estimating-roots-via-bisection-search-and-newton-raphson-method/


# calculates the x^(1/y) within precision
def calc_root_bisection(x, y, precision):
    a = 0.0                # lower bound
    b = float(x)           # upper bound
    c = float((b - a) / 2) # midpoint
    err = float(abs(precision)) # error tolerance

    print('x    y    a     b     c     b-c    trial')
    print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    while( b - c > err ):
        trial = c ** y - x
        print(f'{x:<4} {y:<4} {a:<5.3g} {b:<5.3g} {c:<5.3g} {b-c:<5.3g} {trial:<4.3g}')
        if trial > (0 + err): b = c
        elif trial < (0 - err): a = c

        c = (b - a) / 2 # update midpoint

    print(f'[{a:.5g}, {c:.5g}, {b:.5g}], {y}√{x} = {trial:.5g}')
    return trial

calc_root_bisection( 2, 3, 0.05 )