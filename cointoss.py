
import random
numberOfStreaks = 0

for experimentNumber in range(20):

    #Code to create a list of 100 'heads' or 'tails' values:
    results = []
    for experimentNumber in range(10):
        tossResult = random.randint(0, 1)
        if tossResult == 0:
            tossResult = 'H'     
        else:
            tossResult = 'T'
        results.append(tossResult)

    print(results)