#Collatz method

while True:
    cont = input('Cont? (y/n)')
    if cont == 'y':

        def collatz(num):
            while num != 1:
                if num % 2 == 0:
                    num = num // 2
                    print(num)
                elif num % 2 == 1:
                    num = num * 3 + 1
                    print(num)

        num = int(input('Enter: '))

        collatz(num)  #<--- executes program

    else:
        break