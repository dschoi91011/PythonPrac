#OBJECTIVES:
"""
Create a quiz game that asks user a number of trivia questions. Track score based on correct answers
given and return percentage score
"""


while True:
    
    score = 0   
    game = input("Shall we play the guessing game? ")
    if game.lower() == "yes":
        answer = input("Who was the oldest living man in the Bible?")
        if answer == "Methuselah":
            print("Correct!")
            score += 1
        else:
            print("Incorrect")
        answer = input("What sucks?")
        if answer == "mosquito":
            print("Correct!")
            score += 1
        else:
            print("Incorrect")
        answer = input("Why?")
        if answer == "Why not?":
            print("Correct!")
            score += 1
        else:
            print("Incorrect")
                

        #Score keeping
        if score == 0:
            print("Your score is 0%")
        elif score == 1:
            print(f"Your score is {float(score / 3)}%")
        elif score == 2:
            print(f"Your score is {float(score / 3)}%")
        else:
            print("Your score is 100%")

        while True:
            answer = input("Would you like to try again?")
            if answer == "yes":
                break
            elif answer == "no":
                print("That concludes the guessing game")
                quit()
            else:
                print("That is not valid")

        


    elif game.lower() == "no":
        quit()

    else:
        print("That is not valid")
