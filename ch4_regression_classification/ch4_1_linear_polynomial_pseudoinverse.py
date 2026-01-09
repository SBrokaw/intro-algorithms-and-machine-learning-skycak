# Skycak, J. (2022). Linear, Polynomial, and Multiple Linear Regression via Pseudoinverse. 
# In Introduction to Algorithms and Machine Learning: 
# from Sorting to Strategic Agents. 
# https://justinmath.com/linear-polynomial-and-multiple-linear-regression-via-pseudoinverse/

import matplotlib.pyplot as plt
import numpy as np

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


def coefficient_matrix( order, data ):
    coeffs = []
    for d in data:
        coeffs += [[v ** exp for exp in range(order, 0, -1) for v in d] + [1]]

    # print(f"  coeffs:{coeffs}")
    return Matrix(coeffs)

def compute_regression_2d(xs, cs):
    ys = np.array([cs[-1] for _ in range(len(xs))])
    for coeff, exp in zip(cs,range(len(cs) - 1, 0, -1)):
        ys += (coeff * (xs ** exp))

    return ys


def compute_regression_3d(xs, ys, cs):
    return [cs[0] * x + cs[1] * y + cs[2] for x, y in zip(xs, ys)]



table_width = 50
# 1. Fit y=mx+b to [(1,0),(3,−1),(4,5)].
# 2. Fit y=mx+b to [(−2,3),(1,0),(3,−1),(4,5)].
# 3. Fit y=ax2+bx+c to [(−2,3),(1,0),(3,−1),(4,5)].
# 4. Fit y=ax2+bx+c to [(−3,−4),(−2,3),(1,0),(3,−1),(4,5)].
# 5. Fit y=ax3+bx2+cx+d to [(−3,−4),(−2,3),(1,0),(3,−1),(4,5)].
# 6. Fit z=ax+by+c to [(−2,3,−3),(1,0,−4),(3,−1,2),(4,5,3)].
problems = [
    (1, [(0,1),(2,5),(4,3)]),
    (2, [(0,1),(2,5),(4,3),(5,0)]),
    (1, [(0,1,50),(2,5,30),(4,3,20),(5,0,10)]),
    (1, [(1,0),(3,-1),(4,5)]),
    (1, [(-2,3),(1,0),(3,-1),(4,5)]),
    (2, [(-2,3),(1,0),(3,-1),(4,5)]),
    (2, [(-3,-4),(-2,3),(1,0),(3,-1),(4,5)]),
    (3, [(-3,-4),(-2,3),(1,0),(3,-1),(4,5)]),
    (1, [(-2,3,-3),(1,0,-4),(3,-1,2),(4,5,3)])
]
nprobs = len(problems)
ncols = 3
nrows = nprobs // ncols + (1 if nprobs % ncols else 0)
fig = plt.figure(figsize=(4 * ncols, 4 * nrows))
for i, (order, data) in enumerate(problems):
    print(f"".center(table_width, '_'))
    print(f"order:{order} data:{data}".center(table_width, '—'))
    print(f"".center(table_width, '='))
    x = [list(point[:-1]) for point in data]
    y = Matrix([[point[-1]] for point in data])
    X = coefficient_matrix(order, x)

    X_inv = X.pseudoinverse()
    X_T = X.transpose()
    X_T_y = X_T.matrix_multiply(y)
    p = X_inv.matrix_multiply(X_T_y)
    print(f"p:")
    p.print()
    print(f"".center(table_width, "—"))

    # form the equation string (i.e. z ≈ 1.1x + 0.31y - 2.7)
    regression_eq = ""
    input_vars = ['x', 'y', 'z'][0:len(data[0]) - 1]
    output_var = ['x', 'y', 'z'][len(data[0]) - 1]
    regression_eq += f"{output_var} ≈ "
    exponents = ['', '²', '³'][0:order]
    exponents.reverse()
    p_vals = p.vals
    for p_idx, m in enumerate(exponents):
        for t in input_vars:
            regression_eq += f"{p_vals[p_idx]:.2g}{t}{m} + "
    regression_eq += f"{p_vals[-1]:.2g}"
    regression_eq = regression_eq.replace("+ -", "– ")
    regression_eq = regression_eq.replace("-", "–")
    print(f"  Regression Equation: {regression_eq}")


    # plot it
    # xs, ys, [zs] form the input data points
    # xr, yr, [zr] form the regression curve
    npts = 20
    ax = fig.add_subplot(nrows, ncols, i + 1, projection="3d" if len(data[0]) > 2 else None)
    xs = [point[0] for point in data]
    ys = [point[1] for point in data]
    xr = np.linspace(min(-3, min(xs)), max(3, max(xs)), npts)
    if len(data[0]) > 2:
        zs = [p[2] for p in data]
        yr = np.linspace(min(-3, min(ys)), max(3, max(ys)), npts)
        zr = compute_regression_3d(xr, yr, p.vals)
        ax.scatter(xs, ys, zs)
        ax.plot(xr, yr, zr, label=regression_eq)
    else:
        yr = compute_regression_2d(xr, p.vals)
        ax.scatter(xs, ys)
        ax.plot(xr, yr, label=regression_eq)
    ax.legend()

    print()

filename = f"ch4_1_plots.png"
fig.savefig(filename)
print(f"  Plot {filename} generated.")
plt.close()
