# Skycak, J. (2021). Simplex Method. 
# In Introduction to Algorithms and Machine Learning: 
# from Sorting to Strategic Agents. 
# https://justinmath.com/simplex-method/

class SimplexSolver():
    def __init__(self, table):
        ## Simplex table format (example shown):
        #                basic variables : slack variables
        #                x_1  x_2  x_3     x_4  x_5  x_6   | constant
        # table[0] = max  1    2    1       0    0    0    |   0
        # table[1] = con  2    1    1       1    0    0    |  14
        # table[2] = con  4    2    3       0    1    0    |  28
        # table[3] = con  2    5    5       0    0    1    |  30
        self.table = [row[:] for row in table]
        self.objective = self.table[0][-1]

    def print_table(self):
        col_width = 5
        print(f"    basic variables : slack variables")
        print(f"      x_1  x_2  x_3  x_4  x_5  x_6 | constant")
        print(f"max ", end='')
        for c in self.table[0]:
            print(f"{c: 2g}".center(col_width), end='')
        print()
        for constraint in self.table[1:]:
            print(f"con ", end='')
            for c in constraint:
                print(f"{c: 2g}".center(col_width), end='')
            print()

        return 0

    def solve(self):
        # while max(self.table[0]) > 0:
        max_slope = self.table[0].index(max(self.table[0]))
        constraints = [constraint_eq[-1] / constraint_eq[max_slope] for constraint_eq in self.table[1:]]
        most_limiting = constraints.index(min(constraints)) + 1
        scalar = self.table[most_limiting][max_slope]
        self.table[most_limiting] = [v / scalar for v in self.table[most_limiting]]

        rows_to_reduce = [i for i in range(len(self.table)) if i != most_limiting]
        print(f"  rows_to_reduce = {rows_to_reduce}")

        return self.objective


array = [[1, 2, 1, 0, 0, 0, 0],
         [2, 1, 1, 1, 0, 0, 14],
         [4, 2, 3, 0, 1, 0, 28],
         [2, 5, 5, 0, 0, 1, 30]]
simplex = SimplexSolver(array)
simplex.print_table()
print()

objective = simplex.solve()
simplex.print_table()
print(f"  Maximization = {objective}")
