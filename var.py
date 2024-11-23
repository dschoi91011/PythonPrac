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