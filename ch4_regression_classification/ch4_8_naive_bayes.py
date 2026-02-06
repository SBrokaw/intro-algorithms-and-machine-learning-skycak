# Skycak, J. (2022). Naive Bayes. 
# In Introduction to Algorithms and Machine Learning: 
# from Sorting to Strategic Agents. 
# https://justinmath.com/naive-bayes/

class NaiveBayesClassifier:
    def __init__(self, training_set):
        self.data = [[_ for _ in row] for row in training_set]
        self.P_category = [row[0] for row in self.data].count(1) / len(self.data)
        self.P_not_category = 1.0 - self.P_category
        self.P_vars_given_category = self.vars_given_category(1)
        self.P_vars_given_not_category = self.vars_given_category(0)



    def vars_given_category(self, category):
        P_var_given_cat = [[]]
        for var in range(len(self.data[0][1:])):
            P = self.data_given_category(category).count(1)
            P_not = 1.0 - P
            P_var_given_cat[var] = [P_not, P]

        return P_var_given_cat

    def data_given_category(self, category):
        return [row for row in self.data if row[0] == category]

    def guess_category(self, point):
        P_c = self.P_category
        P_not_c = self.P_not_category
        for i in range(len(point)):
            P_c *= self.P_vars_given_category[i][point[i]]
            P_not_c *= self.P_vars_given_not_category[i][point[i]]

        if P_c > P_not_c: guess = 1
        elif P_c < P_not_c: guess = 0
        else: P_ 



training_set = [[0, 0, 0],
                [1, 1, 1],
                [1, 1, 1],
                [0, 0, 0],
                [0, 0, 1],
                [1, 1, 1],
                [0, 1, 0],
                [0, 0, 1],
                [1, 1, 0],
                [0, 0, 1]]

table_width = 80
print(f" Chapter 4, Lesson 8: Naive Bayes Classifiers ".center(table_width, '='))
nbc = NaiveBayesClassifier(training_set) 
print(f"  P(spam)={nbc.P_category:.2g} P(not_spam)={nbc.P_not_category:.2g}")
print(f"  P(vars|spam)=")
for row in nbc.P_vars_given_category:
    print(f"    {row}")
