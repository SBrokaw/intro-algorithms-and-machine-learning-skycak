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


A = Matrix([[1, 2], [3, 4]])
A.show()