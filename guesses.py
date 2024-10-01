
import random
secretNumber = random.randint(1, 20)

print("I am thinking of a number between 1 and 20. You have 5 tries.")

for guessTaken in range(1, 6):
    print("Take a guess.")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break

if guess == secretNumber:
    print(f"Good job! You guess my number in {guessTaken} tries!")

else:
    print(f"No more tries. The number was {secretNumber}.")
"""
#########################
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess "))
    guess_count += 1
    if guess == secret_number:
        print("You won")
        break
else:
    print("You lose")
    
"""

#Number Guesser

import random

while True:
    def play_again():
        retry = input("Would you like to play again? ")
        if retry == "y":

        elif retry == "n":
            print("Good bye")
            quit()
            
    secret_num = random.randint(0,20)
    tries = 0
    while tries < 6:
        guess = int(input(f"Guess my number, between 0 and 20. You have {6 - (tries)} tries. "))
        if guess == secret_num:
            tries += 1
            print(f"Congratulations, the number was {secret_num}! You win. It took you {tries} times.")
            play_again()
            break
                
        elif guess < secret_num:
            tries += 1
            print("Too low")
        elif guess > secret_num:
            tries += 1
            print("Too high")

        if tries == 6:
            print("You lose")
            play_again()
