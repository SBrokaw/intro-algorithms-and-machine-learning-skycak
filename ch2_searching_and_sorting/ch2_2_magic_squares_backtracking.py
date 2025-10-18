# Skycak, J. (2021). Solving Magic Squares via Backtracking. 
# In Introduction to Algorithms and Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/solving-magic-squares-via-backtracking/

def valid_square( trial ):
    if sum(trial[0]) != 15 or 

def magic_squares():
    digits = range(1, 10)
    blank = [[None,None,None],
             [None,None,None],
             [None,None,None]]
    trial = [[None,None,None],
             [None,None,None],
             [None,None,None]]
    successes = []

    for n1 in digits:
        trial = blank.copy()
        trial[0][0] = n1
        for n2 in digits:
            trial = blank.copy()
            trial[0][0] = n1
            trial[0][1] = n2
            for n3 in digits:
                trial = blank.copy()
                trial[0][0] = n1
                trial[0][1] = n2
                trial[0][2] = n3
                for n4 in digits:
                    trial = blank.copy()
                    trial[0][0] = n1
                    trial[0][1] = n2
                    trial[0][2] = n3
                    trial[1][0] = n4
                    for n5 in digits:
                        trial = blank.copy()
                        trial[0][0] = n1
                        trial[0][1] = n2
                        trial[0][2] = n3
                        trial[1][0] = n4
                        trial[1][1] = n5
                        for n6 in digits:
                            trial = blank.copy()
                            trial[0][0] = n1
                            trial[0][1] = n2
                            trial[0][2] = n3
                            trial[1][0] = n4
                            trial[1][1] = n5
                            trial[1][2] = n6
                            for n7 in digits:
                                trial = blank.copy()
                                trial[0][0] = n1
                                trial[0][1] = n2
                                trial[0][2] = n3
                                trial[1][0] = n4
                                trial[1][1] = n5
                                trial[1][2] = n6
                                trial[2][0] = n7
                                for n8 in digits:
                                    trial = blank.copy()
                                    trial[0][0] = n1
                                    trial[0][1] = n2
                                    trial[0][2] = n3
                                    trial[1][0] = n4
                                    trial[1][1] = n5
                                    trial[1][2] = n6
                                    trial[2][0] = n7
                                    trial[2][1] = n8
                                    for n9 in digits:
                                        trial = blank.copy()
                                        trial[0][0] = n1
                                        trial[0][1] = n2
                                        trial[0][2] = n3
                                        trial[1][0] = n4
                                        trial[1][1] = n5
                                        trial[1][2] = n6
                                        trial[2][0] = n7
                                        trial[2][1] = n8
                                        trial[2][2] = n9

                                        if valid_square(trial): successes += [trial.copy()]