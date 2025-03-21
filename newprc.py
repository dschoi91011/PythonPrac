#message = "hello world"
#print(message)

#name = "ada lovelace"
#print(name.title())

#first_name = "ada"
#last_name = "lovelace"
#full_name = f"{first_name} {last_name}"
#print(full_name)

#print(f"Hello, {full_name.title()}!")
#print("\tPython")

#print("Languages:\n\tEnglish\n\tKorean \n\tSpanish")
#print("\t\tsecondary bullet point")

#variable = "Eric"
#print(f"Hello, {variable.title()}! This is a test run.")
#print("This\n\tis\n\t\talso\n\t\t\tsome\n\t\ttest\n\trun")

#famous_person = "Albert Einstein"
#message = f"{famous_person} formulated the theory of relativity."
#print(message)

#famous_person = "Albert Einstein"
#message = "was a college dropout."
#total_message = f"{famous_person} {message}"
#print(total_message)

#print(4*5)
#integer = 4*5
#print(f"\t{integer}")
#favorite_number = 13
#print(f"My favorite number is: \n{favorite_number}")

#LISTS -------------------------------------------------------------------------------------
"""
trump_cards = ['aces', 'kings', 'queens', 'jacks']
print(trump_cards[0])
print(trump_cards[0].title())
message = f"A pair of {trump_cards[0].title()} is a powerful starting hand."
print(message)

fast_food = ['mcdonalds', 'jack', 'del taco']
print(fast_food)
fast_food[1] = 'wendys'
print(fast_food)
fast_food.append('jack')
print(fast_food)
fast_food.insert(2, 'sonics')
print(fast_food)
del fast_food[1]
print(fast_food)

ate_it = fast_food.pop(0)
print(fast_food)
print(ate_it)
print(f"I have way too much {ate_it.title()} for my own good.")

fast_food.remove('jack')
print(fast_food)

cars = ['bmw','infiniti', 'honda', 'toyota', 'volvo']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
"""
#LOOPS -------------------------------------------------------------------------------------
"""
cars = ['bmw', 'audi', 'infiniti']
favorite = cars[2]
print(f"I have {len(cars)} cars in my list.")
#for car in cars:
#	print(car)
#	print(f"The manufacturer {car.title()} builds great cars.\n")
#print(f"I like the {favorite.title()} most.\n")
#for value in range(6):
#	print(value)
#	numbers = list(range(5))
#	print(numbers)

#exponents = []
#for value in range(10):
#	exponents.append(value**2)
#	print(exponents)

#add_numbers = list(range(0,16,3))
#print(add_numbers)

#digits = [1, 3, 5, 6, 7, 9, 0]
#print(f"The following include: \n\t{min(digits)} \n\t{max(digits)} \n\t{sum(digits)}")

#exponents = [value**2 for value in range(5)]
#print(exponents)
"""
"""
for value in range(20):
	numerals = list(range(20))
	sum(numerals)
print(f"{sum(numerals)}")

cube = []
for value in range(10):
	cube.append(value**3)
	print(cube)

straight = ['ten', 'jack', 'queen', 'king', 'ace']
print(straight[:3])
print(straight[1:3])
print(straight[3:])

print("\nIf I'm dealt an Ace and a King, I would need the following by the river for a straight:")
for win in straight[:3]:
	print(win.title())

firstList = ['alpha', 'bravo', 'charlie']
secondList = firstList[:]
print(firstList)
secondList.append('delta')
print(secondList)

print("I will now count my chickens:")
print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)
print("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2< 5 - 7)
print("What is 3 + 2?", 3 + 2)
print("WHat is 5-7?", 5 - 7)
print("Oh, that's why it's False.")
print("Is it greater?", 5>-2)
print("Is it greater or equal?", 5>=-2)
print("Is it less or equal?", 5 <= -2)

someList = ['able', 'baker', 'charlie']
someList.append('denver')
print(someList)

print('The number', 4 + 4, 'is a factor of 2.')

cars_owned = ['volvo', 'acura', 'toyota', 'infiniti']
'subaru' in cars_owned
'infiniti' in cars_owned
car_owned = 'subaru'
print(car_owned == 'subaru')
print(car_owned == 'infiniti')

sodas = ['coke', 'sprite', 'pepsi']
for soda in sodas:
	if soda == 'coke':
		print(f"{sodas[0].title()} is my favorite soda.")
	elif soda == 'sprite':
		print("Sprite is okay too.")
	elif soda == 'pepsi':
		print("Pepsi is a poor replacement for coke.")
	else:
		print("I don't drink that.")
"""