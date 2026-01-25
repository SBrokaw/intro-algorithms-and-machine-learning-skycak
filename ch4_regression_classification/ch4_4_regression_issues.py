# Skycak, J. (2022). Overfitting, Underfitting, Cross-Validation, and the Bias-Variance Tradeoff.
# In Introduction to Algorithms and Machine Learning: 
# from Sorting to Strategic Agents. 
# https://justinmath.com/linear-polynomial-and-multiple-linear-regression-via-pseudoinverse/

import numpy as np
from math import sin, sqrt, log, cbrt, exp

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


def coefficient_matrix_polynomial( order, data ):
    coeffs = []
    for d in data:
        coeffs += [[v ** exp for exp in range(order, 0, -1) for v in d] + [1]]

    # print(f"  coeffs:{coeffs}")
    return Matrix(coeffs)

def power_regression_output_vector( data ):
    vals = [[log(y)] for (y,) in data]
    return Matrix(vals)

def output_vector_polynomial( data ):
    vals = [[y] for (y,) in data]
    return Matrix(vals)

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

def power_regression_string( p ):
    return f"y ≈ {exp(p.vals[0]):.2g}x^{p.vals[1]:.2g}"

def exponent_regression_string( p ):
    return f"y ≈ {exp(p.vals[0]):.2g}∙{exp(p.vals[1]):.2g}^x"

def regression_string_ex1( order, p ):
    return regression_string_polynomial(order, p)

def predicted_val_polynomial( p, x ):
    exponents = [e for e in range(len(p.vals) - 1, -1, -1)]
    y = 0
    for c, exp in zip(p.vals, exponents):
        y += c * x ** exp

    return y

table_width = 80
col_width = table_width // 3
problems = [
    ["Example 1. Linear Regression", 
     output_vector_polynomial, coefficient_matrix_polynomial, regression_string_polynomial, 1,
     [(0,0),(1,10),(2,20),(3,50),(4,35),(5,100),(6,110),(7,190),(8,150),(9,260),(10,270)]],
    ["Example 2. Quadratic Regression", 
     output_vector_polynomial, coefficient_matrix_polynomial, regression_string_polynomial, 2,
     [(0,0),(1,10),(2,20),(3,50),(4,35),(5,100),(6,110),(7,190),(8,150),(9,260),(10,270)]],
    ["Example 3. Eighth Order Regression", 
     output_vector_polynomial, coefficient_matrix_polynomial, regression_string_polynomial, 8,
     [(0,0),(1,10),(2,20),(3,50),(4,35),(5,100),(6,110),(7,190),(8,150),(9,260),(10,270)]]
]
for prob_desc, output_vector_eq, coefficient_matrix_eq, regression_string_eq, order, data in problems:
    ## Problem Start
    print(f"".center(table_width, '_'))
    print(f"coeff_eq:{coefficient_matrix_eq.__name__} data:{data}".center(table_width, '—'))
    print(f"".center(table_width, '='))
    x = [list(point[:-1]) for point in data]
    y = output_vector_eq([[point[-1]] for point in data])
    X = coefficient_matrix_eq(order, x)

    ## Calculate and Print Regression
    X_inv = X.pseudoinverse()
    X_T = X.transpose()
    X_T_y = X_T.matrix_multiply(y)
    p = X_inv.matrix_multiply(X_T_y)
    print(f"  {prob_desc}")
    print(f"  p:{p.vals}")
    print(f"  {regression_string_eq(order, p)}")

    ## Calculate Cross-validation error "cross-validated residual sum of squares (RSS)"
    rss_error = 0
    print(f"  " + 
          f" Removed Point ".center(col_width, '_') +
          f" Regression Eq. ".center(col_width, '_') +
          f" Predicted Val. ".center(col_width, '_')) 
    for removed_point in data:
        remaining_data = data.copy()
        remaining_data.remove(removed_point)

        x = [list(point[:-1]) for point in remaining_data]
        y = output_vector_eq([[point[-1]] for point in remaining_data])
        X = coefficient_matrix_eq(order, x)

        ## Calculate and Print Regression
        X_inv = X.pseudoinverse()
        X_T = X.transpose()
        X_T_y = X_T.matrix_multiply(y)
        p = X_inv.matrix_multiply(X_T_y)
        predicted_val = predicted_val_polynomial(p, removed_point[0])
        rss_error += (predicted_val - removed_point[1]) ** 2

        print(f"  " +
              f"{removed_point}".center(col_width) +
              f"{regression_string_eq(order, p)}"[:col_width].center(col_width) +
              f"{predicted_val:.4g}".center(col_width))

    print(f"    Cross-Validated RSS Error: {rss_error:.4g}")
    print(f"".center(table_width, "—"))
    print()
