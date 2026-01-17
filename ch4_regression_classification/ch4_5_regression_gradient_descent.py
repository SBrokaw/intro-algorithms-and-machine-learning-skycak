# Skycak, J. (2022). Regression via Gradient Descent.
# In Introduction to Algorithms and Machine Learning: 
# from Sorting to Strategic Agents. 
# https://justinmath.com/regression-via-gradient-descent/
from math import log

const_PI = 3.141592654
const_e = 2.718281828
table_width = 90
col_width = table_width // 3

def dot_product( arr1, arr2 ):
    if len(arr1) != len(arr2):
        print(f'ERROR! Dot product dimension mismatch. {len(arr1)} != {len(arr2)}')
        return 0

    product = 0.0
    for i in range(len(arr1)):
        product += arr1[i] * arr2[i]

    return product

class Matrix:
    def __init__(self, rows):
        self.data = [r for r in rows]
    
    @property
    def num_rows(self): return len(self.data)

    @property
    def num_cols(self): return len(self.data[0])

    @property
    def is_empty(self): return True if len(self.data[0]) == 0 else False

    @property
    def vals(self): return [c for r in self.data for c in r]

    def show(self):
        for r in self.data:
            print('[ ', end = '')
            for i in range(len(r)):
                end_char = '' if i == len(r) - 1 else ', '
                print(f'{r[i]: .3g} {end_char}', end = '')
            print(']')
        return 0

    def print(self):
        return self.show()

    def disp(self):
        return self.show()
    
    def display(self):
        return self.show()

    # return 0-indexed column j
    def col(self, j):
        if j < 0 or j > self.num_cols - 1: return None
        return [self.data[k][j] for k in range(self.num_rows)]

    # return 0-indexed row i
    def row(self, i):
        if i < 0 or i > self.num_rows - 1: return None
        return self.data[i]

    def transpose(self):
        rows = len(self.data)
        columns = len(self.data[0])
        transposed = [[0] * rows for c in range(columns)]
        for i in range(rows):
            for j in range(columns):
                transposed[j][i] = self.data[i][j]

        return Matrix(transposed)

    def add(self, m):
        if self.num_rows != m.num_rows or self.num_cols != m.num_cols:
            print(f'ERROR! Matrix add dimension mismatch. [{self.num_rows}, {self.num_cols}] != [{m.num_rows}, {m.num_cols}]')
            return self

        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.data[i][j] += m.data[i][j]

        return self

    def subtract(self, m):
        if self.num_rows != m.num_rows or self.num_cols != m.num_cols:
            print(f'ERROR! Matrix subtract dimension mismatch. [{self.num_rows}, {self.num_cols}] != [{m.num_rows}, {m.num_cols}]')
            return self

        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.data[i][j] -= m.data[i][j]

        return self

    def scalar_multiply(self, k):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.data[i][j] *= k

        return self

    # Matrix Multiply returns self ∙ m
    def matrix_multiply(self, m):
        # print(f"Matrix Multiply Debug")
        # self.print()
        # print()
        # m.print()
        # print()

        if self.num_cols != m.num_rows:
            print(f'ERROR! Matrix multiply dimension mismatch. [{self.num_rows}, {self.num_cols}] != [{m.num_rows}, {m.num_cols}]')
            return self

        product = [[0.0] * m.num_cols for c in range(self.num_rows)]
        # print(f"MM Debug product:{product}")
        for i in range(self.num_rows):
            for j in range(m.num_cols):
                row = self.data[i]
                col = [m.data[k][j] for k in range(self.num_cols)]
                # print(f'row {row}\tcol {col}')
                product[i][j] = dot_product(row, col) 

        return Matrix(product)


    def inverse(self):
        if self.data == [[]]: 
            print(f'ERROR! Inverse does not exist for matrix {self.data}')
            return Matrix([[]])
        if self.num_cols != self.num_rows: 
            print(f'ERROR! Inverse does not exist for non-square {self.num_rows}x{self.num_cols} matrix ')
            return Matrix([[]])

        rref = [r[:] for r in self.data]
        for idx, r in enumerate(rref):
            augment = [0] * self.num_cols
            augment[idx] = 1
            rref[idx] += augment

        row_idx = 0
        pivot_idx = 0
        # matrix_print(rref, 2)
        for i in range(self.num_cols):
            # if pivot row exists for column:
            col_i = [rref[u][i] for u in range(self.num_rows)]
            pivot_idx = next((j for j, v in enumerate(col_i) if v != 0 and j >= row_idx), -1)
            # print(f'  swap? pivot_idx:{pivot_idx} row_idx:{row_idx}'); matrix_print(rref, 4)
            if pivot_idx >= 0:
                # if pivot row does not match current row_index:
                if pivot_idx != row_idx:
                    # swap current row with pivot row
                    # (so that it matches)
                    temp_row = rref[row_idx]
                    rref[row_idx] = rref[pivot_idx]
                    rref[pivot_idx] = temp_row
                    # print(f'  swapped {row_idx},{pivot_idx}'); matrix_print(rref, 4)

                # divide pivot row (so that first nonzero entry is 1)
                scalar = rref[row_idx][i]
                if scalar != 0 and scalar != 1:
                    rref[row_idx] = [k / scalar for k in rref[row_idx]]
                    # print(f'  scaled r{row_idx} 1/{scalar}'); matrix_print(rref, 4)

                # clear entries below and above pivot entry
                # (by subtracting multiples of pivot row)
                clr_rows = [u for u in range(len(self.col(i))) if u != row_idx and rref[u][i] != 0]
                # print(f'  clr_rows:{clr_rows} i:{i} row_idx:{row_idx}'); matrix_print(rref, 4)
                for clr in clr_rows:
                    if rref[row_idx][i] == 0: continue
                    k = rref[clr][i] / rref[row_idx][i]
                    rref[clr] = [rref[clr][u] - k * rref[row_idx][u] for u in range(len(rref[clr]))]
                    # print(f'  cleared r{clr} - {k}∙r{row_idx}'); matrix_print(rref, 4)

                row_idx += 1

            else: # no pivot -> singular matrix -> no inverse exists
                print(f'ERROR! Inverse does not exist for singular matrix.')
                return Matrix([[]])

        inverse = [r[self.num_cols:] for r in rref]
        return Matrix(inverse)
    

    def determinant(self):
        if self.num_cols != self.num_rows:
            print(f'ERROR! Determinant dimension mismatch. {self.num_rows} != {self.num_cols}')
            return None

        det =  self.determinant_loop(self)
        return det
        
    def determinant_loop(self, m):
        det = 0

        #base case when matrix is 1x1
        if m.num_cols == 1 and m.num_rows == 1:
            return m.data[0][0]

        for i in range(m.num_cols):
            sub_m = Matrix([[m.data[j][k] for k in range(m.num_cols) if k != i] for j in range(m.num_cols) if j != 0])
            # print('  sub_m'); print('  ',end=''); sub_m.print()
            det += (-1)**i * m.data[0][i] * self.determinant_loop(sub_m)
            # print(f'  det = {det}')

        return det
    

    def pseudoinverse(self):
        X = self
        X_T = X.transpose()
        X_T_X= X_T.matrix_multiply(X)
        X_T_X_inv= X_T_X.inverse()
        X_T_X_inv_X_T = X_T_X_inv.matrix_multiply(X_T)

        return X_T_X_inv

def output_vector_polynomial( data ):
    vals = [[y] for (y,) in data]
    return Matrix(vals)

def coefficient_matrix_polynomial( order, data ):
    coeffs = []
    for d in data:
        coeffs += [[v ** exp for exp in range(order, 0, -1) for v in d] + [1]]

    # print(f"  coeffs:{coeffs}")
    return Matrix(coeffs)

# linear, quadratic, and <n> order polynomial regression string for up to 2 input variables x and y
def regression_string_polynomial( order, p ):
    sig_figs = 4
    regression_eq = ""
    num_input_vars = (len(p.vals) - 1) // order
    input_vars = ['x', 'y', 'z'][0:num_input_vars]
    output_var = ['x', 'y', 'z'][num_input_vars]
    regression_eq += f"{output_var} ≈ "
    exponents = ['', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸'][0:order]
    exponents.reverse()
    p_idx = 0
    for m in exponents:
        for t in input_vars:
            regression_eq += f"{p.vals[p_idx]:.{sig_figs}g}{t}{m} + "
            p_idx += 1
    regression_eq += f"{p.vals[-1]:.{sig_figs}g}"
    regression_eq = regression_eq.replace("+ -", "– ")
    regression_eq = regression_eq.replace("-", "–")

    return regression_eq

def next_guess( v, gradient, alpha ):
    w = [v[i] - alpha * gradient[i] for i in range(len(v))]
    return w

def point_problem1( v ):
    a, b = v[0], v[1]
    return (a * 0.001 ** b - 0.01) ** 2 + (a * 2 ** b - 4) ** 2 + (a * 3 ** b - 9) ** 2

def RSS_sigma_problem1( v, data ):
    rss = 0
    a, b = v[0], v[1]
    for (x, y) in data:
        rss += (a * x ** b - y) ** 2

    return rss

def RSS_sigma_problem2( v, data ):
    rss = 0
    a, b, c = v[0], v[1], v[2]
    for (x, y) in data:
        rss += (a * x ** 2 + b * x + c - y) ** 2

    return rss


def gradient_problem1( x_n ):
    a, b = x_n[0], x_n[1]
    return [
        2 * (a * (0.001) ** b - 0.01) * 0.001 ** b 
            + 2 * (a * 2 ** b - 4) * 2 ** b 
            + 2 * (a * 3 ** b - 9) * 3 ** b,
        2 * (a * 0.001 ** b - 0.01) * (a * 0.001 ** b * log(0.001)) 
            + 2 * (a * 2 ** b - 4) * (a * 2 ** b * log(2))
            + 2 * (a * 3 ** b - 9) * (a * 3 ** b * log(3))
    ]

def gradient_sigma_problem1( v, data ):
    da = 0
    db = 0
    a, b = v[0], v[1]
    for (x, y) in data:
        common = 2 * (a * x ** b - y) * x ** b
        da += common
        db += common * a * log(x)

    return [da, db]


def gradient_sigma_problem2( v, data ):
    da = 0
    db = 0
    dc = 0
    a, b, c = v[0], v[1], v[2]
    for (x, y) in data:
        common = 2 * (a * x ** 2 + b * x + c - y)
        da += common * x ** 2
        db += common * x
        dc += common

    return [da, db, dc]


def problem1( alpha, trials ):
    print(' Problem1 : Power Regression y = a∙x^b '.center(table_width, '='))
    output_mask = {0, 1, 2, 3, 50, 100, 500, 1000, 5000, 10000}
    x_n = [1, 1]
    print(f"  n    " + f"<a_n, b_n>".center(col_width) + f"∇RSS(a_n, b_n)".center(col_width) + f"RSS(a_n, b_n)".center(col_width))
    print(f''.center(table_width, '‾'))
    for n in range(trials):
        m = gradient_problem1( x_n )
        p = point_problem1( x_n )
        if n in output_mask: 
            print(f"  {n}".ljust(7) 
                  + f"<{x_n[0]:.6g}, {x_n[1]:.6g}>".center(col_width) 
                  + f"<{m[0]:6.6f}, {m[1]:6.6f}>".center(col_width)
                  + f"{p:.6f}".center(col_width))

        x_n = next_guess( x_n, m, alpha )

    return x_n

def sigma_problem1( alpha, trials ):
    print(' Problem1 Sigma Notation: Power Regression y = a∙x^b '.center(table_width, '='))
    output_mask = {0, 1, 2, 3, 50, 100, 500, 1000, 5000, 10000}
    data = [(0.001, 0.01), (2, 4), (3, 9)]
    x_n = [1, 1]
    print(f"  n    " + f"<a_n, b_n>".center(col_width) + f"∇RSS(a_n, b_n)".center(col_width) + f"RSS(a_n, b_n)".center(col_width))
    print(f''.center(table_width, '‾'))
    for n in range(trials):
        m = gradient_sigma_problem1( x_n, data )
        p = RSS_sigma_problem1( x_n, data )
        if n in output_mask: 
            print(f"  {n}".ljust(7) 
                  + f"<{x_n[0]:.6g}, {x_n[1]:.6g}>".center(col_width) 
                  + f"<{m[0]:6.6f}, {m[1]:6.6f}>".center(col_width)
                  + f"{p:.6f}".center(col_width))

        x_n = next_guess( x_n, m, alpha )

    return x_n


def sigma_problem2( alpha, trials ):
    print(' Problem2 Sigma Notation: Polynomial Regression y = a∙x² + b∙x + c '.center(table_width, '='))
    output_mask = {0, 1, 2, 3, 50, 100, 500, 1000, 5000, 10000}
    data = [(0.001, 0.01), (2, 4), (3, 9)]
    x_n = [1, 1, 1]
    print(f"  n    " + f"<a_n, b_n, c_n>".center(col_width) + f"∇RSS(a_n, b_n, c_n)".center(col_width) + f"RSS(a_n, b_n, c_n)".center(col_width))
    print(f''.center(table_width, '‾'))
    for n in range(trials):
        m = gradient_sigma_problem2( x_n, data )
        p = RSS_sigma_problem2( x_n, data )
        if n in output_mask: 
            print(f"  {n}".ljust(7) 
                  + f"<{x_n[0]:.3g}, {x_n[1]:.3g}, {x_n[2]:.3g}>".center(col_width) 
                  + f"<{m[0]:.3f}, {m[1]:.3f}, {m[2]:.3f}>".center(col_width)
                  + f"{p:.6f}".center(col_width))

        x_n = next_guess( x_n, m, alpha )

    return x_n

def pseudoinverse_problem2():
    print(" Problem2 Pseudoinverse: y = a∙x² + b∙x + c ".center(table_width, '='))
    data = [(0.001, 0.01), (2, 4), (3, 9)]
    output_vector_eq = output_vector_polynomial
    coefficient_matrix_eq = coefficient_matrix_polynomial
    regression_string_eq = regression_string_polynomial
    order = 2
    ## Problem Start
    print(f"  coeff_eq:{coefficient_matrix_eq.__name__} data:{data}")
    print(f"".center(table_width, '—'))
    x = [list(point[:-1]) for point in data]
    y = output_vector_eq([[point[-1]] for point in data])
    X = coefficient_matrix_eq(order, x)

    ## Calculate and Print Regression
    X_inv = X.pseudoinverse()
    X_T = X.transpose()
    X_T_y = X_T.matrix_multiply(y)
    p = X_inv.matrix_multiply(X_T_y)
    print(f"  p:{p.vals}")
    print(f"  {regression_string_eq(order, p)}")
    


a, b = problem1( 0.001, 10001)
print(f"  Final Regression (a, b) = ({a:.6g}, {b:.6g})\n")
a, b = sigma_problem1( 0.001, 10001)
print(f"  Final Regression (a, b) = ({a:.6g}, {b:.6g})\n")
a, b, c = sigma_problem2( 0.001, 10001)
print(f"  Final Regression (a, b, c) = ({a:.6g}, {b:.6g}, {c:.6g})")
print(f"  {regression_string_polynomial(2, Matrix([[a],[b],[c]]))}\n")
pseudoinverse_problem2()
