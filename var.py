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

#Write a function that generates "apple, bananas, tofu, and cats." Should
#work on any given list.
spam = ['apple', 'bananas', 'tofu', 'cats', 'poo']

for item in spam:
    print(item, end = ", ")
    if item == spam[-2]:
        break
print(f"and {spam[-1]}")
