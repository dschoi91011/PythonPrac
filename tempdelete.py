i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i += 1
    print("Numbers now: ", numbers)

    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

#----------------------------

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

