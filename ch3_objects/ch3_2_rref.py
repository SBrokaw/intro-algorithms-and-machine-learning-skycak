# Skycak, J. (2021). Reduced Row Echelon Form and Applications 
# to Matrix Arithmetic. In Introduction to Algorithms and 
# Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/reduced-row-echelon-form-and-applications-to-matrix-arithmetic/

class Matrix:
    def __init__(self, rows):
        self.data = [r for r in rows]
    
    @property
    def num_rows(self): return len(self.data)

    @property
    def num_cols(self): return len(self.data[0])

    @property
    def is_empty(self): return True if len(self.data[0]) == 0 else False

    def show(self):
        for r in self.data:
            print('[ ', end = '')
            for i in range(len(r)):
                end_char = ']' if i == len(r) - 1 else ', '
                print(f'{r[i]:.3g} {end_char}', end = '')
            print('')
        return 0

    def print(self):
        return self.show()

    def disp(self):
        return self.show()
    
    def display(self):
        return self.show()

    def col(self, j):
        if j < 1 or j > self.num_cols: return None
        return [self.data[k][j-1] for k in range(self.num_rows)]

    def row(self, i):
        if i < 1 or i > self.num_rows: return None
        return self.data[i-1]

    def transpose(self):
        rows = len(self.data)
        columns = len(self.data[0])
        transposed = [[0] * rows for c in range(columns)]
        for i in range(rows):
            for j in range(columns):
                transposed[j][i] = self.data[i][j]

        return Matrix(transposed)

    def rref(self):
        rref = [r[:] for r in self.data]
        cols = [c[:] for c in self.transpose().data]

        row_idx = 0
        pivot_idx = 0
        # print(cols)
        for c in cols:
            # if pivot row exists for column:
            pivot_idx = next((i for i, v in enumerate(c) if v != 0 and i >= row_idx), -1)
            if pivot_idx >= 0:
                # if pivot row does not match current row_index:
                if pivot_idx != row_idx:
                    # swap current row with pivot row
                    # (so that it matches)
                    for v in cols:
                        temp_val = v[row_idx]
                        v[row_idx] = v[pivot_idx]
                        v[pivot_idx] = temp_val
                    # print(f'swap {row_idx},{pivot_idx}\t{cols}')

                # divide pivot row (so that first nonzero entry is 1)
                scalar = c[row_idx]
                if scalar != 1:
                    for v in cols:
                        v[row_idx] /= scalar
                    # print(f'scale r{row_idx} 1/{scalar}\t{cols}')

                # clear entries below and above pivot entry
                # (by subtracting multiples of pivot row)
                clr_idxs = [u for u in range(len(c)) if u != pivot_idx and c[u] != 0]
                for r in clr_idxs:
                    clr_scalar = -1 * c[r] / c[pivot_idx]
                    for c2 in cols:
                        c2[r] += clr_scalar * c2[pivot_idx]
                    # print(f'clear r{r} + {clr_scalar}∙r{pivot_idx}\t{cols}')

                row_idx += 1

        return Matrix(cols).transpose()

    def inverse(self):
        if self.num_cols != self.num_rows:
            print(f'ERROR! Matrix is not square. Dims={self.num_rows}x{self.num_cols}')
            return Matrix([[]])

        # copy and augment matrix
        rows = [r[:] for r in self.data]
        for idx, r in enumerate(rows):
            augment = [0] * len(rows)
            augment[idx] = 1
            rows[idx] += augment
        
        augmented = Matrix(rows)
        
        cols = [c[:] for c in augmented.transpose().data]

        row_idx = 0
        pivot_idx = 0
        # print(cols)
        for c in cols[:augmented.num_rows]:
            # if pivot row exists for column:
            pivot_idx = next((i for i, v in enumerate(c) if v != 0 and i >= row_idx), -1)
            if pivot_idx >= 0:
                # if pivot row does not match current row_index:
                if pivot_idx != row_idx:
                    # swap current row with pivot row
                    # (so that it matches)
                    for v in cols:
                        temp_val = v[row_idx]
                        v[row_idx] = v[pivot_idx]
                        v[pivot_idx] = temp_val
                    # print(f'swap {row_idx},{pivot_idx}\t{cols}')

                # divide pivot row (so that first nonzero entry is 1)
                scalar = c[row_idx]
                if scalar != 1:
                    for v in cols:
                        v[row_idx] /= scalar
                    # print(f'scale r{row_idx} 1/{scalar}\t{cols}')

                # clear entries below and above pivot entry
                # (by subtracting multiples of pivot row)
                clr_idxs = [u for u in range(len(c)) if u != pivot_idx and c[u] != 0]
                for r in clr_idxs:
                    clr_scalar = -1 * c[r] / c[pivot_idx]
                    for c2 in cols:
                        c2[r] += clr_scalar * c2[pivot_idx]
                    # print(f'clear r{r} + {clr_scalar}∙r{pivot_idx}\t{cols}')

                row_idx += 1


        return Matrix(cols[augmented.num_rows:]).transpose()


matxs = [Matrix([[1, -2], [2, -1]]),
         Matrix([[0]]),
         Matrix([[]]),
         Matrix([[0, 1, -1], [0, -1, -1], [0, 0, -1]]),
         Matrix([[-1, 1, -1], [0, -1, -1], [1, 0, -1]]),
         Matrix([[1, 0, -1], [0, 2, 1], [1, -1, 0]]),
         Matrix([[-1, 1, -1], [0, -1, -1]]),
         Matrix([[-1, 1], [0, -1], [1, 0]])
         ]

for A in matxs:
    print('Matrix A')
    A.print()
    print('RREF(A)')
    A_rref = A.rref()
    A_rref.print()
    print('A^-1')
    A_inv = A.inverse()
    A_inv.print()
    print()
