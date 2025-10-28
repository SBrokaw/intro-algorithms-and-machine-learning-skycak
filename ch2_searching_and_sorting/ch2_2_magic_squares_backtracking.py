# Skycak, J. (2021). Solving Magic Squares via Backtracking. 
# In Introduction to Algorithms and Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/solving-magic-squares-via-backtracking/
import random
import pdb

def deepcopy( target ):
    if isinstance(target, list): return [deepcopy(i) for i in target]
    else: return target


def blankarray():
    blank = [[None,None,None],
             [None,None,None],
             [None,None,None]]
    return deepcopy( blank )


def valid_square( trial ):
    #check rows
    if sum(trial[0]) != 15:
        return False
    elif sum(trial[1]) != 15:
        return False
    elif sum(trial[2]) != 15:
        return False

    #check columns
    if trial[0][0] + trial[1][0] + trial[2][0] != 15:
        return False
    elif trial[0][1] + trial[1][1] + trial[2][1] != 15:
        return False
    elif trial[0][2] + trial[1][2] + trial[2][2] != 15:
        return False

    #check diagonals
    if trial[0][0] + trial[1][1] + trial[2][2] != 15:
        return False
    elif trial[0][2] + trial[1][1] + trial[2][0] != 15:
        return False

    return True


def hopeless_combination(trial):
    #check rows only if the row is full
    if None not in trial[0] and sum(trial[0]) != 15: return True
    elif None not in trial[1] and sum(trial[1]) != 15: return True
    elif None not in trial[2] and sum(trial[2]) != 15: return True

    #check columns only if column is full
    c1t = [trial[0][0], trial[1][0], trial[2][0]]
    c2t = [trial[0][1], trial[1][1], trial[2][1]]
    c3t = [trial[0][2], trial[1][2], trial[2][2]]
    if None not in c1t and sum(c1t) != 15: return True
    elif None not in c2t and sum(c2t) != 15: return True
    elif None not in c3t and sum(c3t) != 15: return True

    #check diagonals only if full
    d1 = [trial[0][0], trial[1][1], trial[2][2]]
    d2 = [trial[0][2], trial[1][1], trial[2][0]]
    if None not in d1 and sum(d1) != 15: return True
    elif None not in d2 and sum(d2) != 15: return True

    return False


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
        trial = blankarray()
        trial[0][0] = n1
        for n2 in digits:
            trial = blankarray()
            trial[0][0] = n1
            trial[0][1] = n2
            for n3 in digits:
                trial = blankarray()
                trial[0][0] = n1
                trial[0][1] = n2
                trial[0][2] = n3
                for n4 in digits:
                    trial = blankarray()
                    trial[0][0] = n1
                    trial[0][1] = n2
                    trial[0][2] = n3
                    trial[1][0] = n4
                    for n5 in digits:
                        trial = blankarray()
                        trial[0][0] = n1
                        trial[0][1] = n2
                        trial[0][2] = n3
                        trial[1][0] = n4
                        trial[1][1] = n5
                        for n6 in digits:
                            trial = blankarray()
                            trial[0][0] = n1
                            trial[0][1] = n2
                            trial[0][2] = n3
                            trial[1][0] = n4
                            trial[1][1] = n5
                            trial[1][2] = n6
                            for n7 in digits:
                                trial = blankarray()
                                trial[0][0] = n1
                                trial[0][1] = n2
                                trial[0][2] = n3
                                trial[1][0] = n4
                                trial[1][1] = n5
                                trial[1][2] = n6
                                trial[2][0] = n7
                                for n8 in digits:
                                    trial = blankarray()
                                    trial[0][0] = n1
                                    trial[0][1] = n2
                                    trial[0][2] = n3
                                    trial[1][0] = n4
                                    trial[1][1] = n5
                                    trial[1][2] = n6
                                    trial[2][0] = n7
                                    trial[2][1] = n8
                                    for n9 in digits:
                                        trial = blankarray()
                                        trial[0][0] = n1
                                        trial[0][1] = n2
                                        trial[0][2] = n3
                                        trial[1][0] = n4
                                        trial[1][1] = n5
                                        trial[1][2] = n6
                                        trial[2][0] = n7
                                        trial[2][1] = n8
                                        trial[2][2] = n9

                                        if valid_square(trial): 
                                            successes += [deepcopy(trial)]
                                        #if len(successes) : print(f'{successes[-1]}')
    
    print(f'{len(successes)} Successes -- Example: {successes[int(len(successes) * random.random())]}')

def magic_squares_w_backtracing():
    digits = range(1, 10)
    blank = [[None,None,None],
             [None,None,None],
             [None,None,None]]
    trial = [[None,None,None],
             [None,None,None],
             [None,None,None]]
    successes = []

    for n1 in digits:
        trial = blankarray()
        trial[0][0] = n1
        for n2 in digits:
            trial = blankarray()
            trial[0][0] = n1
            trial[0][1] = n2
            for n3 in digits:
                trial = blankarray()
                trial[0][0] = n1
                trial[0][1] = n2
                trial[0][2] = n3
                if hopeless_combination(trial): continue
                for n4 in digits:
                    trial = blankarray()
                    trial[0][0] = n1
                    trial[0][1] = n2
                    trial[0][2] = n3
                    trial[1][0] = n4
                    for n5 in digits:
                        trial = blankarray()
                        trial[0][0] = n1
                        trial[0][1] = n2
                        trial[0][2] = n3
                        trial[1][0] = n4
                        trial[1][1] = n5
                        for n6 in digits:
                            trial = blankarray()
                            trial[0][0] = n1
                            trial[0][1] = n2
                            trial[0][2] = n3
                            trial[1][0] = n4
                            trial[1][1] = n5
                            trial[1][2] = n6
                            if hopeless_combination(trial): continue
                            for n7 in digits:
                                trial = blankarray()
                                trial[0][0] = n1
                                trial[0][1] = n2
                                trial[0][2] = n3
                                trial[1][0] = n4
                                trial[1][1] = n5
                                trial[1][2] = n6
                                trial[2][0] = n7
                                if hopeless_combination(trial): continue
                                for n8 in digits:
                                    trial = blankarray()
                                    trial[0][0] = n1
                                    trial[0][1] = n2
                                    trial[0][2] = n3
                                    trial[1][0] = n4
                                    trial[1][1] = n5
                                    trial[1][2] = n6
                                    trial[2][0] = n7
                                    trial[2][1] = n8
                                    if hopeless_combination(trial): continue
                                    for n9 in digits:
                                        trial = blankarray()
                                        trial[0][0] = n1
                                        trial[0][1] = n2
                                        trial[0][2] = n3
                                        trial[1][0] = n4
                                        trial[1][1] = n5
                                        trial[1][2] = n6
                                        trial[2][0] = n7
                                        trial[2][1] = n8
                                        trial[2][2] = n9
                                        if hopeless_combination(trial): continue

                                        if valid_square(trial): 
                                            successes += [deepcopy(trial)]
                                        #if len(successes) : print(f'{successes[-1]}')
    
    print(f'{len(successes)} Successes -- Example: {successes[int(len(successes) * random.random())]}')


#magic_squares()
magic_squares_w_backtracing()
