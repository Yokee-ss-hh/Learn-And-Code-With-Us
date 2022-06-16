# Polymorphism in Python is the ability of an object to take many forms.
# In simple words, polymorphism allows us to perform the same action in many different ways.

print("********** polymorphism in inbuilt methods **************")
# same '+' and 'len()' on 2 different types of objects

print(2+3)
print('Yok'+'esh')

print(len('hello bro'))
print(len(bin(23)))


print("************* polymorphism in classes ****************")
# Different classes with same method names comes under polymorphism


class A:

    def disp(self):

        print("I am from class A")


class B:

    def disp(self):

        print("I am from class B")


a = A()
b = B()

a.disp()
b.disp()

print("************ polymorphism in user defined functions *************")
# Python does not allow us to create 2 or more functions with the same name, if we do so
# it will take the latest created function and ignores the remaining functions


def m1():

    print("I am first")


def m1():

    print("I am second")


m1() # calls line 48 and ignores line 43


# First product method.
# Takes two argument and print their
# product
def product(a, b):
    p = a * b
    print(p)


# Second product method
# Takes three argument and print their
# product
def product(a, b, c):
    p = a * b * c
    print(p)


# Uncommenting the below line shows an error
# product(4, 5)

# This line will call the second product method
product(4, 5, 5)

print("****************** Function Overloading *********************")
# In python, function overloading is defined as the ability of the function to
# behave in different ways depend on the number of parameters passed to it
# like zero, one, two which will depend on how function is defined.
# Overloading function provides code reusability, removes complexity and improves
# code clarity to the users who will use or work on it. Function overloading in python
# can be of two types one is overloading built-in functions and overloading the
# custom or user-defined functions in python.
# As from above example, if we declare 2 functions with same name python takes last declared function only
# Then how to define function overloading ?
# Let's see


class Compute:

    def area(self, x=None, y=None):

          if x!=None and y !=None:
              return x*y
          elif x!=None:
              return x*x
          else:
              return 0


obj = Compute()
print(obj.area())
print(obj.area(6))
print(obj.area(2,8))

# In lines 81 to 83, we are calling same method by varying number of parameters
# Hence this is considered as function overloading

print("*******************")


class Student:

    def __init__(self):
        pass

    def sayHello(self, name=None):
        if name is not None:
            self.name = name
            print("Hey", name)
        else:
            print("Hey")


stu = Student()
stu.sayHello()
stu.sayHello("Yokesh")

print("*******************")


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()

print("*******************")
# function overloading using *args and **kwargs


def overload_array_of_integers(x,*args ,**kwargs):

     if x and len(args) == 0 and len(kwargs) == 0:

         print("Value received is : ",x)

     elif x > 0 and len(args) > 0 and len(kwargs) == 0:

         print("Sum of x and args is :",x+sum(args))

     elif x > 0 and len(args) > 0 and len(kwargs) > 0:

         print("sum of x , args and kwargs is :",x + sum(args) + sum(list(kwargs.values())))


overload_array_of_integers(5)
overload_array_of_integers(1,2,3,4,5,6,7,8,9,10)
overload_array_of_integers(1,2,3,4,5,6,7,8,9,10,eleven=11,twelve=12)

print("********************* Method Overriding ************************")
'''
Method overriding is an ability of any object-oriented programming language that allows 
a subclass or child class to provide a specific implementation of a method that is already 
provided by one of its super-classes or parent classes. When a method in a subclass has the 
same name, same parameters or signature and same return type(or sub-type) as a method in its super-class,
then the method in the subclass is said to override the method in the super-class.
'''
'''
The version of a method that is executed will be determined by the object that is used to invoke it. 
If an object of a parent class is used to invoke the method, then the version in the parent class 
will be executed, but if an object of the subclass is used to invoke the method, then the version in 
the child class will be executed. In other words, it is the type of the object 
being referred to (not the type of the reference variable) that determines which version 
of an overridden method will be executed.
'''

print("*********** Overriding in single inheritance ***************")


class Parent():

    # Constructor
    def __init__(self):
        self.value = "Inside Parent"

    # Parent's show method
    def show(self):
        print(self.value)


# Defining child class
class Child(Parent):

    # Constructor
    def __init__(self):
        self.value = "Inside Child"

    # Child's show method
    def show(self):
        print(self.value)


# Driver's code
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()


print("*********** Overriding in multiple inheritance ***************")


class Parent1():

    # Parent's show method
    def show(self):
        print("Inside Parent1")


# Defining Parent class 2
class Parent2():

    # Parent's show method
    def display(self):
        print("Inside Parent2")


# Defining child class
class Child1(Parent1, Parent2):

    # Child's show method
    def show(self):
        print("Inside Child1")


# Driver's code
obj11 = Child1()

obj11.show()
obj11.display()

print("*********** Overriding in multi-level inheritance ***************")


class Parentt():

    # Parentt's show method
    def display(self):
        print("Inside Parentt")


# Inherited or Sub class (Note Parentt in bracket)
class Childd(Parentt):

    # Childd's show method
    def show(self):
        print("Inside Childd")


# Inherited or Sub class (Note Childd in bracket)
class GrandChildd(Childd):

    # Childd's show method
    def show(self):
        print("Inside GrandChildd")

    # Driver code


g = GrandChildd()
g.show()
g.display()

print("********* Calling the Parent’s method within the overridden method using class name **********")


class Parrent():

    def show(self):
        print("Inside Parrent")


class Chhild(Parrent):

    def show(self):
        # Calling the parrent's class
        # method
        Parrent.show(self)
        print("Inside Chhild")


# Driver's code
objj = Chhild()
objj.show()

print("********* Calling the Parent’s method within the overridden method using super() **********")


class Parennt():

    def show(self):
        print("Inside Parennt")


class Chilld(Parennt):

    def show(self):
        # Calling the parennt's class
        # method
        super().show()
        print("Inside Chilld")


# Driver's code
objjj = Chilld()
objjj.show()


print("*****************************************************************************")
print("Method Overloading vs Method Overriding")
'''
Method Overloading is an example of Compile time polymorphism. 
In this, more than one method of the same class shares the same method name having different signatures.
Method overloading is used to add more to the behavior of methods and there is no need of more 
than one class for method overloading.
Note: Python does not support method overloading. 
We may overload the methods but can only use the latest defined method.
'''

'''
Method overriding is an example of run time polymorphism.
In this, the specific implementation of the method that is already provided by the parent class
is provided by the child class. It is used to change the behavior of existing methods and there
is a need for at least two classes for method overriding.
In method overriding, inheritance always required as it is done between parent class(superclass)
and child class(child class) methods.
'''
print("******************************************************************************")
