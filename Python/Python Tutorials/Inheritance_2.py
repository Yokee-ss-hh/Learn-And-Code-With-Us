# Multiple Inheritance : 2 base classes for 1 derived class
'''
          A                  B
          |                  |
          --------------------
                   |
                   C
'''
print("************ Method Resolution Order (MRO) *****************")
# Python uses MRO algorithm to find the method called by the derived class object. If the method called
# is not found in derived class, it goes and searches in the base classes from which derived class is inherited
# The process continues until the final base object class 'Object'.
# MRO uses Depth-First,Left-Right Traversal


class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X,Y):
    pass


class B(Y,Z):
    pass


class M(B,A,Z):
    pass


print(M.__mro__)
'''
It will check for the good head(which means does the class B inheriting from any of 
the classes which are called later, If yes then they will not added to the current search list). 
Here when it is checks for the B, It has two parent classes which are actually called 
later(Y from class A, and Z from class M), So they will not added in the search list when it checks for B.
Start MRO graph from the last derived class to upper most base class that looks like below (depth-first)
M -> B -> Y -> Object -> Z -> Object -> A -> X -> Object -> Y -> Object -> Z -> Object
Remove all duplicates except last occurring one's (left-right)
M -> B -> A -> X -> Y -> Z -> Object
In the above order,python searches for the method when called by derived class M's object.
'''


class A:

  def method(self):
    print("A.method() called")


class B:

  def method(self):
    print("B.method() called")


class C(A, B):
  pass


class D(C, B):
  pass


d = D()
d.method()
print(D.__mro__)
'''
python searches for 'method()' in 'D' class . It is not there so it looks for 'method()' in class 'C'.
In class 'C' again we have classes 'A' and 'B'. Python goes for class 'A' and finds 'method' there.
So, it prints "A.method() called"
'''
'''
The MRO for this can be a bit tricky. 
The immediate superclass for D is C, so if the method is not found in D, 
it is searched for in C. However, if it is not found in C, 
then you have to decide if you should check A (declared first in the list of C’s super classes) 
or check B (declared in D’s list of super classes after C). In Python 3 onwards, 
this is resolved as first checking A. So, the MRO becomes:
D -> C -> A -> B -> Object
'''
'''
Calculating MRO Manually,
1) depth - first : D inherits from C and B , C inherits from A and B ,A,B inherits from Object O
   MRO Graph looks like : D -> C -> A -> Object -> B -> Object -> B -> Object
2) left - right : Remove all duplicates except last one's
   Final MRO : D -> C -> A -> B -> Object
'''

print("********************* multiple inheritance example1 **************************")


class Car:

    def go(self):
        print('Going')


class Flyable:

    def fly(self):
        print('Flying')


class FlyingCar(Flyable, Car):

     pass


fc = FlyingCar()
fc.go()
fc.fly()

print("********************* multiple inheritance example2 **************************")


class Car1:
    def __init__(self, door, wheel):
        self.door = door
        self.wheel = wheel

    def start(self):
        print('Start the Car')

    def go(self):
        print('Going from Car1')


class Flyable1:
    def __init__(self, wing):
        self.wing = wing

    def start(self):
        print('Start the Flyable1 object')

    def fly(self):
        print('Flying')


class FlyingCar(Flyable1, Car1):
    def __init__(self, door, wheel, wing):
        super().__init__(wing=wing)
        self.door = door
        self.wheel = wheel

    def start(self):
        super().start()

    def go(self):
        super().go()


fc = FlyingCar('door','wheel','wing')
fc.start()
fc.go()

print(FlyingCar.__mro__)

print("********************* multiple inheritance example3 **************************")
# How super() works in multiple inheritance
# LINK : https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance
# Study the answer starts with "I want to elaborate.............."


class First(object):

  def __init__(self):

    print("First(): entering")
    super(First, self).__init__()
    print("First(): exiting")


class Second(object):

  def __init__(self):

    print("Second(): entering")
    super(Second, self).__init__()
    print("Second(): exiting")


class Third(First, Second):

  def __init__(self):

    print("Third(): entering")
    super(Third, self).__init__()
    print("Third(): exiting")


x = Third()
print(Third.__mro__)
# According to this article about Method Resolution Order by Guido van Rossum,
# the order to resolve __init__ is calculated (before Python 2.3) using a
# "depth-first left-to-right traversal" :

# Third --> First --> object --> Second --> object
# After removing all duplicates, except for the last one, we get :
# Third --> First --> Second --> object

'''
So, lets follow what happens when we instantiate an instance of the Third class, e.g. x = Third().

According to MRO Third.__init__ executes.
prints Third(): entering
then super(Third, self).__init__() executes and MRO returns First.__init__ which is called.
First.__init__ executes.
prints First(): entering
then super(First, self).__init__() executes and MRO returns Second.__init__ which is called.
Second.__init__ executes.
prints Second(): entering
then super(Second, self).__init__() executes and MRO returns object.__init__ which is called.
object.__init__ executes (no print statements in the code there)
execution goes back to Second.__init__ which then prints Second(): exiting
execution goes back to First.__init__ which then prints First(): exiting
execution goes back to Third.__init__ which then prints Third(): exiting
This details out why instantiating Third() results in to :

Third(): entering
First(): entering
Second(): entering
Second(): exiting
First(): exiting
Third(): exiting
The MRO algorithm has been improved from Python 2.3 onwards to work well in complex cases, 
but I guess that using the "depth-first left-to-right traversal" + "removing duplicates expect for the last" 
still works in most cases (please comment if this is not the case). 
Be sure to read the blog post by Guido!
LINK : http://python-history.blogspot.nl/2010/06/method-resolution-order.html
'''

print("**********************************************************************************")

print(issubclass(Third,Second))
print(issubclass(Third,First))
print(issubclass(Second,object))

print(isinstance(x,Third))
print(isinstance(x,Second))
print(isinstance(x,First))

# Lines 248,249 gives True because 'x' object class 'Third' inherits classes 'First' and 'Second'
