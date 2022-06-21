print("***************************************************************************")
print("************* Descriptor and its protocols *******************")

# First We Need To Understand about __dict__ , vars() and __mro__ , mro() in python
# mro = method resolution order


class Dict:

    name = 'dictionary'

    def __init__(self,a):

        self.a = a


dict_obj = Dict(10)
print(dict_obj.a)
print(Dict.name)

print(Dict.__dict__)
print(vars(Dict))

print(dict_obj.__dict__)
print(vars(dict_obj))

print(Dict.__dict__['name'])
print(type(dict_obj).__dict__['name'])

print(dict_obj.__dict__['a'])


'''
To understand a little more about Python descriptors and Python internals, 
you need to understand what happens in Python when an attribute is accessed. 
In Python, every object has a built-in __dict__ attribute. 
This is a dictionary that contains all the attributes defined in the object itself.
'''
# If i want to access some data using object - dot operator like

print(dict_obj.a)
# and
print(dict_obj.name)

# What happens here internally is :

'''
So, what happens when you access the attribute of an object with dot notation? 
How does the interpreter know what you really need? 
Well, here’s where a concept called the lookup chain comes in
'''

# These below steps are followed !
'''
First, you’ll get the result returned from the __get__ method of the data descriptor 
named after the attribute you’re looking for.

If that fails, then you’ll get the value of your object’s __dict__ for the key named 
after the attribute you’re looking for.

If that fails, then you’ll get the result returned from the __get__ method of 
the non-data descriptor named after the attribute you’re looking for.

If that fails, then you’ll get the value of your object type’s __dict__ for 
the key named after the attribute you’re looking for.

If that fails, then you’ll get the value of your object parent type’s __dict__ for the 
key named after the attribute you’re looking for.

If that fails, then the previous step is repeated for all the parent’s types in the 
method resolution order of your object.

If everything else has failed, then you’ll get an AttributeError exception.
'''

# Now, Whenever object's instance variables are initialized with some value in the constructor of a class as
# self.a = a . Internally, this line calls __set__() method if available in it's parent class i.e, this object
# calls __set__() method from object class which is the base class for all user defined classes that contains
# pre-defined body for __set__() method.
# This __set__() method sets the value to the variable 'a' with the value we passed using __dict__() method as
# If we passed 10 as value, then __get__() method in the parent class of our user-defined class takes this value
# and object as it's parameters and assigns this value to the object's dictionary as,
# sample_obj.__dict__['a'] = 10

# If later in my class if i want to print sample_obj.a , then same process will happen .
# As soon as python encounters print(sample_obj.a), it looks for the __get__() method of it's parent class
# If there is no parent class, then object is taken as parent because object is the base class of all user defined
# classes
# There python will be having a method called __get__() that takes object as a parameter and returns
# sample_obj.__dict__['a']

# If any object implements these dunder methods in them , then they are called descriptors

# Descriptors are Python objects that implement a method of the descriptor protocol, which gives you the ability to
# create objects that have special behavior when they’re accessed as attributes of other objects.

'''
__get__(self, obj, type=None) -> object
__set__(self, obj, value) -> None
__delete__(self, obj) -> None
__set_name__(self, owner, name)
These are the 4 methods every user defined class calls from it's base class 'object' while
assigning values to variables and while getting values from assigned variables.
'''
# If your descriptor implements just .__get__(), then it’s said to be a non-data descriptor.
# If it implements .__set__() or .__delete__(), then it’s said to be a data descriptor.

# As we know if we create a class , this class implicitly make use of these descriptor methods which
# are pre-defined in its base class 'object'. But we are not using default base class 'object'.
# Let's make our own base class for our class as,

print("*********** Python Descriptor Example *************")
'''
If you want to use Python descriptors in your code, then you just need to implement the descriptor protocol. 
The most important methods of this protocol are .__get__() and .__set__(), which have the following signature:

__get__(self, obj, type=None) -> object
__set__(self, obj, value) -> None
When you implement the protocol, keep these things in mind:

self is the instance of the descriptor you’re writing.
obj is the instance of the object your descriptor is attached to.
type is the type of the object the descriptor is attached to.
In .__set__(), you don’t have the type variable, because you can only call .__set__() on the object. 
In contrast, you can call .__get__() on both the object and the class.

Another important thing to know is that Python descriptors are instantiated just once per class. 
That means that every single instance of a class containing a descriptor shares that descriptor instance. 
This is something that you might not expect and can lead to a classic pitfall, like this:
'''


class OneDigitNumericValue():
    def __init__(self):
        self.value = 0

    def __get__(self, obj, type=None) -> object:
        return self.value

    def __set__(self, obj, value) -> None:
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError("The value is invalid")
        self.value = value


class Foo():
    number = OneDigitNumericValue()

my_foo_object = Foo()
my_second_foo_object = Foo()
my_third_foo_object = Foo()

my_foo_object.number = 3
print(my_foo_object.number)         # o/p = 3
print(my_second_foo_object.number)  # o/p = 3
print(my_third_foo_object.number)  # o/p = 3

'''
Here, you have a class Foo that defines an attribute number, which is a descriptor. 
This descriptor accepts a single-digit numeric value and stores it in a property of the descriptor itself. 
However, this approach won’t work, because each instance of Foo shares the same descriptor instance.
What you’ve essentially created is just a new class-level attribute.
You can see that all the instances of Foo have the same value for the attribute number, 
even though the last one was created after the my_foo_object.number attribute was set.
So, how can you solve this problem? You might think that it’d be a good idea to use a dictionary 
to save all the values of the descriptor for all the objects it’s attached to. 
This seems to be a good solution since .__get__() and .__set__() have the obj attribute, 
which is the instance of the object you’re attached to. 
You could use this value as a key for the dictionary.
'''


class OneDigitNumericValue1():
    def __init__(self):
        self.value1 = {}

    def __get__(self, obj1, type=None) -> object:
        try:
            return self.value1[obj1]
        except:
            return 0

    def __set__(self, obj1, value1) -> None:
        if value1 > 9 or value1 < 0 or int(value1) != value1:
            raise AttributeError("The value is invalid")
        self.value1[obj1] = value1


class Foo1():
    number1 = OneDigitNumericValue1()

my_foo_object1 = Foo1()
my_second_foo_object1 = Foo1()

my_foo_object1.number1 = 3
print(my_foo_object1.number1)
print(my_second_foo_object1.number1)

my_third_foo_object1 = Foo1()
print(my_third_foo_object1.number1)

'''
Unfortunately, the downside here is that the descriptor is keeping a strong reference to the owner object. 
This means that if you destroy the object, then the memory is not released because the 
garbage collector keeps finding a reference to that object inside the descriptor!

You may think that the solution here could be the use of weak references. 
While that may, you’d have to deal with the fact that not everything can be referenced as 
weak and that, when your objects get collected, they disappear from your dictionary.

The best solution here is to simply not store values in the descriptor itself, 
but to store them in the object that the descriptor is attached to. Try this approach next:
'''


class OneDigitNumericValue2():
    def __init__(self, name2):
        self.name2 = name2

    def __get__(self, obj2, type=None) -> object:
        return obj2.__dict__.get(self.name2) or 0

    def __set__(self, obj2, value2) -> None:
        obj2.__dict__[self.name2] = value2


class Foo2():
    number2 = OneDigitNumericValue2("number")

my_foo_object2 = Foo2()
my_second_foo_object2 = Foo2()

my_foo_object2.number2 = 3
print(my_foo_object2.number2)
print(my_second_foo_object2.number2)

my_third_foo_object2 = Foo2()
print(my_third_foo_object2.number2)

'''
In this example, when you set a value to the number attribute of your object, 
the descriptor stores it in the __dict__ attribute of the object it’s attached 
to using the same name of the descriptor itself.

The only problem here is that when you instantiate the descriptor you have to specify the name as a parameter:

number = OneDigitNumericValue("number")
Wouldn’t it be better to just write number = OneDigitNumericValue()? 
It might, but if you’re running a version of Python less than 3.6, 
then you’ll need a little bit of magic here with metaclasses and decorators. 
If you use Python 3.6 or higher, however, then the descriptor protocol has a 
new method .__set_name__() that does all this magic for you, as proposed in PEP 487:

__set_name__(self, owner, name)
With this new method, whenever you instantiate a descriptor this method is 
called and the name parameter automatically set.
'''


class OneDigitNumericValue3():
    def __set_name__(self, owner, name3): # owner = Foo3 class , self = number 3 object , name3 comes from line 281
        self.name3 = name3

    def __get__(self, obj3, type=None) -> object:
        return obj3.__dict__.get(self.name3) or 0

    def __set__(self, obj3, value3) -> None:
        obj3.__dict__[self.name3] = value3


class Foo3():

    number3 = OneDigitNumericValue3()


my_foo_object3 = Foo3()
my_second_foo_object3 = Foo3()
my_third_foo_object3 = Foo3()


my_foo_object3.number3 = 3
print(my_foo_object3.number3)
print(my_second_foo_object3.number3)
print(my_third_foo_object3.number3)

'''
Now, .__init__() has been removed and .__set_name__() has been implemented. 
This makes it possible to create your descriptor without specifying the name of the 
internal attribute that you need to use for storing the value. Your code also looks nicer and cleaner now!
'''

print("*****************************************************************************************")


class Sample:

    def __set_name__(self, owner, name):

        self.fullname = name

    def __set__(self, instance, value):

        instance.__dict__['fullname'] = value+"yokesh"

    def __get__(self, instance, owner):

        return instance.__dict__['fullname'].upper()


class DerivedSample(Sample):

    sample = Sample()


derived_sample = DerivedSample()

derived_sample.sample = 'tommy'  # Invokes method starts on line 367

print(derived_sample.sample)    # Invokes method starts on line 371

# Here, we setted a value of object using dot-operator to 'tommy'
# After setting, we accessed and we got output as 'TOMMYYOKESH'
# That means we are manipulating the data we setted to an object using dot operator implicitly
# using descriptors

print("***************************************************************************************")


class Fruits:

    def __init__(self):

        self.fruits = None

    def __getattr__(self, item):

        print("I am get attribute")
        return self.__dict__.get(item,None)

    def __setattr__(self, key, value):

        print("I am set attribute")
        self.__dict__[key] = value

    def __delattr__(self, item):

        print("I was called by Fruits() object and i deleted ",item)
        self.__dict__.__delitem__(item)


fruit_obj = Fruits()

fruit_obj.fruits = "mango"

print(fruit_obj.fruits)

fruit_obj.__delattr__('fruits')

print(fruit_obj.fruits) # returns None as we provided 'None' as default argument in line 404.


print("***************************************************************************************")
print("Property Vs Descriptor")

# descriptors are a low-level mechanism that lets you hook into an object's attributes being accessed.
# Properties are a high-level application of this; that is, properties are implemented using descriptors.
# Or, better yet, properties are descriptors that are already provided for you in the standard library.

# Descriptor Example :


class Celsius( object ):

    def __init__( self, value=0.0 ):
        self.value= float(value)

    def __get__( self, instance, owner ):
        return instance.value

    def __set__( self, instance, value ):
        instance.value= float(value)


class Farenheit( object ):

    def __get__( self, instance, owner ):
        return instance.celsius * 9 / 5 + 32

    def __set__( self, instance, value ):
        instance.celsius= (float(value)-32) * 5 / 9


class Temperature( object ):
    celsius= Celsius()
    farenheit= Farenheit()


oven = Temperature()
oven.farenheit = 450
print(oven.celsius)
oven.celsius = 175
print(oven.farenheit)


oven1 = Temperature()
oven1.farenheit = 900
print(oven1.celsius)
oven1.celsius = 78
print(oven1.farenheit)


# Property Example :

class Temperature1( object ):

    def fget(self):
        return self.celsius1 * 9 / 5 + 32

    def fset(self, value1):
        self.celsius1 = (float(value1)-32) * 5 / 9

    def cset(self, value1):
        self.cTemp = float(value1)

    def cget(self):
        return self.cTemp

    celsius1 = property( cget, cset, doc="Celsius temperature" )
    farenheit1 = property(fget, fset,doc="Farenheit temperature")


oven2 = Temperature1()
oven2.farenheit1 = 450
print(oven2.celsius1)
oven2.celsius1 = 175
print(oven2.farenheit1)

oven3 = Temperature1()
oven3.farenheit1 = 900
print(oven3.celsius1)
oven3.celsius1 = 78
print(oven3.farenheit1)

# As we can see using both descriptors and property we are getting same result
# Property are made over descriptors and are very easy to use
# property are high level descriptors
# properties are coded over descriptors

print("**********************************************************************************")

# The below topic is not related to descriptor but related to normal class and objects

print("************ __getattr__  vs __getattribute__  vs getattr() ****************")

# __getattr__ gets called if there is no attribute in the instance
# It is invoked 'last' , if python cannot find that attribute
# __getattr__ has lowest pripority

# 1) __getattribute__ gets called all the times whether there is the attribute or not
# 2) It is invoked first(highest priority)
# 3) So, even if there is the attribute in the instance, python calls __getattribute__ first
#    with the attribute as an argument


# getattr() has 2 or 3 parameters
# getattr(myobj,myattribute) is same as myobj.getattribute(myattribute)
# The 3rd argument is default attribute

class A:

    def __getattr__(self, name):

        return ('hahahaha'+name)


a = A()
a.ace = 'ace value'

print(a.ace)
print(a.ace2)
print(a.__dict__)

# python could find 'ace' , so prints the value of 'ace'
# But, 'ace2' cannot be found, so __getattr_ is invoked.
# If we print a.__dict__ , we can see the attribute 'ace' with value of it

# What if we add __getattribute__ to class 'A'


class A1:

    def __getattr__(self, name1):

        return ('hahahaha'+name1)

    def __getattribute__(self, name2):

        return ('holaaaaaa'+name2)


a1 = A1()
a1.ace1 = 'ace value1'

print(a1.ace1)
print(a1.ace2_2)
print(a1.__dict__)

# 1) Even though we assigned a value 'ace value1' to the attribute 'ace1'
# __getattribute__ is invoked first . Python doesn't even try to find 'ace1'
# 2) 'ace2_2' does not exist .So, __getattribute__ is called here not __getattr__
# 3) If we see the output of a1.__dict__, we can again conclude that __getattribute__ is invoked
# 'first', the highest priority

# In short,
# __getattribute__ gets called "first"(the highest priority),whether or not there is the attribute
# __getattr__ gets called "last"(the lowest priority), if python cannot find the attribute

# __getattr__(self,name) is invoked by self.name if name does not exist
# __setattr__(self,name,value) is invoked by self.name = value
# __delattr__(self,name) is invoked by del self.name
# __getattribute__(self,name) is invoked by self.name ,if name exists.


print("**********************************************************************************")

# objects uses __getattr__, __setattr__ and __delattr__ to get a value, set a value and delete a value of the respective object.
# derived classes uses __get__, __set__ and __del__ that are defined in the base class(descriptor) to achieve property in python.
# To understand above line, see line 295 . That's how property in python works internally.
# Descriptors are the ones used to create a property by python internally.

print("**********************************************************************************")

# classes vs descriptors

class Apple:

    def __getattr__(self, item):

        return self.__dict__[item]

    def __setattr__(self, key, value):

        self.__dict__[key] = value

    def __delattr__(self, item):

        del self.__dict__[item]


apple = Apple()
apple.name = 'simla apple'
apple.color = 'red'
print(apple.name)
print(apple.color)

del apple.name

print(vars(apple)) # Notice that 'name' got deleted from the object's variable


# Classes implement __getattr__,__setattr__ and __delattr__


# Descriptors


class Descriptor:

    def __init__(self):
        self.__fuel_cap = 0

    def __get__(self, instance, owner):
        return self.__fuel_cap

    def __set__(self, instance, value):
        if isinstance(value, int):
            print(value)
        else:
            raise TypeError("Fuel Capacity can only be an integer")

        if value < 0:
            raise ValueError("Fuel Capacity can never be less than zero")

        self.__fuel_cap = value

    def __delete__(self, instance):
        del self.__fuel_cap


class Car:
    fuel_cap = Descriptor()
    def __init__(self,make,model,fuel_cap):
        self.make = make
        self.model = model
        self.fuel_cap = fuel_cap

    def __str__(self):
        return "{0} model {1} with a fuel capacity of {2} ltr.".format(self.make,self.model,self.fuel_cap)


car2 = Car("BMW","X7",40)
print(car2)

'''
The __init__() method of the Descriptor class has a local variable __fuel_cap to zero. 
The dunder or a double underscore at the beginning of it means that the variable is private. 
Having a dunder, in the beginning, is only to distinguish the fuel capacity attribute of 
Descriptor class with the Car class.
As you know by now, the __get__() method is used to retrieve the attributes, 
and it returns the variable fuel capacity. 
It takes three arguments the descriptor object, instance of the class that contains the descriptor 
object instance, i.e., car2 and finally the owner, which is the class to which the instance belongs, 
i.e., the Car class. In this method, you simply return the value attribute, i.e., 
the fuel_cap whose value is set in the __set__() method.
The __set__() method is invoked when the value is set to the attribute, 
and unlike the __get__() method, it returns nothing. It has two arguments apart from the 
descriptor object itself, i.e., the instance which is the same as the __get__() method and the 
value argument, which is the value you assign to the attribute. 
In this method, you check whether the value you would like to assign to the fuel_cap attribute 
is an integer or not. If not, you raise a TypeError exception. 
Then, in the same method, you also check whether the value is less than zero if it is 
then you raise another exception but this time a ValueError exception. 
After checking for errors, you update the fuel_cap attribute equal to the value.
Finally, the __delete__() method, which is called when the attribute is deleted 
from an object and similar to the __set__() method, it returns nothing.
'''
# Descriptors is the concept behind the python property

