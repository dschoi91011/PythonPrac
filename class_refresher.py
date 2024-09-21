#define new type called "Person"
#this object should have a 'name' attribute
    #attribute: variable of class that is shared b/w all of its instances
#this object should have a 'talk' method

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print('talk')


john = Person('John Smith')
print(john.name)

john.talk()

########################

class PersonTwo:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f"Hi, my name is {self.name}.")


bass = PersonTwo('Bass Choi')
sharon = PersonTwo('Sharon Lee')
bass.talk()
sharon.talk()
