# Skycak, J. (2021). Basic Matrix Arithmetic. In Introduction to 
# Algorithms and Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/basic-matrix-arithmetic/

def dot_product( arr1, arr2 ):
    if len(arr1) != len(arr2):
        print(f'ERROR! Dot product dimension mismatch. {len(arr1)} != {len(arr2)}')
        return 0

    product = 0
    for i in range(len(arr1)):
        product += arr1[i] * arr2[i]

    return product

class Matrix:
    def __init__(self, rows):
       self.data = [r for r in rows] 
       self.num_cols = len(self.data[0])
       self.num_rows = len(self.data)

    def show(self):
        for r in self.data:
            print('[ ', end = '')
            for i in range(len(r)):
                end_char = ']' if i == len(r) - 1 else ', '
                print(f'{r[i]} {end_char}', end = '')
            print('')
        return 0

    def print(self):
        return self.show()

    def disp(self):
        return self.show()
    
    def display(self):
        return self.show()

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

    def matrix_multiply(self, m):
        if self.num_cols != m.num_rows:
            print(f'ERROR! Matrix multiply dimension mismatch. [{self.num_rows}, {self.num_cols}] != [{m.num_rows}, {m.num_cols}]')
            return self

        product = [[0] * self.num_rows for c in range(m.num_cols)]
        for i in range(self.num_rows):
            for j in range(m.num_cols):
                row = self.data[i]
                col = [m.data[k][j] for k in range(self.num_cols)]
                # print(f'row {row}\tcol {col}')
                product[i][j] = dot_product(row, col) 

        # print(f'product = {product}')
        return Matrix(product)

matxs = [Matrix([[1, 2], [3, 4]]),
         Matrix([[1, 2, 3], [4, 5, 6]]),
         Matrix([[-1, -2], [-3, -4], [-5, -6]])]

for A in matxs:
    print(f'A')
    A.show()
    print(f'A_t')
    A_t = A.transpose()
    A_t.disp()
    print(f'A + A_t')
    A.add(A_t).print()
    print(f'A - A_t')
    A.subtract(A_t).print()
    print(f'-1·A')
    A.scalar_multiply(-1).print()
    print(f'A[{A.num_rows},{A.num_cols}]·A_t[{A_t.num_rows},{A_t.num_cols}]')
    A.disp(); A_t.disp()
    A.matrix_multiply(A_t).print()
    print()
