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
        col_width = 6
        # header
        print(f"     ", end='')
        for col in ["x_" + str(n+1) for n in range(len(self.table[0]) - 1)]:
            print(f"{col:3s}".center(col_width), end='')
        print(f" constant")

        # maximize row
        print(f"max ", end='')
        for c in self.table[0]:
            print(f"{c: 2g}".center(col_width), end='')
        print()
        # constraints rows
        for constraint in self.table[1:]:
            print(f"con ", end='')
            for c in constraint:
                print(f"{c: 2g}".center(col_width), end='')
            print()

        return 0

    def solve(self):
        for loop in range(5): # while max(self.table[0][:-1]) > 0:
            max_slope = self.table[0].index(max(self.table[0]))
            constraints_raw = [constraint_eq[-1] / constraint_eq[max_slope] for constraint_eq in self.table[1:]]
            constraints = [v for v in constraints_raw if v > 0]
            most_limiting = constraints_raw.index(min(constraints)) + 1 # index of most limiting constraint
            scalar = self.table[most_limiting][max_slope]
            self.table[most_limiting] = [v / scalar for v in self.table[most_limiting]]

            rows_to_reduce = [i for i in range(len(self.table)) if i != most_limiting]
            for i in rows_to_reduce:
                k = -1 * self.table[i][max_slope] / self.table[most_limiting][max_slope]
                self.table[i] = [self.table[i][j] + k * self.table[most_limiting][j] for j in range(len(self.table[i]))]

            self.print_table()
            if max(self.table[0][:-1]) <= 0: 
                break

        return abs(self.table[0][-1])


table_width = 50
problems = [[[1, 2, 1, 0, 0, 0, 0],  # maximize
             [2, 1, 1, 1, 0, 0, 14], # constraint1
             [4, 2, 3, 0, 1, 0, 28], # constraint2
             [2, 5, 5, 0, 0, 1, 30]], # constraint3
            [[20, 10, 15, 0, 0, 0, 0, 0], # maximize
             [3, 2, 5, 1, 0, 0, 0, 55], # constraint1
             [2, 1, 1, 0, 1, 0, 0, 26], # constraint2
             [1, 1, 3, 0, 0, 1, 0, 30], # constraint3
             [5, 2, 4, 0, 0, 0, 1, 57]] # constraint4
           ]
for problem_no, array in enumerate(problems):
    print(f" Starting Table {problem_no} ".center(table_width, '—'))
    print(f"".center(table_width, '‾'))
    simplex = SimplexSolver(array)
    simplex.print_table()
    print()

    objective = simplex.solve()
    print(f" Final Table ".center(table_width, '—'))
    simplex.print_table()
    print(f"Maximization = {objective}".center(table_width))
    print(f"".center(table_width, '‾'))
