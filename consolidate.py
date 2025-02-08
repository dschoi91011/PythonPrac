from sys import argv

script, vone, vtwo, vthree = argv

print("The script is called:", script)
print("The first variable is:", vone)
print("The second variable is:", vtwo)
print("The third variable is:", vthree)



#Run in Terminal command line (not Python).
#Go to directory in which this script is stored:
#In this case, it would be D:/Python
#> python ex13.py var_1 var_2 var_3
#The variables (var_x) can be whatever
#You can also change the variable names, e.g.:
#var1, var2, var3, var4 = argv
#It will still work the same way


#this script will also work if done in notepad

"""
from sys import argv

script, user_name = argv     #d:\python> ex14.py Bass
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
"""
#What is this?
#I have no idea what this is
#     What about a haiku?
#Dunno.


from sys import argv
script, input_file = argv


def print_all(f):     #'f' is a file
    print(f.read())

def rewind(f):
    f.seek(0)
    #f.seek(0) will move to the start of the file, (0) being the index
                      

def print_a_line(line_count, f):
    print(line_count, f.readline())
    #f.readline() will read a line from the file and move the reader
    #to just after the \n that ends that line
    


current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)
"""
"""
from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")    #The file name you want to change (e.g. ex_15.sample.txt)

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(f"{line1}\n{line2}\n{line3}\n")

print("And finally, we close it.")
target.close()
"""
"""
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()     #indata = open(from_file).read() should also work

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()     #if you wrote indata = open(from_file).read(),
                    #get rid of in_file.close(). Python will
                    #auto-close that line of code once it runs
"""
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin'.")


print_two("Sharon", "Bass")
print_two_again("Daniel", "Choi")
print_one("First!")
print_none()

def cheese_and_crackers(cheeseCount, boxesOfCrackers):
    print(f"You have {cheeseCount} cheeses!")
    print(f"You have {boxesOfCrackers} boxes of crackers!")
    print("Man, that's enough for a party!")
    print("Get a blanket.\n")

def favoriteNumber():
    number = int(input("What is your favorite number? "))
    print(f"Well, I hope that {number} is also your lucky number.")



print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
cheese_amount = 10
crackers_amount = 50

cheese_and_crackers(cheese_amount, crackers_amount)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(cheese_amount + 100, crackers_amount + 1000)


favoriteNumber()

from sys import argv
script, input_file = argv

def print_all(f):     #'f' is a file
    print(f.read())

def rewind(f):
    f.seek(0)
    #f.seek(0) will move to the start of the file, (0) being the index
                      

def print_a_line(line_count, f):
    print(line_count, f.readline())
    #f.readline() will read a line from the file and move the reader
    #to just after the \n that ends that line

    #readline() has an in-built code taht scans each byte of the file
    #until it finds a \n character, then stops reading to return what
    #it found so far.

    #there are empty lines b/w the lines in the file b/c readline()
    #returns the \n that's in the file at the end of that line.
    #add end="" at the end of print function calls to avoid adding
    #double \n to every line

current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)

print("\nNow let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions")