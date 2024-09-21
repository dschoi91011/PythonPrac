import random
numStreaks = 0

for generateNum in range(20):

    #create list of 100 'heads' or 'tails' values:
    results = []
    for generateNum in range(10):
        tossResult = random.randint(0, 1)
        if tossResult == 0:
            tossResult = 'H'
        else:
            tossResult = 'T'
        results.append(tossResult)

    print(results)

    #check for streak of 6 heads or tails in a row
    heads = 0
    tails = 0
    for i in results:
        if i == 'H':
            heads += 1
            tails = 0
            if heads == 6:
                numStreaks += 1

        else:
            heads = 0
            tails += 1
            if tails == 6:
                numStreaks += 1

    print(f"Number of streaks: {numStreaks}")

print('Chance of steak: %s%%' % (numStreaks / 100))