
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