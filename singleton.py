# Singleton
# various implementations at
# http://code.activestate.com/recipes/52558/ 

#simple

class _Singleton(object):
    def __init__(self):
        #to show that they are the same object
        self.instance = "Instance at %d" % self.__hash__()
        self.test = None
    def setTest(self, test):
        self.test = test
    def getTest(self):
        return self.test
        
_singleton = _Singleton()

def Singleton(): return _singleton

s1 = Singleton()
s2 = Singleton()

s1.setTest("Hello, this is set in s1")
print s1.getTest()
print s2.getTest()


#with inheritance

class Singleton2(object):
    __single = None
    
    def __new__(classtype, *args, **kwargs):
        if classtype != type(classtype.__single):
            classtype.__single = object.__new__(classtype, *args, **kwargs)
        return classtype.__single
    def __init__(self, name = None):
        self.name = name
    def display(self):
        print self.name, id(self), type(self)

class Subsingleton(Singleton2):
    pass
    
s1 = Singleton2("foo")
s1.display()
s2 = Singleton2("bar")
s1.display()
s2.display()

#with Python decorator, similar to above

class Singleton3(object):
    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = cls(*args, **kwargs)
        return cls._instance
        
s1 = Singleton3()
s2 = Singleton3()