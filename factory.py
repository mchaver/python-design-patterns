#Factory pattern
#Common in toolkits and frameworks where library code needs to create objects of types 
#that may be subclassed
#Also used in test-drive development to allow classes to be put under a test.
class ObjectOne:
    def __init__(self):
        self.msg = "This is object one"
    def get(self):
        return self.msg
        
class ObjectTwo:
    def __init__(self):
        self.msg = "This is object two"
    def get(self):
        return self.msg

class ObjectThree:
    def __init__(self):
        self.msg = "This is object three"
    def get(self):
        return self.msg

#an interface for creating objects in which the factory decides which object to create
def factory(object):
    """Objects must be registered with the factory"""
    objects = dict(One=ObjectOne, Two=ObjectTwo, Three=ObjectThree)
    if object in objects:
        return objects[object]()
    else:
        return None
        
#use a string to pick an object and the factory will return it
one, two, three = factory("One"), factory("Two"), factory("Three")

print one.get()
print two.get()
print three.get()

class Chicken:
    def __init__(self):
        self.sound = "Bawk!"
    def make_sound(self):
        return self.sound
        
class Dog:
    def __init__(self):
        self.sound = "Ruff!"
    def make_sound(self):
        return self.sound
        
class Horse:
    def __init__(self):
        self.sound = "Neigh!"
    def make_sound(self):
        return self.sound

def AnimalFactory(animalOrSound):
    animals = {"Chicken" : Chicken, "Dog" : Dog,"Horse" : Horse}
    sounds = {"Bawk!" : Chicken, "Ruff!" : Dog, "Neigh!" : Horse}
    if animalOrSound in animals:
        return animals[animalOrSound]()
    elif animalOrSound in sounds:
        return sounds[animalOrSound]()
    else:
        return None
        
first, second, third = AnimalFactory("Ruff!") , AnimalFactory("Chicken"), AnimalFactory("Neigh!")
print first.make_sound()
print second.make_sound()
print third.make_sound()