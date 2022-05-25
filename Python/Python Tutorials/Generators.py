import collections.abc
import types
import sys
'''
1) If you create your own iterator, it is a little bit involved - you have to create a class and at-
-least implement the iter and the next methods.
2) But what if you don't want to go through this hassle and want to quickly create an iterator.
3) Fortunately, Python provides a short-cut way to defining an iterator.
4) All you need to do is define a function with at least 1 call to yield and now when you call that function-
 -it will return "something" which will act like an iterator (you can call next method and use it in a for loop).
5) This something has a name in Python called Generator.
6) Generators are the simplest and faster way to create an iterator.
'''

print("********** Iterator Example ************")
# basic iterator example which returns even numbers from 2 to 20

class EvenGenerator():
    def __init__(self,num):
        self.num = num
    def __iter__(self):
        self.start_pos = 2
        return self
    def __next__(self):
       while self.start_pos <= self.num:
           if self.start_pos:
             temp = self.start_pos
             self.start_pos+=2
             return temp
           else:
               break

# one way


evengenerator1 = EvenGenerator(20)
even_iter = iter(evengenerator1)
print(next(even_iter))
print(next(even_iter))
print(next(even_iter))
print(next(even_iter))
print(next(even_iter))
print(next(even_iter))
print(next(even_iter))
print(next(even_iter))
print(next(even_iter))
print(next(even_iter))
print(next(even_iter)) # Reached Limit Here

# second way
evengenerator2 = EvenGenerator(20)
even_iter2 = iter(evengenerator2)
for x in range(10):
    print(next(even_iter2),end=",")
print("\n")


# Here to implement custom even items iterator that returns even numbers from 2 to 20,
# We implemented a class with 1 constructor, 1 iter method and 1 next method.
# This way to generate a custom iterator is so tough with so many lines of code.
# SO, That's why we have generator to automate the above all processes.


print("*********** Generator Example ****************")


def even_maker():

    yield 2
    yield 4
    yield 6
    yield 8
    yield 10
    yield 12
    yield 14
    yield 16
    yield 18
    yield 20


# one way
gen_obj = even_maker() # returning an iterator and assigning to gen_obj
print(type(gen_obj))
print(gen_obj)
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print("\n")

# second way
gen_obj2 = even_maker()
for value in gen_obj2:
    print(value,end=",")
print("\n")

# third way
gen_obj3 = even_maker()
for y in range(10):
    print(next(gen_obj3),end="\n")
print('\n')

# even_maker() returns an iterator that is used to iterate upon using next() in the above example.
# Each and every next() function matches with one yield in the generator function.
# This is how generator acts, generators is the simpliest way to make our own iterators.

print("********** Generator Comprehension / Expression *************")

generator_example = (2*x for x in range(1,11))
print(type(generator_example))
print(generator_example)
print(next(generator_example))
print(next(generator_example))
print(next(generator_example))
print(next(generator_example))
print(next(generator_example))
print(next(generator_example))
print(next(generator_example))
print(next(generator_example))
print(next(generator_example))
print(next(generator_example))

g2 = (x for x in [1,2,3,4,5,6,7])
for value in g2:
    print(value,end=",")
print('\n')

print("**************************************************************")
print("**Proof that generators implements iterators using inheritance***"
      "and Iterators implement iterables using inheritance")
print("In simple words generators are subclasses for iterators and "
      "iterators are the sub classes for iterables")

print(issubclass(collections.abc.Iterator,collections.abc.Iterable))
print(issubclass(types.GeneratorType,collections.abc.Iterator))

print("Every Generator is a Iterator, But Every Iterator is not a Generator")

print("*****************************************************************")
print("***** Another Example for Iterators and Generators *****")

# Return Numbers from 1 to 10

sample_iter1 = iter(range(1,11))
print(sample_iter1)
print(type(sample_iter1))

print(next(sample_iter1))
print(next(sample_iter1))
print(next(sample_iter1))
print(next(sample_iter1))
print(next(sample_iter1))
print(next(sample_iter1))
print(next(sample_iter1))
print(next(sample_iter1))
print(next(sample_iter1))
print(next(sample_iter1))

'''
OR we can use,
for val in range(1,11):
    print(next(sample_iter1),end=",")
'''

print('\n')


def my_func():
    for _ in range(1,11):
        yield _


sample_gen_object = my_func()
# my_func returns an iterator that is used to iterate upon using next() method

print(sample_gen_object)
print(type(sample_gen_object))

print(next(sample_gen_object))
print(next(sample_gen_object))
print(next(sample_gen_object))
print(next(sample_gen_object))
print(next(sample_gen_object))
print(next(sample_gen_object))
print(next(sample_gen_object))
print(next(sample_gen_object))
print(next(sample_gen_object))
print(next(sample_gen_object))

'''
OR we can use,
for val in range(1,11):
    print(next(sample_gen_object),end=",")
'''

'''
Explanation : 
1) In line 127, sample_iter1 stores an iterator that is created from the iter(range(1,11))
2) In line 151, sample_gen_object stores an generator that is created from the function call of my_func()
3) As, generators are sub classes of iterators at c-api level, sample_gen_object also has next()/__next__()-
-method to use on itself to get the next values.
4) Generators do remember the past yielded value.
5) Line 157 invokes 0, and sample_gen_object remembers that, In the next call i.e, line 158 invokes 1 , as -
- sample_gen_object knows that it yielded 0 in the past , so it goes for 1 .Similarly all the other values -
- are returned by memorizing their past yielded values.
'''

print("***********************************************************************")
print("*** Which is faster and low memory user b/w iterator/generator ??? *****")


# Let us make string from lower to upper

class StringLowerToUpper():

    def __init__(self,name):
        self.name = name
        self.length = len(name)

    def __iter__(self):
        self.start = 0
        return self

    def __next__(self):

        if self.start < self.length:

            temp = self.name[self.start].upper()

            self.start += 1

            return temp



sltu = StringLowerToUpper('yokesh')
sltu_iter = iter(sltu)
print(next(sltu_iter))
print(next(sltu_iter))
print(next(sltu_iter))
print(next(sltu_iter))
print(next(sltu_iter))
print(next(sltu_iter))
'''
OR we can use ,
for val in range(len('yokesh')):
    print(next(sltu_gen),end=",")
'''


def lower_to_upper(name):

    yield name[0].upper()
    yield name[1].upper()
    yield name[2].upper()
    yield name[3].upper()
    yield name[4].upper()
    yield name[5].upper()


ltu_gen = lower_to_upper('yokesh')
print(next(ltu_gen))
print(next(ltu_gen))
print(next(ltu_gen))
print(next(ltu_gen))
print(next(ltu_gen))
print(next(ltu_gen))

'''
OR we can use ,
for val in range(len('yokesh')):
    print(next(ltu_gen),end=",")
'''

print(f"Memory Taken By Iterator : {sys.getsizeof(sltu_iter)}")
print(f"Memory Taken By Generator : {sys.getsizeof(ltu_gen)}")

# From the above results, we can say

# Generators Consume More Memory When Compared To Iterators.
# Iterators takes more time to execute when compared to generators.

print("Iterators are more memory efficient and takes less memory when compared to generators")
print("Generators are faster than Iterators")
print("All generators are iterators, but vice versa is False")


# Remember Below Cheat Sheet regarding generators,
'''
A generator function is a function with yield in it.

A generator expression is like a list comprehension. It uses "()" vs "[]"

A generator object (often called 'a generator') is returned by both above.

A generator is also a subtype of iterator.
'''

print("************************************************************************")
print("***** Lazy Evaluation / Deferred Evaluation *****")

# lazy evaluation means that the object is evaluated when it is needed, not when it is created.
# lazy evaluation is implemented by iterators and generators in python.
# lazy evaluation delays the eval of an expr until its value is needed and avoids repeated evals.
# range() internally implements lazy evaluation and range() is a generator.
# The object returned by the range() is called lazy iterable.

z = range(1,11)

print(z)

print(list(z))

print(type(z))

# From lines 280, 282, We can specify that printing range object itself won't return numbers in that-
# - specific range,Instead it returns range object.
# But, Printing list of range object will return the numbers in that range.

# Then, How to print values using range object itself, just use for loop!

for item in z:
    print(item,end=",")
print("\n")
# How lazy evaluation differ from strict evaluation ...?

# this is a list, create all 5000000 x/2 values immediately, uses []
lis = [x / 2 for x in range(5)]
print(f"List formed using strict evaluation : {lis}")

# this is a generator, creates each x/2 value only when it is needed, uses ()
gen = (x / 2 for x in range(5))
print(f"Items formed using lazy evaluation  : ")
for val in gen:
    print(val,end=",")

print('\n')

'''
1) Even though range(5) is a generator in Python3.x, [x/2 for x in range(5000000)] is still a list. 
2) range(...) does it's job and generates x one at a time, but the entire list of x/2 values will be-
 -computed when this list is created.
'''

print("***** Strict vs Lazy Evaluation and normal vs generator function Example *****")


def return_something1(*nums1):
    for val1 in nums1:
        return val1


print(return_something1(1,2,3,4,5,6,7,8,9))
print(return_something1(1,2,3,4,5,6,7,8,9))
print(return_something1(1,2,3,4,5,6,7,8,9))
print('\n')


def return_something2(*nums2):
    for val2 in nums2:
        yield val2


gen_object = return_something2(1,2,3,4,5,6,7,8,9)

print(gen_object.__next__())
print(gen_object.__next__())
print(gen_object.__next__())

print("Here, return_something1 function performs strict evaluation and do not memorize previously returned value")
print("Here, return_something2 function performs lazy evaluation and memorizes previously returned value")

# In the above, Using Lazy execution I can get the value whenever i needed without repetetion -
# -of previously returned one's.
# Functions vs Generators :
# A function executes when you call it, it returns a value. And then it's over.
# No saved state. Next call to it is entirely separate.
#
# A generator has a yield statement. When it hits that it return a value but
# it saves its internal state. This is very handy to compute a sequence

'''
A function is something you call. It does its job. And then it finishes, usually returning a value of some sort.

Once it’s delivered its return value, it has finished, the space it used has been garbage collected off the stack. It’s as if it never existed.

A generator, on the other hand, is a kind of separate ongoing process.

You call it and it starts executing just like a function. But when it yields its return value,-
-it doesn’t end or disappear. 

All the local variables that it declared are still there holding whatever values they held at the moment it yielded.

And if you ask it for a new value, it just starts up and continues where it left off.

That means a generator can generate an ongoing sequence of return values. Whereas a function returns just one.

Eventually a generator might finish. And then be cleared away. Or it might run forever in an infinite loop.

But because it is paused and stops temporarily when it yields, that is OK.
'''


def gen():
    x = 0
    while True:
        yield x
        x = x + 1


g = gen()
for i in range(10):
    print("%s : %s" % (i, next(g)))


print("********************************************************************************")
print("********* fibonacci using normal function and using generator **********")

# using normal function :
def fibo1(num):

    temp = [0,1]
    if num in temp:
        return num
    else:
        return fibo1(num-1)+fibo1(num-2)


print([fibo1(x) for x in range(5)])

# using generator :
def fibo2(num):

    a,b = 0,1

    while True:
        yield a
        a,b = b,a+b


it = fibo2(5)
print([next(it) for x in range(5)])

print("**************************************************************************")
