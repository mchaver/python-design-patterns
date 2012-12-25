#Prototype pattern

#discussion at
#http://code.activestate.com/recipes/86651-prototype-pattern/

from copy import deepcopy

class Prototype:
    def __init__(self):
        self._objects = dict()
    def registerObject(self, name, object):
        self._objects[name] = object
    def unregisterObject(self, name):
        del self._objects[name]
    def clone(self, name, **attr):
        object = deepcopy(self._objects[name])
        object.__dict__.update(attr)
        return object

class A:
    pass

a = A()
prototype = Prototype()
prototype.registerObject("a", a)
b = prototype.clone("a", a = 1, b = 2, c = 3)

print(a)
print(b.a,b.b,b.c)