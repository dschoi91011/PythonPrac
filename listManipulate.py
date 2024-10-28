ten_things = "apples oranges crows telephone light sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ') #Converts string into list
more_stuff = ["day", "night", "song", "frisbee", "corn",
              "banana", "girl", "boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() #removes last item from "more_stuff" list
    print("Adding: ", next_one)
    stuff.append(next_one) #adds "next_one" variable to "stuff" list
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.\n")

print(stuff[1]) #index 2nd item
print(stuff[-1]) #index last item
print(stuff.pop()) #remove last item
print(' '.join(stuff)) #joins list item into one string
print('#'.join(stuff[3:5])) #joins index list items into string

      
