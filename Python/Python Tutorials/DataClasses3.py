# The variables in the data classes takes an method called field() that has some useful parameters

# syntax : dataclasses.field(*, default=MISSING, default_factory=MISSING, repr=True,
# hash=None, init=True, compare=True, metadata=None)

'''
1) default :  This parameter specifies the default value for the attribute,
              if no value is provided during object creation. Similar to the parameters in a function,
              fields with a default value must come after any fields without a default.
              There is also an alternative way to provide a default value – just like you do to a
              normal variable using = operator

2) default_factory : If provided, it must be a zero-argument callable that will be called when a
                     default value is needed for this field.
                     The return value of the callable will be set as the default value for the
                     attribute in object creation.
                     You either provide a callable to the default factory OR you provide a default value
                     to the attribute. It is an error to specify both default and default_factory.

3) If init = True, then the variable with the field init = True will be initialized by the internal default init
   If init = False, then the variable is not initialized by the internal init. so we need to initialize on our
   own. One way is to use default field when init = False in any of the variable.
   By default, init = True for all variables inside a dataclass

4) If repr = True ,then the variable is used in the internal default __repr__
   If repr = False, then the variable is not uses in internal default __repr__
   By default, repr = True for all variables in a dataclass

5) If compare = True then the variable is used when 2 objects of the class are used on comparison operators.
   If compare = False then the variable is not used when 2 objects of the class are used on comparison operators.
   By default, compare = True for all variables in a dataclass

6) If hash = True, then this variable is used by the python to generate the hash value of its object
   If hash = None , then this variable is not used by the python to generate the hash value of its object
   By default, hash = None for all variables in a dataclass

7) metadata : This is usually a dictionary, the key-value pair indicating various information and it’s data.
              This particular attribute does not really seem to be in use most of the
              time but it’s important if your DataClass is actually being in used somewhere during
              development and the attribute’s data is used or accessed by third-parties when their
              tool or software is integrated in the project.
In the script, it’s value can be accessed by querying __dataclass_fields__ variable of the object.
'''
from dataclasses import dataclass,field


print("************************************************************************************")


@dataclass
class A:

    lname : str
    fname : str
    age : int = field(init = False)
    price : float = field(init = False)


try :
    a = A('yokesh', 'chowdary', 23, 543.21)

except Exception as Ex:

    print(Ex)

# We need to pass 2 only as we gave init = False for 2 variables

a1 = A('yokesh','chowdary')

# Now also we get error as we passed 2 values for 2 variables that initialize lname and fname only.
# Now, age and price didn't gave any values in them.
# If __repr__ is used on the object, we will get attribute error.
try:

    print(a1)

except AttributeError as E2:

    print(E2)


# So, We want need to explicitly initialize age and price so that printing the object will
# not give the error

a1.age = 23
a1.price = 765.4

print(a1)

# Note : After initializing the age and price explicitly, we will not get error while printing
# object because all variables in the data class got values so that repr prints all of them.


print("************************************************************************************")
# Without initializing explicitly as in the line 82,82 . We can use default parameter in those
# variables that has init = False.


@dataclass
class B:

    sweet : str
    hot : str = field(init = False, default = 'kar')


b = B('gulabjamun')
print(b)

# Now, we won't get error while printing object because we passed default value to the variable
# that has init = False.


print("************************************************************************************")
# default_factory : Generally a function returning something is assigned.


@dataclass
class C:

    @staticmethod
    def some():
        return 'yokesh chowdary'

    country: str
    name : str = field(default_factory = some)


c = C('india')
print(c)

print("************************************************************************************")
# We cannot use default and default_factory on the same variable


try :
    @dataclass
    class C1:

        @staticmethod
        def some1():
            return 'yokesh chowdary'

        country1: str
        name1: str = field(default='naina', default_factory=some1)


    c1 = C1('india')
    print(c1)


except Exception as ee:

    print(ee)

print("************************************************************************************")
# repr = True is by default , if repr = False what happens ?


@dataclass
class Book:

    book_name : str
    book_pages : int = field(repr = False)


book = Book('2 ways to code',231)
print(book)

# The above code only prints "Book(book_name='2 ways to code')" . It ignored book_pages as we gave repr = False

print("************************************************************************************")


@dataclass
class Ocean:

    state : str  = field(compare = False)


ocean1 = Ocean('water')
ocean2 = Ocean('not water')

print(ocean1 == ocean2)

# Even though ocean1 object stores 'water' for state variable and ocean2 object stores 'not water'
# for state variable. printing ocean1 == ocean2 is giving True because we disabled == operator
# for the field state.
# This == uses 'eq' = True parameter in dataclass decorator.
# If i modify eq = False in dataclass decorator and try to execute line 183 it gives error as
# == is disabled in decorator at class level.


@dataclass(order = True)
class Ocean1:

    state1 : str  = field(compare = False)
    state2 : str


ocean3 = Ocean1('water','fluid')
ocean4 = Ocean1('not water','not fluid')


print(ocean3 > ocean4)

# FOr using >,<,>=,<= we need to specify order = True in dataclass decorator
# Actually the line 201 should give True because , 'w' in water > 'n' in not water
# As it got true at comparing 'w' with 'n' it stops comparing rest of the letters.
# But, we disabled comparing state1 variable . So, now comparing starts from state2 variable
# In state2 variable, 'f' < 'n' so it returns False as we asked for ocean3 > ocean4

print("************************************************************************************")

# Generally, python does not use objects variables for calculating hash() using unsafe_hash = True parameter.
# That's why by default for every variable in the data class we have hash = None by default .
# We can enable it using hash = True so that while getting hashed value on the object , python uses
# not only the object but also it's variables to generate hash.

print("************************************************************************************")

# Using __dataclass_fields__ in the code


@dataclass
class Medium:

    author : str  = field(metadata = 'this variable indicates author name')
    upvotes : int = field(metadata = 'this indicates count of upvotes')
    type : str = field(metadata = 'Indicates type of the blog')


medium = Medium('yokesh',2000,'cs')
print(medium.__dataclass_fields__)
print(medium.__dataclass_fields__['author'])
print(medium.__dataclass_fields__['author'].metadata)
print(medium.__dataclass_fields__['upvotes'])
print(medium.__dataclass_fields__['upvotes'].metadata)
print(medium.__dataclass_fields__['type'])
print(medium.__dataclass_fields__['type'].metadata)

print("************************************************************************************")

