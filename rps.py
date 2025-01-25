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

