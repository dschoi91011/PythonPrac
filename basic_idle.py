"""
birthyear = input("Enter birth year: ")
age = 2022 - int(birthyear)
print(age)

name = input("What is your name? ")
print(f"Hello, {name.title()}")


#int() is integer
#float() is decimal
#str() is string, or alphabet/words/characters/

first = input("First number to be added: ")
second = input("\nSecond number to be added: ")
sum = int(first) + float(second)
print("Sum: " + str(sum))

#OR

first = int(input("First to be added: "))        #conversion of one variable type to another
second = float(input("Second to be added: "))
sum = str(first + second)
print("Sum: " + sum)

#OR

first = int(input("First: "))
second = int(input("Second: "))
sum = first + second
print("Sum: " + str(sum))


weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    conversion = weight / 2.2
    print("Weight in Lbs: " + str(conversion))
else:
    conversion = weight * 2.2
    print("Weight in Kg: " + str(conversion))

numbers = [1, 2, 3, 4, 5, 6]
print(numbers)
numbers.append(0)
numbers.insert(1,20)
print(numbers)

for item in range(0, 20, 3):
    print(item)

dictionary = {"first_name":"sharon", "last_name":"lee", "age":36, "residence":"pasadena"}
firstName = dictionary["first_name"].title()
lastName = dictionary["last_name"].title()
age = dictionary["age"]
residence = dictionary["residence"].title()
print("Name: " + firstName, lastName)
print("Age: " + str(age))
print("Resdience: " + residence)

favorite_numbers = {'Sharon': '9', 'Bass': '13', 'John': '7', 'Max': '4'}
friends = ['Sharon', 'Bass']
for name in favorite_numbers:
    print(f"Hi {name.title()}")
    if name in friends:
        number = favorite_numbers[name].title()
        print(f"\t{name.title()}, I see your favorite number is {number}.")
if 'Jack' not in favorite_numbers.keys():
              print("Jack, please take our poll.")
print("The following numbers have been mentioned:")
for number in favorite_numbers.values():
    print(number)


sharon = favorite_numbers['Sharon']
print("\nSharon's favorite number is " + str(sharon) + ".")



user_0 = {
    'username': 'dschoi',
    'first': 'daniel',
    'last': 'choi'
    }
realName = ['first', 'last']
for key, value in user_0.items():
    print(f"\nKey: {key}")
    if key in realName:
        name = user_0[key].title()
        print(f"Value: {name}")
    else:
        print(f"Value: {value}")


name = input('What is your name? ')
color = input('What is your favorite color? ')
print(name.title() + " likes " + color)
print(f"{name.title()} likes {color}.")



#Prac app: Ask the year of birth, calculate age
birth_year = int(input("What year were you born? "))
age = (f"You are {str(2022 - birth_year)} years old.")
print(age)


#Prac app: Ask for user weight (lbs), convert to kg
raw_weight = input("Weight(lbs): ")
converted_weight = int(raw_weight) * 0.45
print(converted_weight, "kg")

#Prac app: formatting strings
first = 'John'
last = 'Smith'
print(f"{first} [{last}] is a coder.")

course = "Python for beginners"
print(course.upper())
print(course)
print(course.find('P'))
print(len(course[0:]))
print('Python' in course)
print(course.replace('for', '4'))

import math
print(math.ceil(3.5))

price = 1000000
has_good_credit = False
if has_good_credit == True:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print(f"Down payment: ${down_payment}")

weight = int(input("Weight: "))
conversion = input("(L)bs or (K)g: ")
if conversion.upper() == "L":
    unit = weight // 0.45
    print(f"Your weight is {unit}kg")
elif conversion.upper() == "K":
    print(f"Your weight is {weight * 0.45}lbs")
else:
    print("That is not valid")


i = 3
while i < 20:
    print(i)
    i += 2
    if i < 18:
        print("Not yet")
    else:
        print("Done\n")

i = 1
while i <= 5:
    print("*" * 2)
    i = i + 1
print("Done")


#Guessing game
answer = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == answer:
        print("You won")
        break
else:
    print("Game over")


total = 0
prices = [10, 20, 30]
for items in prices:
    total += items
print(total)

for x in range(4):
    for y in range(3):
        print(f'({x, y})')

numbers = [5, 2, 5, 2, 2]
for items in numbers:
    output = ''
    for count in range(items):
        output += 'x'
    print(output)
print('\n')
"""

i = 1
while i <= 3:
    print("Meow")
    i += 1
print("Shut up, cat!")
    
#for cat in range(3):
#    print("Meow")
#print("Shut up, cat!")




#PRAC APP: CAR GAME
"""
car_started = False
while True:                                     # or command != "quit":
    command = input(">").lower()
    if command == "start":
        if car_started:
            print("Car has already started.")
        else:
            car_started = True
            print("Car started... Let's go!")
    elif command == "stop":
        if not car_started:
            print("Car has already stopped.")
        else:
            car_started = False
            print("Car has stopped.")
    elif command == "help":
        print("start - to start car \nstop - to stop car \nquit - to quit")        ")
    elif command == "quit":
        print("Good bye")
        break
    else:
        print("I don't understand that command.")
        
"""
"""
numbers = [3, 4, 4, 5, 5, 5, 6, 8, 10]
singles = []
for number in numbers:
    if number not in singles:
        singles.append(number)
print(singles)

coordinates = (1, 2, 3)
x, y, z = coordinates
print(x)


name = input("user_name: ")

if len(name) < 3:
    print("user name must be at least 3 characters")    
elif len(name) > 10:
    print("user name can be a maximum of 10 characters")    
else:
    print("user name created")
  
######################

prices = [10, 20, 30]
total = 0

for item in prices:
    total += item
     
print(total)

######################
for x in range(4):
    for y in range(3):
        print(f'({x, y}')
"""
"""
numbers = [2, 2, 2, 2, 5]
for x_count in numbers:
       output = ""                  # OR output = "x" * x_count
       for count in range(x_count):
           output += "x"
       print(output)
print(f"{'#' *30}\n")

numbers = [2, 4, 7, 4, 5, 2, 2, 1, 19]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

phone = input("Phone: ")

phonebook = {"1":"one", "2":"two", "3":"three", "4":"four"}
output = ""
for digit in phone:
       output = phonebook.get(digit)
       print(output)

def math():
       print("I can math good")
       print(100 * 10)

def greetings(name):
       print(f"Hi {name}")
       math()
       print("It's nice to meet you")
              

print("Hello world")
greetings("Bob")
print("Good bye")
"""