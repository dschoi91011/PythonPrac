the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges' ,'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in change:
    print(f"I got {i}")
    break

print("\n")


elements = []
for i in range(0, 6):
    print(f"Adding {i} to the list")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")

    
for i in elements:
    print(f"{i}", end = ' ')
print("\n")

for i in elements:

    if i > 1:
        print("It's too big")
        break

    else:
        print("Keep going")
        

def numbers():
    i = 0
    numbers = []
    x = int(input("number: "))
    n = int(input("increment: "))

    while i < x:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += n
        print("Numbers now: ", numbers)

        print(f"At the bottom i is {i}")


while True:
    query = input("Input new number (y/n): ")
    
    if query == "y":
        numbers()

    elif query == "n":
        break

def secondary():
    x = int(input("first: "))
    n = int(input("last: "))
    r = int(input("increment: "))

    for i in range(x, n, r):
        print(i, end= ' ')

secondary()
