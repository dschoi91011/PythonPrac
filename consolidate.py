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