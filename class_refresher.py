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

#########################

class One:
    def __init__(self, two):
        self.two = two

    def three(self):
        print(self.two)

    def five(self):
        print('some other text\n')

four = One('anything')
four.three()
four.five()

class Head:
    def __init__(self, toes):
        self.toes = toes

    def liver(self):
        print(self.toes, '\n')

    def kidney(self):
        for x in self.toes:
            print(x)

    def pancreas(self):
        jericho = "somethin' for nothin'"
        for x in jericho:
            print(x, end = '')

anatomy = Head('i drink a lot')
anatomy.liver()
anatomy.kidney()
anatomy.pancreas()

######################

class AAA:
    def __init__(self, one):
        self.one = one

    def BBB(self):
        print('something')

    def CCC(self):
        print('whatever', self.one)

var1 = AAA('xxx text xxx')
var1.CCC()
var1.BBB()

print('Hello world')