'''
classes , objects , constructors and destructors
setattr(),getattr(),hasattr() and delattr()
'''
'''
Every user defined classes are derived from a parent called called object and object has its parent as that class
So, If we create a user defined class and its objects, python creates a dictionary to store/track all the 
class level and instance level attributes,methods .
That dictionary can be accessed using __dict__ 
'''


class Animal:

    # class variable
    category = 'intelligent'

    def __init__(self,legs):

        # instance variable initialized using constructor and this value varies for different objects.
        self.number_of_legs = legs
        # this is also an instance variable but this is constant for all objects.
        self.height_of_animal = 'six feet'


animal = Animal(2)

print(type(animal))

print(animal.number_of_legs)  # accessing instance variable of animal object using . operator
print(animal.height_of_animal) # accessing instance variable of animal object using . operator


# We can access class variable with object / with class name directly as class variables are initialized at class level

print(Animal.category)
print(animal.category)


print(isinstance(animal,Animal))

# __dict__ example

print(Animal.__dict__) # In this o/p we will find another __dict__, this is for the object 'animal' we created
print(animal.__dict__) # This gives a dictionary with 2 instance variables of animal object as keys and values
print(vars(Animal)) # same as Class/Object_name .__dict__
print(vars(animal)) # same as object.__dict__

print('********************************************************************************')
# Alternate way to initialize class variables without initializing directly with a value
# and
# Alternate way to initialize instance variables without using constructor.


class Fruit:

    season = 'Summer'

    def __init__(self,color):

        self.color = color


fruit1 = Fruit("yellow")

fruit1.size = '10 cms' # initialized instance variable for the object fruit1 at runtime

Fruit.name = "mango" # initialized class variable for the class Fruit at runtime

print(fruit1.size, fruit1.color, fruit1)

print(Fruit.name, Fruit.season)

print(fruit1.name,fruit1.season)
# As, name variable is initialized to the class Fruit at runtime, We don't get the suggestions-
# - when we type fruit1. That's why we get the warning with brown colored box in line 59(In Pycharm).
# The warning is : Unresolved attribute reference 'name' for class 'Fruit'
# But at runtime, the error gets removed and value stored in the name variable is printed.

fruit2 = Fruit("Red")

fruit2.size = '5 cms'

print(fruit2.size, fruit2.color)

print(fruit2.season)

print(fruit2.name) # This gives o/p as mango only as name is a class variable.

print("*********************************************************************************")
# 2 objects of a class that stores same values in their instance variables are not equal


class Equality:

    def __init__(self,age,name):

        self.age = age
        self.name = name


equality1 = Equality(23,'yokesh')
equality2 = Equality(23,'yokesh')


print(equality1 == equality2)

# Although contents of both objects are equal, they evaluate to false on '==' operator.
# Equality between two objects using == operator in python checks for the same memory location.
# Since two objects take different memory locations on creation, the output for equality is False
# BUT,
# Equality between DataClass objects checks for the equality of data present in it.
# This accounts for True as output for equality check between two DataClass objects which contain same data.
# Open Data classes.py file to know more about DataClasses.

print("*********************************************************************************")

print("**********************************************************************************")
# setattr(object, attribute, value)
# getattr(object, attribute, default)
# hasattr(object, attribute)
# delattr(object, attribute)


class Agriculture:

    place = 'south india'

    def __init__(self,name):

        self.name = name


agriculture = Agriculture('Rice')  # As of now this object has name as instance variable and place as class variable

setattr(agriculture,'color','white')

print(agriculture.color) # color variable added to agriculture1 object at runtime
# Now, agriculture1 object has 2 instance variables and 1 class variable

setattr(Agriculture,'category','regular') # Added one class variable to the class Agriculture

# In total, Agriculture class has 2 class variables (one by default and one variable we initialized using setattr())

# In total, agriculture object has 2 instance variables (one by default and one using setattr())

print(Agriculture.place)    # class variable initialized at the time of class creation
print(Agriculture.category) # class variable created explicitly by us using setattr() method

print(agriculture.name) # instance variable of agriculture object created at the time of class creation
print(agriculture.color) # instance variable of agriculture object created explicitly using setattr() method
print(agriculture.place) # class variable accessing using agriculture object
print(agriculture.category) # class variable accessing using agriculture object

print("** getattr() starts from here **")

print(getattr(Agriculture,'place'))
print(getattr(Agriculture,'category'))

print(getattr(agriculture,'name'))
print(getattr(agriculture,'color'))
print(getattr(agriculture,'place'))
print(getattr(agriculture,'category'))

print(getattr(agriculture,'country','india'))
print(getattr(Agriculture,'continent','asia'))

# As, country is not a instance variable for agriculture object, we will get error,
# so default value of 'india' is returned to handle that error
# As, continent is not a class variable for Agriculture class, we will get error,
# so default value of 'asia' is returned to handle that error

print("** hasattr() starts from here **")

print(hasattr(Agriculture,'place'))
print(hasattr(Agriculture,'category'))

print(hasattr(agriculture,'name'))
print(hasattr(agriculture,'color'))
print(hasattr(agriculture,'place'))
print(hasattr(agriculture,'category'))

print("** delattr() starts from here **")

# Let's delete those class and instance variables we created using setattr() using delattr() method
# We created color instance variable of agriculture object and category class variable of Agriculture class

delattr(agriculture,'color')
delattr(Agriculture,'category')

try:

   print(Agriculture.category)

except Exception as e1 :

    print("This class variable is not available!")
    print(e1.args)

try:

   print(agriculture.color)

except Exception as e2:

    print("This instance variable is not available")
    print(e2.args)


print("*****************************************************************************************")
# Initializing class and instance variables at runtime


class City:
    pass


city = City()
city.size = '1000 acres'
city.population = '2 lakhs'

City.area = 'resident'

# Initially, Class City don't have any class and instance variables, we created them explicitly
# We can also create class and instance variables explicitly using setattr() method also.

print(city.size)
print(city.population)
print(city.area)
print(City.area)

print("***************************************************************************************")
# changing static variable content using any object only reflects for that object only
# Remaining at class level and for all other objects, static variable has the previous value only.


class Car:
    wheel_count = 4

    def __init__(self,color):
        self.color = color


car1 = Car('yellow')
car1.wheel_count = 3

car2 = Car('Blue')
car2.wheel_count = 5

print(f"car1 object has {car1.wheel_count} wheels with {car1.color} color")
print(f"car2 object has {car2.wheel_count} wheels with {car2.color} color")

print("Class variable wheel_count even after modifying by it\'s objects has a value of :",Car.wheel_count)

# Finally, class variables can be modified by the class name only.

Car.wheel_count = 10

print("Class variable modified by the class itself has a value of :",Car.wheel_count)

# Can Class name used to change/modify instance variable content ?
# No, We cannot change/modify existing instance variable content

# Different Ways to change content of instance variables


class Cookie:

    type_of_cookie = 'biscuit'

    def __init__(self,shape,ingredients):
        self.shape = shape
        self.ingredients = ingredients


cookie1 = Cookie('circlular','wheat')
print("Before Content Change : ",cookie1.shape,cookie1.ingredients)

# process1:
cookie1.shape = 'round'

# process2:
setattr(cookie1,'ingredients','eatable things')

print("After Content Change : ",cookie1.shape,cookie1.ingredients)


print("***************************************************************************************")
print("***** Destructor() *****")
'''
Destructors are called when an object gets destroyed. 
In Python, destructors are not needed as much as in C++ because Python has a garbage collector 
that handles memory management automatically. 
The __del__() method is a known as a destructor method in Python. 
It is called when all references to the object have been deleted i.e when an object is garbage collected. 
A reference to objects is also deleted when the object goes out of reference or when the program ends. 
The destructor was called after the program ended or when all the references to object are deleted i.e 
when the reference count becomes zero, not when object went out of scope.
'''


class Employee:

    # Initializing
    def __init__(self):
        print('Employee created')

    # Calling destructor
    def __del__(self):
        print("Destructor called")


def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj


print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')

print('\n')


class A:
    def __init__(self, bb):
        self.b = bb


class B:
    def __init__(self):
        self.a = A(self)

    def __del__(self):
        print("die")


def fun():
    b = B()


fun()


'''
In this example when the function fun() is called, it creates an instance of class B which passes itself to class A, 
which then sets a reference to class B and resulting in a circular reference.
Generally, Python’s garbage collector which is used to detect these types of cyclic references would 
remove it but in this example the use of custom destructor marks this item as “uncollectable”. 
Simply, it does not know the order in which to destroy the objects, so it leaves them. 
Therefore, if your instances are involved in circular references they will live in memory for 
as long as the application run.
'''

print("*********************************************************************************")

# 2 different objects with same variables stores at different places


class Test:

    def __init__(self,a,b):
        self.a = a
        self.b = b


t1 = Test(1,2)
t2 = Test(1,2)

print(t1 == t2)
print(t1 is t2)
print(t1.a == t2.a)
print(t1.b == t2.b)
print(t1.a is t2.a)
print(t1.b is t2.b)
print(isinstance(t1,Test))
print(isinstance(t2,Test))

# Note : As we know destructors are called at the end of the whole program
# That's why destructor in example 1 is called after the execution of example2 i.e, at the end of the complete file.


print("*********************************************************************************")
# 2 objects of a class that stores same values in their instance variables are not equal


class Equality:

    def __init__(self,age,name):

        self.age = age
        self.name = name


equality1 = Equality(23,'yokesh')
equality2 = Equality(23,'yokesh')


print(equality1 == equality2)

# Although contents of both objects are equal, they evaluate to false on '==' operator.
print("*********************************************************************************")
