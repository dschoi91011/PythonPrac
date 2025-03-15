
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