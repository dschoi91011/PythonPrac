#create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#create a basic set of states and cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print some states
print('-' * 10)
print("Michigan's abbr is: ", states['Michigan'])
print("Florida's abbr is: ", states['Florida'])

#do so by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every state abbr
print('-' * 10)
for state, abbrev in list(states.items()):
      print(f"{state} is abbreviated {abbrev}")

#print every city in state
for abbrev, city in list(cities.items()):
    print(f"{abbrev}has the city {city}")

#now do both at the same time
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

#get an abbreviation by state that might not be there
state = states.get('Texas')
if not state:
    print("Sorry, no Texas")

#get a city with a default value
    city = cities.get('TX', 'Does not exist')
    print(f"THe city for the state 'TX' is: {city}")
