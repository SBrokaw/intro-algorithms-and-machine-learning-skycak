# Skycak, J. (2021). Basic Matrix Arithmetic. In Introduction to 
# Algorithms and Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/basic-matrix-arithmetic/

class Matrix:
    def __init__(self, rows):
       self.data = [r for r in rows] 
       print(f'init {self.data}')

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



A = Matrix([[1, 2], [3, 4]])
A.show()
A_t = A.transpose()
A_t.disp()