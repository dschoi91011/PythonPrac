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
