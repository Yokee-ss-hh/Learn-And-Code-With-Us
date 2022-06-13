import datetime
print("************ __str__ and __repr__ ****************")


class Yokesh:

    def __init__(self,fname,lname):

        self.fname = fname
        self.lname = lname

    def __str__(self):

        return f"Hello guys i am {self.fname} {self.lname}"


yokesh = Yokesh('yoki','yokee')
print(yokesh)
print(yokesh.__str__())
print(str(yokesh))
print(repr(yokesh))
print(yokesh.__repr__())


class Kusuma:

    def __init__(self,fname,lname):

        self.fname = fname
        self.lname = lname

    def __repr__(self):

        return f"Hello guys i am {self.fname} {self.lname}"


kusuma = Kusuma('Dr','kusuma mbbs')
print(kusuma)
print(kusuma.__repr__())
print(repr(kusuma))
print(str(kusuma))
print(kusuma.__str__())


# IMP :
# repr() and __repr__() will not work if the class only implements __str__()
# str() and __str__() will work even if the class only implements __repr__()
# That is one of the difference and another difference is :
# __str__() reruns o/p that is user-friendly
# __repr__() returns o/p that is developer friendly
'''
1) These 2 methods are invoked implicitly when objects are printed 
2) Invoked implicitly when we pass object to str()
3) Invoked implicitly when we call these methods explicitly used object as obj.__str__() and obj.__repr__()
'''

# What is the difference between repr() and str()

print(str(datetime.datetime.now()))

print(repr(datetime.datetime.now()))

# str() displays today’s date in a way that the user can understand the date and time.
#
# repr() prints “official” representation of a date-time object
# (means using the “official” string representation we can reconstruct the object).


# Python program to demonstrate writing of __repr__ and
# __str__ for user defined classes

# A user defined class to represent Complex numbers

class Complex:

    # Constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # For call to repr(). Prints object's information
    def __repr__(self):
        return 'Rational(%s, %s)' % (self.real, self.imag)

        # For call to str(). Prints readable form

    def __str__(self):
        return '%s + i%s' % (self.real, self.imag)

    # Driver program to test above


t = Complex(10, 20)

# Same as "print t"
print(str(t))
print(repr(t))


# NOTE : We cannot use str() and repr() on our user defined classes and objects directly , even using
# we will get same o/p as without repr(),str().
# We can use str() and repr() on in-built data types like date time ,lists,.....etc etc as they pre implemented
# these __str__() and __repr__() at its base class level i.e, at it's parent class 'object' level.


# Another example that we can use str() and repr() directly on inbuilt objects

print(str(max(10,20)))
print(repr(max(10,20)))

'''

Apart from all the answers given, I would like to add few points :-

1) __repr__() is invoked when you simply write object's name on interactive python console and press enter.

2) __str__() is invoked when you use object with print statement.

3) In case, if __str__ is missing, then print and any function using str() invokes __repr__() of object.
   If __str__ implementation is missing then __repr__ function is used as fallback. 
   There is no fallback if __repr__ function implementation is missing.

4) __str__() of containers, when invoked will execute __repr__() method of its contained elements.

5) str() called within __str__() could potentially recurse without a base case, and error on maximum recursion depth.

6) __repr__() can call repr() which will attempt to avoid infinite recursion automatically, 
   replacing an already represented object with ....
   
'''

# Another beautiful example,


class C1:pass


class C2:
    def __str__(self):

        return str(f"{self.__class__.__name__} class str ")


class C3:
    def __repr__(self):

         return str(f"{self.__class__.__name__} class repr")


class C4:

    def __str__(self):

        return str(f"{self.__class__.__name__} class str ")

    def __repr__(self):

         return str(f"{self.__class__.__name__} class repr")


ci1 = C1()
ci2 = C2()
ci3 = C3()
ci4 = C4()

print(ci1)
print(str(ci1))
print(repr(ci1))
print(ci2)
print(str(ci2))
print(repr(ci2))
print(ci3)
print(str(ci3))
print(repr(ci3))
print(ci4)
print(str(ci4))
print(repr(ci4))


print("********************** Comparison Dunder Methods ***************************")
'''
__eq__(self,other)    triggered by ==
__ne__(self,other)    triggered by !=
__lt__(self,other)    triggered by <
__gt__(self,other)    triggered by >
__le__(self,other)    triggered by <=
__ge__(self,other)    triggered by >=
'''


class Compare2:

    def __init__(self,val1,val2):

        self.val1 = val1
        self.val2 = val2


class Compare1:

    def __init__(self,val1,val2):

        self.val1 = val1
        self.val2 = val2

    def __eq__(self,other):

        return self.val1 == other.val1 and self.val2 == other.val2

    def __ne__(self,other):

        return self.val1 != other.val1 and self.val2 != other.val2

    def __lt__(self,other):

        return self.val1 < other.val1 and self.val2 < other.val2

    def __gt__(self,other):

        return self.val1 > other.val1 and self.val2 > other.val2

    def __le__(self,other):

        return self.val1 <= other.val1 and self.val2 <= other.val2

    def __ge__(self,other):

        return self.val1 >= other.val1 and self.val2 >= other.val2


compare1 = Compare1(21,12)
compare2 = Compare2(9,30)

print(compare1 == compare2)
print(compare1 != compare2)
print(compare1 < compare2)
print(compare1 > compare2)
print(compare1 <= compare2)
print(compare1 >= compare2)

print(compare1.__eq__(compare2))
print(compare1.__ne__(compare2))
print(compare1.__lt__(compare2))
print(compare1.__gt__(compare2))
print(compare1.__le__(compare2))
print(compare1.__ge__(compare2))

print("********************** Arithmetic Dunder Methods ***************************")
'''
__add__(self,other)       triggered by  '+'
__sub__(self,other)       triggered by '-'
__mul__(self,other)       triggered by '*'
__truediv__(self,other)   triggered by '/'  
__floordiv__(self,other)  triggered by '//'
__mod__(self,other)       triggered by '%'
__pow__(self,other)       triggered by '**'
'''


class Arith2:

    def __init__(self,a,b):

        self.a = a
        self.b = b


class Arith1:

    def __init__(self,a,b):

        self.a = a
        self.b = b

    def __add__(self, other):

        return Arith1((self.a + other.a), (self.b + other.b))

    def __sub__(self, other):

        return Arith1((self.a - other.a), (self.b - other.b))

    def __mul__(self, other):

        return Arith1((self.a * other.a), (self.b * other.b))

    def __truediv__(self, other):

        return Arith1((self.a / other.a), (self.b / other.b))

    def __floordiv__(self, other):

        return Arith1((self.a // other.a), (self.b // other.b))

    def __mod__(self, other):

        return Arith1((self.a % other.a), (self.b % other.b))

    def __pow__(self, power, modulo=None):

        return Arith1((self.a ** power.a), (self.b ** power.b))


arith1 = Arith1(10,20)
arith2 = Arith2(30,40)

obj1 = arith1 + arith2
print(obj1.a,obj1.b)

obj2 = arith1 - arith2
print(obj2.a,obj2.b)

obj3 = arith1 * arith2
print(obj3.a,obj3.b)

obj4 = arith1 / arith2
print(obj4.a,obj4.b)

obj5 = arith1 // arith2
print(obj5.a,obj5.b)

obj6 = arith1 % arith2
print(obj6.a,obj6.b)

obj7 = arith1 ** arith2
print(obj7.a,obj7.b)

# We can use 2 objects of same class or different classes also
# In the above comparison and arithmetic examples, I used objects of different classes
# For each dunder method i returned object with data of type Arith1 class
# We can return Arith2 object also.
# In Arith1 i implemented all dunder methods for all arithmetic operators,
# So, python checks the __add__ in Arith1 if i write Arith1 object + Arith2 object
# And similarly, python checks for __add__ in Arith2 if i write Arith2 obj + Arith1 obj
# Now, if i write obj8 = arith2 + arith1, python gives error as , arith2 object's class Arith2
# did not implement __add__ dunder method in it's class to all it , let's check that

try:
    obj8 = arith2 + arith1
except Exception as e:
    print(e)

# Hover mouse cursor on line 339, and it shows,
# "Class 'Arith2' does not define '__add__', so the '+' operator cannot be used on its instances"

# In this case we need to use Reflected Dunder Methods,

print("********************** Reflected Assignment Dunder Methods ***************************")

# Reflected Arithmetic Dunders are triggered only when left operand did not defined any arithmetic dunder method.


class Teacher1:

    def __init__(self,x):

        self.x = x

    def __add__(self, other):

        return Teacher1(self.x + other.x) # We can return Teacher2 object also


class Teacher2:

    def __init__(self, x):

        self.x = x

    def __rsub__(self, other):

        return Teacher2(self.x - other.x) # We can return Teacher1 object also


t1 = Teacher1(8)
t2 = Teacher2(12)

# As, there is __add__ in Teacher1 class, the below line triggers it and will return an object of type Teacher1
r = t1 + t2

print(r.x)

s = t1 - t2

print(s.x)

# As there is no implementation for __sub__ in Teacher1 class, Now python checks for implementation of __rsub__
# in the right operand of line 383, i.e, t2 is the right operand in line 383, and t2 is the object of class
# Teacher2, So, in Teacher2 class it will check for __rsub__() , yes it will find __rsub__ in the Teacher2 class
# So, it simply calls it as t2 - t1 but not t1 - t2 as the __rsub__ locates in Teacher2 so first object
# should be of type Teacher2.So, it returns 4

print(type(r))
print(type(s))


class Student1:

    def __init__(self,v1):

        self.v1 = v1

    def __rmul__(self, other):

        return Student1(self.v1 * other.v2)


class Student2:

    def __init__(self,v2):

        self.v2 = v2


s1 = Student1(12)
s2 = Student2(4)

s3 = s2 * s1

print(s3.v1)
print(type(s3))

# What If , Both left and right operand classes don't implement __truediv__ and __rtruediv__ , lets see


class Cult1:

    def __init__(self,i):

        self.i = i


class Cult2:

    def __init__(self,j):

        self.j = j


c1 = Cult1(2)
c2 = Cult2(3)
try :
    c1 / c2

except Exception as exce:

    print(exce)

# Big Note :
'''
1) If we are using dunder method on 2 objects of same class, make sure u implement dunder in the class
   else, will get error
2) If we are using dunder method on 2 objects of different classes(say A and B), make sure to implement main
   dunder method like __add__(self,other) in class A when calling A obj + B obj , and implement reflected dunder
   method __radd__(self,other) in class B. 
   Because, if in case class A has missing __add__() for the call A obj + B obj , python looks for reflected dunder
   __radd__() in class B and if find, it changes the call from A obj + B obj to B obj + A obj and returns the answer.
'''
'''
Similarly, we have all reflected arithmetic dunders for all normal arithmetic dunders.
__radd__(self,other)       triggered by  '+'
__rsub__(self,other)       triggered by '-'
__rmul__(self,other)       triggered by '*'
__rtruediv__(self,other)   triggered by '/'  
__rfloordiv__(self,other)  triggered by '//'
__rmod__(self,other)       triggered by '%'
__rpow__(self,other)       triggered by '**'
'''
print("********************** Unary Operators Dunder Methods ***************************")
# Unary operators and functions only have one operand,
'''
__pos__(self)       triggered by +obj
__neg__(self)       triggered by -obj
__invert__(self)    triggered by ~obj    
'''


class Unary:

    def __init__(self,x):

        self.x = x

    def __pos__(self):

        return self.x

    def __neg__(self):

        return -self.x

    def __invert__(self): # It does bitwise NOT

        return ~self.x


unary1 = Unary(4)
unary2 = Unary(-7)

print(-unary1)
print(+unary2)
print(~unary1)
print(~unary2)


print("********************** Bitwise Dunder Methods ***************************")
'''
__lshift__(self,other)     triggered by <<
__rshift__(self,other)     triggered by >>
__xor__(self,other)        triggered by ^
__and__(self,other)        triggered by &
__or__(self,other)         triggered by |
For ~ bitwise not use __invert__(self)
'''


class Bitwise:

    def __init__(self,x):

        self.x = x

    def __lshift__(self, other):

        return self.x << other.x

    def __rshift__(self, other):

        return self.x >> other.x

    def __xor__(self, other):

        return self.x ^ other.x

    def __and__(self, other):

        return self.x & other.x

    def __or__(self, other):

        return self.x | other.x


b1 = Bitwise(3)
b2 = Bitwise(4)

print(b1 << b2)
print(b1 >> b2)
print(b1 ^ b2)
print(b1 & b2)
print(b1 | b2)

'''
Same like reflected arithmetic dunders we have reflected bitwise dunders,
__rlshift__(self,other)     triggered by <<
__rrshift__(self,other)     triggered by >>
__rxor__(self,other)        triggered by ^
__rand__(self,other)        triggered by &
__ror__(self,other)         triggered by |
For ~ bitwise not use __invert__(self)
'''

print("********************** Augmented Assignment Dunder Methods ***************************")
'''
__iadd__(self,other)       triggered by  '+='
__isub__(self,other)       triggered by '-='
__imul__(self,other)       triggered by '*='
__itruediv__(self,other)   triggered by '/='  
__ifloordiv__(self,other)  triggered by '//='
__imod__(self,other)       triggered by '%='
__ipow__(self,other)       triggered by '**='
__ilshift__(self,other)     triggered by <<=
__irshift__(self,other)     triggered by >>=
__iand__(self,other)        triggered by &=
__ior__(self,other)         triggered by |=
__ixor__(self,other)        triggered by ^=
'''


class AugAssign:

    def __init__(self,g,h):

        self.g = g
        self.h = h

    def __iadd__(self, other):

        self.g = self.g + other.g
        self.h = self.h + other.h

        return self

    def __isub__(self, other):

        self.g = self.g - other.g
        self.h = self.h - other.h

        return self

    def __imul__(self, other):

        self.g = self.g * other.g
        self.h = self.h * other.h

        return self

    def __itruediv__(self, other):

        self.g = self.g / other.g
        self.h = self.h / other.h

        return self

    def __ifloordiv__(self, other):

        self.g = self.g // other.g
        self.h = self.h // other.h

        return self

    def __imod__(self, other):

        self.g = self.g % other.g
        self.h = self.h % other.h

        return self

    def __ipow__(self, other):

        self.g = self.g ** other.g
        self.h = self.h ** other.h

        return self

    def __lshift__(self, other):

        self.g = self.g << other.g
        self.h = self.h << other.h

        return self

    def __rshift__(self, other):

        self.g = self.g >> other.g
        self.h = self.h >> other.h

        return self

    def __and__(self, other):

        self.g = self.g & other.g
        self.h = self.h & other.h

        return self

    def __or__(self, other):

        self.g = self.g | other.g
        self.h = self.h | other.h

        return self

    def __xor__(self, other):

        self.g = self.g ^ other.g
        self.h = self.h ^ other.h

        return self


aa1 = AugAssign(2,4)
aa2 = AugAssign(3,6)

aa1+=aa2
print(aa1.g, aa1.h)
print(aa2.g, aa2.h)

aa1-=aa2
print(aa1.g, aa1.h)
print(aa2.g, aa2.h)

aa1*=aa2
print(aa1.g, aa1.h)
print(aa2.g, aa2.h)

aa1/=aa2
print(aa1.g, aa1.h)
print(aa2.g, aa2.h)

aa1//=aa2
print(aa1.g, aa1.h)
print(aa2.g, aa2.h)


aa3 = AugAssign(5,7)
aa4 = AugAssign(1,3)

aa3%=aa4
print(aa3.g, aa3.h)
print(aa4.g, aa4.h)

aa3**=aa4
print(aa3.g, aa3.h)
print(aa4.g, aa4.h)


aa5 = AugAssign(5,3)
aa6 = AugAssign(2,2)

print("**")
aa5 >>= aa6
print(aa5.g,aa5.h)
print(aa6.g,aa6.h)

aa5 <<= aa6
print(aa5.g,aa5.h)
print(aa6.g,aa6.h)


aa5 = AugAssign(4,2)
aa6 = AugAssign(3,1)


aa5 & aa6
print(aa5.g,aa5.h)
print(aa6.g,aa6.h)

aa5 | aa6
print(aa5.g,aa5.h)
print(aa6.g,aa6.h)


aa5 ^ aa6
print(aa5.g,aa5.h)
print(aa6.g,aa6.h)


print("********************** Type conversion magic methods ***************************")


class Mango:

    def __init__(self,m,n):

        self.m = m
        self.n = n

    def __int__(self):

        return int(self.m)

    def __complex__(self):

        return complex(self.m)

    def __float__(self):

        return float(self.n)


mango = Mango(2.312,22)
print(int(mango))
print(complex(mango))
print(float(mango))

'''
Python’s __index__(self) method is called on an object to get its associated integer value. 
The returned integer is used in slicing or as the basis for the conversion in the built-in 
functions bin(), hex(), and oct(). 
The __index__() method is also used as a fallback for int(), float(), 
and complex() functions when their corresponding magic methods are not defined.
'''


class Data:

    def __init__(self,p):

        self.p = p

    def __index__(self):
        return self.p


x = Data(2)
# All those functions may use __index__():
print(bin(x))
print(oct(x))
print(hex(x))
print(complex(x))
print(int(x))
print(float(x))

'''
How to Use __index__() for Slicing and Indexing ???
You can use the magic method __index__() on a custom class to make it possible for objects 
of this class to be used in a slicing or indexing operation on an iterable. 
Python will internally call the __index__() method to obtain the integer associated with the custom object. 
This integer is then used as the basis for the slicing and indexing operation.
'''


class MyInteger:
    def __init__(self, i):
        self.i = i

    def __index__(self):
        return self.i


x = MyInteger(1)
y = MyInteger(8)
z = MyInteger(3)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[x])

'''
The objects x, y, z are of type My_Integer but they can still be used for the 
indexing and slicing operations as shown in the last three print statements.
'''


print("********************** Reflection magic methods ***************************")

# __instancecheck__(self,other)  triggered by isinstance(some_instance,some_class)
# __subclasscheck__(self,other)

print(isinstance(2,int))
print(isinstance('yokesh',str))

# The above 2 lines, calls respective classes int and str which they have implemented
# methods of __instancecheck__(self,other) , Let's see in action


class YokeshMeta(type):

    def __instancecheck__(self, instance):

        return True


class Yokesh(metaclass = YokeshMeta):

    pass


class Yoki(Yokesh):

    pass


class Yokeee(Yokesh):

    pass


yy = Yokeee()
print(isinstance(yy,Yokeee))
print(isinstance(yy,Yoki))
print(isinstance(yy,Yokesh))


# __subclasscheck__ is one of the methods to customize the result of issubclass() built-in function.
# It is a method to check whether a class is a subclass or not and returns True
# if the class is considered as a subclass(direct or indirect) of another class,
# otherwise, returns False. It cannot be defined as a class method in the actual/real class.
# It is implemented in the metaclass, as it is not for ordinary classes

class A(type):

    # __subclasscheck__() defined
    def __subclasscheck__(cls, sub):
        # Getting the L attribute of
        # subclass
        attr = getattr(cls, 'L', [])

        # Checking if the subclass
        # is present in the L attribute
        # of subclass or not
        if sub in attr:
            return True

        return False


class B(metaclass=A):
    # L Attribute
    L = [1, 2, 3, 4, 5]


class C(metaclass=A):
    # L Attribute
    L = ["Geeks", "For"]


# Driver's code
print(issubclass(1, B))
print(issubclass("Geeks", B))
print(issubclass("Geeks", C))

'''
Abstract class can override __subclasshook__() method to customize issubclass().
It returns True when a class is found to be subclass of a ABC class, 
it returns False if it is not and returns NotImplemented if the subclass check is 
continued with the usual mechanism. This method is defined in the ABC class with some conditions.
Classes that follow those conditions are considered to be a subclass.
'''
# Note: It must be defined as a class method.

from abc import ABCMeta


class A(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, C):
        if cls is A:

            # condition to check if the
            # function anyfun() is present
            # in any sub class or not
            if any("__anyfun__" in Q.__dict__
                   for Q in C.__mro__):
                return True

        return False


class P(object):
    pass


class Q(object):

    def __anyfun__(self):
        return 0


# Driver's code
print(issubclass(Q, A))
print(issubclass(P, A))

print("**************** Callable Objects Magic Methods **********************")
# As you may already know, in Python, functions are first-class objects.
# This means that they can be passed to functions and methods just as if
# they were objects of any other kind. This is an incredibly powerful feature.
#
# A special magic method in Python allows instances of your classes to behave as
# if they were functions, so that you can "call" them, pass them to functions that take
# functions as arguments, and so on. This is another powerful convenience feature that makes
# programming in Python that much sweeter.


class Example:
    def __init__(self):
        print("Instance Created")

    # Defining __call__ method
    def __call__(self):
        print("Instance is called via special method")


# Instance created
e = Example()

# __call__ method will be called
e()


class Product:
    def __init__(self):
        print("Instance Created")

    # Defining __call__ method
    def __call__(self, a, b):
        print(a * b)


# Instance created
ans = Product()

# __call__ method will be called
ans(10, 20)

# Why __call__ ?
# __call__ makes the instance of a class callable. Why would it be required?
#
# Technically __init__ is called once by __new__ when object is created, so that it can be initialized.
#
# But there are many scenarios where you might want to redefine your object,
# say you are done with your object, and may find a need for a new object.
# With __call__ you can redefine the same object as if it were new.
#
# This is just one case, there can be many more.


class ExampleExam:
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c
        print("init", self.a, self.b, self.c)


try :
     ExampleExam(1,2,3)(4,5,6)

except Exception as z :

    print(z)

# Now, use __call__()


class ExampleEE:
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c
        print("init", self.a, self.b, self.c)

    def __call__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
        print("call", self.x, self.y, self.z)


ExampleEE(1,2,3)(4,5,6)

# As, __init__ is called only once in the program, we can use __call__ to use on objects whenever
# we need as many times as possible.


class test(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


instance1 = test(1, 2, 3)
print(instance1.a)  # prints 1

# scenario 1
# creating new instance instance1
# instance1 = test(13, 3, 4)
# print(instance1.a) #prints 13


# scenario 2
# modifying the already created instance **instance1**
instance1(13, 3, 4)
print(instance1.a)  # prints 13

# NOTE : scenario 1 and scenario 2 seems same in terms of result output.
# But in scenario1, we again create another new instance instance1.
# In scenario2, we simply modify already created instance1.
# __call__ is beneficial here as the system doesn't need to create new instance.


print("********************  Making Custom Sequences ***********************")
'''
There's a number of ways to get your Python classes to act like 
built in sequences (dict, tuple, list, str, etc.). 
These are by far my favorite magic methods in Python because of the 
absurd degree of control they give you and the way that they magically make a whole 
array of global functions work beautifully on instances of your class.
'''
'''
Now that we're talking about creating your own sequences in Python, 
it's time to talk about protocols. Protocols are somewhat similar to interfaces in other 
languages in that they give you a set of methods you must define. 
However, in Python protocols are totally informal and require no explicit declarations 
to implement. Rather, they're more like guidelines.

Why are we talking about protocols now? Because implementing custom container types in Python 
involves using some of these protocols. First, there's the protocol for defining 
immutable containers: to make an immutable container, 
you need only define __len__ and __getitem__ (more on these later). 
The mutable container protocol requires everything that immutable containers 
require plus __setitem__ and __delitem__. Lastly, if you want your object to be iterable,
you'll have to define __iter__, which returns an iterator. 
That iterator must conform to an iterator protocol, which requires iterators to have 
methods called __iter__(returning itself) and next.
'''

# __getitem__(self,key)
# __setitem__(self,key,value)

print("******")


class BankRecord:

    def __init__(self, name):

        self.record = {
            "name": name,
            "balance": 100,
            "transaction": [100],
            "comments":['100 is credited']
        }

    def __getitem__(self, key):

        return self.record[key]

    def __setitem__(self, key, newvalue):

        if key == "balance" and newvalue is not  None and newvalue >= 100:
            self.record[key] += newvalue

        elif key == "transaction" and newvalue != None:
            self.record[key].append(newvalue)

    def getbalance(self):
        return self.__getitem__("balance")

    def updatebalance(self, new_balance):

        self.__setitem__("balance", new_balance)
        self.__setitem__("transaction", new_balance)

    def gettransactions(self):

        return self.__getitem__("transaction")

    def numtransactions(self):

        return len(self.record["transaction"])

    def make_comment(self,comment):

        self.record['comments'].append(comment)

    def see_comment(self,value):

        index = self.record['transaction'].index(value)
        return self.record['comments'][index]


sam = BankRecord("Yokesh")
print("The balance is : " + str(sam.getbalance()))

sam.updatebalance(200)
print("The new balance is : " + str(sam.getbalance()))
print("The no. of transactions are: " + str(sam.numtransactions()))

sam.make_comment('200 is added to your account')
print(sam.see_comment(200))

sam.updatebalance(300)
sam.make_comment('300 is added to your account')
print(sam.see_comment(300))

print("The new balance is : " + str(sam.getbalance()))
print("The no. of transactions are: " + str(sam.numtransactions()))
print("The transaction history is: " + str(sam.gettransactions()))


# __len__(self)
# __delitem__(self,key)
print("******")


class Money:

    def __init__(self):

        self.amount = dict()

    def __len__(self):

        return len(self.amount)

    def __setitem__(self, key, value):

        self.amount[key] = value

    def __getitem__(self, item):

        return self.amount['item']

    def __delitem__(self, key):

        del self.amount['key']

    def total_amount(self):

        temp = list(self.amount.values())
        return sum([a*a for a in temp])


money = Money()
money['10 rupee notes'] = 10
money['20 rupee notes'] = 20

print(len(money))

print("The total amount is : ",money.total_amount())

del money.amount['10 rupee notes']

print("The total amount after deleting is : ",money.total_amount())

print(len(money))


# __iter__(self)
# __reversed__(self)
# __contains__(self, item)
# __missing__(self, key)

'''
14

[::-1] is a slice. object.__reversed__() is instead used by the reversed() function, 
and is only applicable to sequences (objects that provide both a __len__ and a __getitem__ method).

If you don't supply __reversed__, the function uses those __len__ and __getitem__ methods 
to access indices in reverse. __reversed__ must itself return an iterator:
'''

print("******")


class Reversable(object):

       def __init__(self, seq):

         self.seq = seq

       def __len__(self):

          return len(self.seq)

       def __getitem__(self, item):

         return self.seq[item]

       def __reversed__(self):

          for elem in 'Reversing: ' + self.seq[::-1]:

              yield elem


r = Reversable('Foo bar baz!')
print(list(r))
print(r[::-1])
print(list(reversed(r)))


# __contains__ method defines how instances of class behave when they appear at right side
# of 'in' and 'not in' operator.

# Example to check if instance variable names are stored in object dictionary of the class PersonPP
# or not
# So, i used self.__dict__ to check the instance variable names there
# I returned True / False based on the above formula
print("******")


class PersonPP(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __contains__(self, param1):
        return True if param1 in self.__dict__.keys() else False


pp = PersonPP('yokesh',23)
print('name' in pp)
print('age' in pp)
print('lname' in pp) # returns False as we don't have 'lname' as instance variable
print("******")
# Example to check whether the instance variables stores the content we check using object


class GeneralCheck:

    def __init__(self,substr):

        self. substr = substr

    def __contains__(self, item):

        return True if item in self.substr else False


gc = GeneralCheck('yokesh')
print('yokesh' in gc)
print('yoke' in gc)
print('h' in gc)
print('oke' in gc)
print('shy' in gc)
print('okh' in gc)

print("******")
# __missing__ is used in subclasses of dict.
# It defines behavior for whenever a key is accessed that does not exist in a
# dictionary (so, for instance, if I had a dictionary d and said d["george"]
# when "george" is not a key in the dict, d.__missing__("george") would be called).

'''
When trying to access a key that doesn’t exist, Python’s __getitem__() dictionary method internally 
calls the __missing__() method if the key doesn’t exist.

In our case, the key 'David' doesn’t exist in the dict subclass, 
so Python calls __missing__() which returns the string 'I was called because no value for your key is existing' 
instead of raising the KeyError (which would be the default behavior).
'''


class MyDictSubclass(dict):

    def __missing__(self, key):
        return 'I was called because no value for your key is existing'


x = {'Alice': 23, 'Bob': 24, 'Carl': 25}
my_dict = MyDictSubclass(x)
# Try accessing existing key:
print(my_dict['Bob'])
# Try to access Non-existing key :
print(my_dict['David'])

print("***************************************************************************************")
# reversed() returns an iterator that contains items in reverse order


class ReverseCheck:

    def __init__(self,data):

        self.data = data

    def __reversed__(self):

        return reversed(self.data)


rc = ReverseCheck([1,2,3,4,5])
for item in reversed(rc):
    print(item)

print("***********************************************************************************")


# References : https://rszalski.github.io/magicmethods/#intro


































