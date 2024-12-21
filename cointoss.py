
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

        #Code that checks if there is a streak of 6 heads or tails in a row

    heads = 0
    tails = 0
    for i in results:
        if i == 'H':
            heads += 1
            tails = 0
            if heads == 6:
                numberOfStreaks += 1
                
        else:
            heads = 0
            tails += 1
            if tails == 6:
                numberOfStreaks += 1


    print(f"Number of streaks: {numberOfStreaks}")

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
