from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}: ")
print(txt.read())

print("Type filename: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

######################################

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

###########################################

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
