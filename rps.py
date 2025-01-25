import random, sys
print("ROCK, PAPER, SCISSORS")
Wins = 0
Losses = 0
Ties = 0

while True:   #main loop
    print("%s Wins, %s Losses, %s Ties" % (Wins, Losses, Ties))   # SAME AS    print(f"{Wins} Wins, {Losses} Losses, {Ties} Ties")
    while True:   #player input loop
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        playerChoice = input()
        if playerChoice == 'q':
            sys.exit()
        elif playerChoice == 'r' or playerChoice == 'p' or playerChoice == 's':
            break
        else:
            print("Type r, p, s, or q")

#player choice
    if playerChoice == 'r':
        print('ROCK vs...')
    elif playerChoice == 'p':
        print('PAPER vs...')
    elif playerChoice == 's':
        print('SCISSORS vs...')

#computer choice
    randomNum = random.randint(1, 3)
    if randomNum == 1:
        computerChoice = 'r'
        print('ROCK')
    elif randomNum == 2:
        computerChoice = 'p'
        print('PAPER')
    elif randomNum == 3:
        computerChoice = 's'
        print('SCISSORS')

#display/record score
    if playerChoice == computerChoice:
        print("It's a tie!")
        Ties += 1
    elif playerChoice == 'r' and computerChoice == 'p':
        print("You lose")
        Losses += 1
    elif playerChoice == 'r' and computerChoice == 's':
        print("You win")
        Wins += 1
    elif playerChoice == 'p' and computerChoice == 'r':
        print("You win")
        Wins += 1
    elif playerChoice == 'p' and computerChoice == 's':
        print("You lose")
        Losses += 1
    elif playerChoice == 's' and computerChoice == 'p':
        print("You win")
        Wins += 1
    elif playerChoice == 's' and computerChoice == 'r':
        print("You lose")
        Losses += 1

