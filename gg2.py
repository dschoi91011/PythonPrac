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
            


            
    
