#Decorator Pattern
#Allows behavior to be added to an existing object dynamically, works as an alternative
#to subclassing. It can provide new behavior at run-time for individual objects.

#Often used on streams

#Subclass the original Decorator class into a Component class
#In the decorator class, add a component pointer as a field
#Pass a component to the decorator constructor to initialize the component pointer
#In Decorator class, redirect all Component methods to the Component point
#In the ConcreteDecorator class, override any component methods whose behavior needs to be
#modified


class tree(object):
    def get_appearance(self):
        print("the tree is green")
    def get_height(self):
        print("the tree is tall")
        
class tree_decorator(object):
    def __init__(self, decoratee):
        self._decoratee = decoratee
        #if you want to use the same class
        #self.__class__ = decoratee.__class__
    def get_appearance(self):
        print("the tree is green and covered in christmas lights")
    def __getattr__(self, name):
        return getattr(self._decoratee, name)
        


pine_tree = tree()
xmas_tree = tree_decorator(pine_tree)

pine_tree.get_appearance()
pine_tree.get_height()
xmas_tree.get_appearance()
xmas_tree.get_height()
