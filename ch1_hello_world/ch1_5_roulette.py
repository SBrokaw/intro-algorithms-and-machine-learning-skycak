# Skycak, J. (2021). Roulette Wheel Selection. 
# In Introduction to Algorithms and Machine Learning: 
# from Sorting to Strategic Agents. 
# https://justinmath.com/roulette-wheel-selection/

import random
import pdb

def pdf_to_cdf(f):
    cdf = []
    sum = sum_pdf(f)
    if sum < 0.99 or sum > 1.01:
        return -1

    for i in range(len(f)):
        cdf.append(round(sum_pdf(f[:i+1]), 2))
    return cdf

def sum_pdf(f):
    if not f: return 0 
    if not isinstance(f, (list, tuple, range)): return 0

    return sum_pdf_loop(f)

def sum_pdf_loop(f):
    if not f: return 0 # base case return 0 when f is empty
    sum = f[0] + sum_pdf_loop(f[1:])
    return sum

def cdf_roulette(cdf, sample):
    if sample > 1 or sample < 0: return -1
    if sample == 1.0: return len(cdf) - 1

    for i in range(len(cdf)):
        if cdf[i] >= sample:
            return i

    return -1

pdfs = [[0.4, 0.2, 0.2, 0.2],
        [0.9, 0.03, 0.04, 0.03],
        [0.1, 0.2, 0.3, 0.4],
        [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]]

for pdf in pdfs:
    cdf = pdf_to_cdf(pdf)
    print(f'PDF = {pdf}\nCDF = {cdf}')

    # output1 = []
    # output2 = []

    # for i in range(10):
    #     sample = round(random.random(), 2)
    #     index = cdf_roulette(cdf, sample)

    #     output1.append(f'{sample}'.center(5, ' '))
    #     output2.append(f'{index}'.center(5, ' '))

    # print(f'{output1}\n{output2}')

    count = 0
    trials = [0] * len(cdf)
    for i in range(10000):
        count += 1
        sample = round(random.random(), 3)
        result = cdf_roulette(cdf, sample)
        trials[result] += 1

    for i in range(len(trials)):
        trials[i] = trials[i] / count

    print(trials)

