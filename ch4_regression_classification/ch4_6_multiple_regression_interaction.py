# Skycak, J. (2022). Multiple Regression and Interaction Terms. 
# In Introduction to Algorithms and Machine Learning: 
# from Sorting to Strategic Agents. 
# https://justinmath.com/multiple-regression-and-interaction-terms/
from math import log, exp
from random import random as rand

table_width = 95
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

def output_vector_prob3( data ):
    vals = [[-1 * log((5 / (y - 0.5)) - 1)] for (y,) in data]
    return Matrix(vals)

def coefficient_matrix_polynomial( order, data ):
    coeffs = []
    for d in data:
        coeffs += [[v ** exp for exp in range(order, 0, -1) for v in d] + [1]]

    # print(f"  coeffs:{coeffs}")
    return Matrix(coeffs)


def regression_string_prob1( p ):
    regression = f"y ≈ 5 / (1 + e^-({p.vals[0]:.2g}x + {p.vals[1]:.2g})) + 0.5"
    regression = regression.replace("+ -", "– ")
    return regression

def next_guess( v, gradient, alpha ):
    w = [v[i] - alpha * gradient[i] for i in range(len(v))]
    return w

def RSS_sigma_problem1( v, data ):
    rss = 0
    a1, a2, a3, b = v[0], v[1], v[2], v[3]
    for [x1, x2, x3, y] in data:
        z = a1 * x1 + a2 * x2 + a3 * x3 + b
        v = 1 + exp(-1 * z)
        u = 1 / v - y
        rss += u ** 2

    return rss


def RSS_sigma_problem2( v, data ):
    rss = 0
    [a1, a2, a3, a12, a13, a23, b] = v
    for [x1, x2, x3, y] in data:
        z = a1 * x1 + a2 * x2 + a3 * x3 + a12 * x1 * x2 + a13 * x1 * x3 + a23 * x2 * x3 + b
        v = 1 + exp(-1 * z)
        u = 1 / v - y
        rss += u ** 2

    return rss

def gradient_sigma_problem1( v, data ):
    da1, da2, da3, db = 0, 0, 0, 0
    a1, a2, a3, b = v[0], v[1], v[2], v[3]
    for [x1, x2, x3, y] in data:
        z = a1 * x1 + a2 * x2 + a3 * x3 + b
        v = 1 + exp(-1 * z)
        u = 1 / v - y
        common = 2 * u * exp(-1 * z) / (v ** 2)
        da1 += common * x1
        da2 += common * x2
        da3 += common * x3
        db += common 

    return [da1, da2, da3, db]


def gradient_sigma_problem2( v, data ):
    da1, da2, da3, da12, da13, da23, db = 0, 0, 0, 0, 0, 0, 0
    [a1, a2, a3, a12, a13, a23, b] = v
    for [x1, x2, x3, y] in data:
        z = a1 * x1 + a2 * x2 + a3 * x3 + a12 * x1 * x2 + a13 * x1 * x3 + a23 * x2 * x3 + b
        v = 1 + exp(-1 * z)
        u = 1 / v - y
        common = 2 * u * exp(-1 * z) / (v ** 2)
        da1 += common * x1
        da2 += common * x2
        da3 += common * x3
        da12 += common * x1 * x2
        da13 += common * x1 * x3
        da23 += common * x2 * x3
        db += common 

    return [da1, da2, da3, da12, da13, da23, db]

def sigma_problem1( alpha, trials, initial_guess ):
    output_mask = {0, 1, 2, 3, 50, 100, 500, 1000, 5000, 10000}
    data = [[0, 0, 0, 0.0],
            [1, 0, 0, 0.2],
            [2, 0, 0, 0.5],
            [0, 1, 0, 0.4],
            [0, 2, 0, 0.6],
            [0, 0, 1, 0.5],
            [0, 0, 2, 0.8],
            [1, 1, 0, 1.0],
            [1, 0, 1, 0.0],
            [0, 1, 1, 0.1]]
    x_n = initial_guess.copy()
    # print(f"  n    " + f"<a1_n, a2_n, a3_n, b_n>".center(col_width) + f"∇RSS(a1_n, a2_n, a3_n, b_n)".center(col_width) + f"RSS(a1_n, a2_n, a3_n, b_n)".center(col_width))
    # print(f''.center(table_width, '‾'))
    for n in range(trials):
        m = gradient_sigma_problem1( x_n, data )
        p = RSS_sigma_problem1( x_n, data )
        # if n in output_mask: 
        #     print(f"  {n}".ljust(7) 
        #           + f"<{x_n[0]:.3g}, {x_n[1]:.3g}, {x_n[2]:.3g}, {x_n[3]:.3g}>".center(col_width) 
        #           + f"<{m[0]:.3f}, {m[1]:.3f}, {m[2]:.3f}, {m[3]:.3f}>".center(col_width)
        #           + f"{p:.3f}".center(col_width))

        x_n = next_guess( x_n, m, alpha )

    return x_n + [p]

def sigma_problem2( alpha, trials, initial_guess ):
    output_mask = {0, 1, 2, 3, 50, 100, 500, 1000, 5000, 10000}
    data = [[0, 0, 0, 0.0],
            [1, 0, 0, 0.2],
            [2, 0, 0, 0.5],
            [0, 1, 0, 0.4],
            [0, 2, 0, 0.6],
            [0, 0, 1, 0.5],
            [0, 0, 2, 0.8],
            [1, 1, 0, 1.0],
            [1, 0, 1, 0.0],
            [0, 1, 1, 0.1]]
    x_n = initial_guess.copy()
    # print(f"  n    " + f"<a1_n, a2_n, a3_n, b_n>".center(col_width) + f"∇RSS(a1_n, a2_n, a3_n, b_n)".center(col_width) + f"RSS(a1_n, a2_n, a3_n, b_n)".center(col_width))
    # print(f''.center(table_width, '‾'))
    for n in range(trials):
        m = gradient_sigma_problem2( x_n, data )
        p = RSS_sigma_problem2( x_n, data )
        # if n in output_mask: 
        #     print(f"  {n}".ljust(7) 
        #           + f"<{x_n[0]:.3g}, {x_n[1]:.3g}, {x_n[2]:.3g}, {x_n[3]:.3g}>".center(col_width) 
        #           + f"<{m[0]:.3f}, {m[1]:.3f}, {m[2]:.3f}, {m[3]:.3f}>".center(col_width)
        #           + f"{p:.3f}".center(col_width))

        x_n = next_guess( x_n, m, alpha )

    return x_n + [p]


print(" Problem1 Sigma Notation: y ≈ 1 / (1 + e^-(a1∙x1 + a2∙x2 + a3∙x3 + b)) ".center(table_width, '='))
random_guesses = [[4 * rand() - 2 for i in range(4)] for j in range(40)]
random_guesses.append([0.79, 1.13, 0.75, -1.72])
digits = 4
rss_final = 999
for starting_point in random_guesses:
    a1, a2, a3, b, rss = sigma_problem1( 0.001, 10001, starting_point)
    if rss < rss_final:
        a1_final, a2_final, a3_final, b_final, rss_final = a1, a2, a3, b, rss

print(f"  Final Regression (a1, a2, a3, b)  RSS:{rss_final:.{digits}g}")
print(f"    ({a1_final:.{digits}g}, {a2_final:.{digits}g}, {a3_final:.{digits}g}, {b_final:.{digits}g})") 
# print(f"  {regression_string_prob1(Matrix([[a],[b]]))}\n")
print()


print(" Problem2 Sigma Notation: y ≈ 1 / (1 + e^-(a1∙x1 + a2∙x2 + a3∙x3 + a12∙x1∙x2 + a13∙x1∙x3 + a23∙x2∙x3 + b)) ".center(table_width, '='))
random_guesses = [[4 * rand() - 2 for i in range(7)] for j in range(40)]
random_guesses.append([1.02, 1.34, 1.91, 3.82, -4.82, -3.34, -2.11])
rss_final = 999
for starting_point in random_guesses:
    a1, a2, a3, a12, a13, a23, b, rss = sigma_problem2( 0.001, 10001, starting_point)
    if rss < rss_final:
        a1_final, a2_final, a3_final, a12_final, a13_final, a23_final, b_final, rss_final = a1, a2, a3, a12, a13, a23, b, rss

print(f"  Final Regression (a1, a2, a3, a12, a13, a23, b)  RSS:{rss_final}")
print(f"    ({a1_final:.{digits}g}, {a2_final:.{digits}g}, {a3_final:.{digits}g}, {a12_final:.{digits}g}, {a13_final:.{digits}g}, {a23_final:.{digits}g}, {b_final:.{digits}g})") 
# print(f"  {regression_string_prob1(Matrix([[a],[b]]))}\n")
print()
