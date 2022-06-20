# @dataclasses.dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
'''
1) init = True means , dataclass uses constructor internally
   init = False means we need to provide our own __init__
2) repr = True means, dataclass uses customized __repr__ internally
   repr = False means, we need to write our own __repr__
3) eq = True means, if data stored in respective objects of a dataclass is same, then '==' gives True
   eq = False means, even though data stored in respective objects of a dataclass is same, '==' gives False
4) order = True means we can use comparison operators on dataclass objects (>,<,<=,>=)
   order = False means we cannot use these operations
'''

# dataclass objects are mutable because we can change the data associated with the dataclass object using
# dot operator . If we have a variable as name = 'yokesh' associated with dataclass object , i can change the name
# variable to some other as, data_obj.name = 'someother'.
# So we cannot use hash() on this object, because mutable objects are unhashable.
# Inorder to use hash() on mutable dataclass objects , we want to freeze the dataclass so that data inside the
# dataclass cannot be modified using object and dot operator
from dataclasses import dataclass

'''
5) frozen = True,means we cannot modify the data once created and can use hash() on the frozen dataclass objects
6) unsafe_hash = True, means we can perform hash() on mutable objects of a dataclass without freezing them using
   frozen = True. 
'''


print("********************** init *************************")
# By default init = True


@dataclass(init = False)
class Books:

    quality : str
    quantity : int
    name : str
    cost : int


try:
     books = Books('100%',90,'py by Yok',"320")

except Exception as e:

    print(e)


# Then, How to make a call to __init__ without converting init = True in dataclass decorator
# Just define normal __init__

@dataclass(init = False)
class FavFood:

    def __init__(self,a,b):

        self.name = a
        self.quantity = b


fav = FavFood('biryani',1)
print(fav)

# In line 61, while printing object it is not giving user-friendly representation of object with the data
# but it is giving just the user-friendly name of the class as 'FavFod()' . But inside () there is no
# data associated with the 'fav' object. This is happening because we did not used internal constructor
# to set the data to 'fav' object. so internal __repr__ ignores the data that are setted to 'fav' object and
# __repr__ thinks that there is no data associated with 'fav' object. so it just gives object representation
# string without data in it as 'FavFood()'.
# What if i want __repr__ with data in it ?


@dataclass(init=False)
class FavFood1:

    def __init__(self, a, b):
        self.name = a
        self.quantity = b

    def __repr__(self):

        return f"FavFood(name = '{self.name}', quantity = {self.quantity})"


fav1 = FavFood1('biryani', 1)
print(fav1)

# Here our custom __repr__ in line 79 is overriding the internal __repr__
# We are using our custom __repr__ in the dataclass as __init__ = False allows
# internal __repr__ without data to be returned when print(fav1) is executed.


print("********************** repr *************************")
# By default, repr = True
# If repr = False, we cannot use customized internal __repr__ method so that printing object
# gives us a string that is not understandable.


@dataclass(repr = False)
class Dog:

    name : str
    color : str


dog = Dog('juicy','grey')
print(dog)
# The above line gives data about 'dog' object that is not understandable
# So, We want to create our own repr to get understandable data about 'dog' object


@dataclass(repr = False)
class Dog1:

    name : str
    color : str

    def __repr__(self):

        return f"Dog(name = '{self.name}', color = '{self.color}')"


dog1 = Dog1('juicy','grey')
print(dog1)


print("********************** eq *************************")
# By default eq = True


# eq checks whether the 2 objects of dataclass holds same data or not
# if 2 objects have same data then '==' returns True else False


@dataclass
class Water:

    component1 : str
    component2 : str


water1 = Water('Hydrogen','Oxygen')
water2 = Water('Hydrogen','Oxygen')

print(water1 == water2)


@dataclass(eq = False)
class Water1:

    component1 : str
    component2 : str


water3 = Water1('Hydrogen','Oxygen')
water4 = Water1('Hydrogen','Oxygen')

print(water3 == water4)
print(water3 != water4)
# When eq=False, the two object are compared using their hash based on its
# location in memory like two normal objects.
# Since the two objects have different hash representation, their equality returns False.

print("********************** order *************************")

# Comparison between two DataClasses are not only restricted to equality,
# but also supports >, >=, < and <= operators when order=True is set in argument parameter.
# The comparison between objects is based on the comparison between their corresponding attributes,
# which is done one by one starting from the first one.


@dataclass(order = True)
class A:

    name : str
    age : int


a1 = A('yokesh',23)
a2 = A('yokesh',22)
a3 = A('Ram',20)
a4 = A('john',32)
a5 = A('yogesh',22)

print(a1 > a2)
print(a4 < a1)
print(a5 < a2)
print(a3 > a4)

'''
If true (the default is False), __lt__(), __le__(), __gt__(), and __ge__() methods will be generated. 
These compare the class as if it were a tuple of its fields, in order. 
Both instances in the comparison must be of the identical type. 
If order is true and eq is false, a ValueError is raised.
If the class already defines any of __lt__(), __le__(), __gt__(), or __ge__(), then TypeError is raised.
'''

try :
    @dataclass(order = True , eq = False)
    class OK:

         age : int
         name : str

except Exception as e :

    print(e)


print("********************** frozen *************************")


# If true (the default is False), assigning to fields will generate an exception.
# This emulates read-only frozen instances.
# If __setattr__() or __delattr__() is defined in the class, then TypeError is raised


@dataclass(frozen = True)
class Green:

    color : str


gre = Green('green')

# If i try to change the objects data

try:
     gre.color = 'orange'

except Exception as o:

    print(o)

# This happens because , the dataclass 'Green' is frozen, and it is Immutable .
# Frozen dataclasses won't allow its objects' data to be modified.


# setting a objects data calls __setattr__ magic method internally
# getting a objects data calls __getattr__ magic method internally

# If dataclass is in freeze mode, and if we implement these 2 methods then python will throw error.


@dataclass(frozen = False)
class Attr:

    def __setattr__(self, key, value):

        self.__dict__[key] = value

    def __getattr__(self, item):

        return self.__dict__[item]


attr = Attr()
attr.item = 'yokesh'
print(attr.item)


# Now, if i make frozen = True, Let's see what happens


try :
    @dataclass(frozen=True)
    class Attrr:

        def __setattr__(self, key, value):
            self.__dict__[key] = value

        def __getattr__(self, item):
            return self.__dict__[item]


    attrr = Attrr()
    attrr.item = 'yokesh'
    print(attrr.item)

except Exception as e1:

    print(e1)


# The exception e1 prints
# Cannot overwrite attribute __setattr__ in class Attrr.
# That means python saying that the class Attrr is read-only, so you cannot overwrite the existing contents
# using __setattr__ method.


# Now, Hover on 2 red lines in the above code to know more.


print("********************** unsafe_hash *************************")

'''
unsafe_hash: If False (the default), a __hash__() method is generated according to how eq and frozen are set.
__hash__() is used by built-in hash(), and when objects are added to hashed collections 
such as dictionaries and sets. 
Having a __hash__() implies that instances of the class are immutable.
Mutability is a complicated property that depends on the programmer’s intent, the existence
and behavior of __eq__(), and the values of the eq and frozen flags in the dataclass() decorator.
By default, dataclass() will not implicitly add a __hash__() method unless it is safe to do so.
Neither will it add or change an existing explicitly defined __hash__() method.
Setting the class attribute __hash__ = None has a specific meaning to Python, 
as described in the __hash__() documentation.
If __hash__() is not explicitly defined, or if it is set to None,
then dataclass() may add an implicit __hash__() method.
Although not recommended, you can force dataclass() to create a __hash__() method with unsafe_hash=True. 
This might be the case if your class is logically immutable but can nonetheless be mutated. 
This is a specialized use case and should be considered carefully.
Here are the rules governing implicit creation of a __hash__() method.
Note that you cannot both have an explicit __hash__() method in your dataclass and set unsafe_hash=True; 
this will result in a TypeError.
If eq and frozen are both true, by default dataclass() will generate a __hash__() method for you. 
If eq is true and frozen is false, __hash__() will be set to None, marking it 
unhashable (which it is, since it is mutable). 
If eq is false, __hash__() will be left untouched meaning the __hash__() method of the superclass 
will be used (if the superclass is object, this means it will fall back to id-based hashing).
'''

# Generally, mutable objects in python are Unhashable.
# This means their hash cannot be generated using the hash() function of Python.
# Since any class objects including DataClass objects’ values can change, they are mutable.
# Hence they shouldn’t be able to produce any hash value


@dataclass
class Some:

    something : str


some = Some("Hello how are you")

try :

    print(hash(some))

except Exception as k:

    print(k)


# Inorder to produce hash on the dataclass object we want to make the dataclass object immutable

@dataclass(unsafe_hash = True)
class Some1:
    something1 : str


some1 = Some1("Hello how are you")

try:

    print(hash(some1))

except Exception as k1:

    print(k1)


print("**************************************************************************************************")


