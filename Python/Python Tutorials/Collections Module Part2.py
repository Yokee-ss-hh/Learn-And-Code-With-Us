from collections import OrderedDict,defaultdict

print("*****************************************************************************************")
print("*************************Initializing Techniques***********************************")

# Before python 3.6, dictionaries are un-ordered. So python introduced Ordereddict() class
# to make dictionaries follow the order in which they are initialized.

# In python 3.6 update dictionaries became ordered so many people thought there is no need
# for Ordereddict in future, but some features of Ordereddict are so much useful

# Python OrderedDict() is also mutable same as normal dict()

'''Python’s OrderedDict is a dict subclass that preserves the order in which key-value pairs,
commonly known as items, are inserted into the dictionary. When you iterate over an OrderedDict object,
items are traversed in the original order. 
If you update the value of an existing key, then the order remains unchanged. 
If you remove an item and reinsert it, then the item is added at the end of the dictionary.
Being a dict subclass means that it inherits all the methods a regular dictionary provides.
OrderedDict also has additional features that you’ll learn about in this tutorial.
In this section, however, you’ll learn the basics of creating and using OrderedDict objects in your code.'''

print(OrderedDict())
print(OrderedDict([('one',1),('two',2),('three',3)])) # list of tuples as initializer
print(OrderedDict((('one',1),('two',2),('three',3)))) # tuple of tuples as initializer
print(OrderedDict({('one',1),('two',2),('three',3)})) # Order of elements may change as we used set
print(OrderedDict({'one':1,'two':2,'three':3})) # Order is prevailed as dicts in py 3.6+ are ordered
print(OrderedDict(one=1,two=2,three=3)) # Ordereddict using keyword arguments
print(OrderedDict.fromkeys(['one','two','three'])) # None will be taken as value for all keys as default
print(OrderedDict.fromkeys(['one','two','three'],'yokesh')) # yokesh is the value for all keys

print("*************************Manipulating Techniques***********************************")
'''Since OrderedDict is a mutable data structure, you can perform mutating operations on its instances.
You can insert new items, update and remove existing items, and so on.
If you insert a new item into an existing ordered dictionary, then the item is added to the end of the dictionary:'''

numbers = OrderedDict(one=1, two=2, three=3)

print(numbers)

# The newly added item, ('four', 4), is placed at the end of the underlying dictionary,
# so the order of the existing items remains unaffected, and the dictionary keeps the insertion order.

numbers['four'] = 4

print(numbers)

# If you delete an item from an existing ordered dictionary and insert that same item again,
# then the new instance of the item is placed at the end of the dictionary:

del numbers['one']

print(numbers)

numbers['one'] = 1

print(numbers) # Note 'one':1 is added at end of the OrderedDict

# If you update the value of a given key in an ordered dictionary,
# then the key isn’t moved but assigned the new value in place.
# In the same way, if you use .update() to modify the value of an existing key-value pair,
# then the dictionary remembers the position of the key and assigns the updated value to it.

primes = OrderedDict(two=2,three=3,five=5)

print(primes)

primes['two'] = 2.0

print(primes)

primes.update(five=5.0)

print(primes)

# Just like with regular dictionaries, you can iterate through an OrderedDict object using several tools and techniques.
# You can iterate over the keys directly, or you can use dictionary methods, such as .items(), .keys(), and .values():

for item in OrderedDict(one=1, two=2, three=3):

    print(item,'->',OrderedDict(one=1, two=2, three=3)[item])

for item in OrderedDict(one=1, two=2, three=3).keys():

    print(item,'->',OrderedDict(one=1, two=2, three=3)[item])

for item in OrderedDict(one=1, two=2, three=3).values():

    print(item)

for item in OrderedDict(one=1, two=2, three=3).items():

    print(item)

# Another important feature that OrderedDict has provided since Python 3.5 is
# that its items, keys, and values support reverse iteration using reversed().
# This feature was added to regular dictionaries in Python 3.8.


even_nums = {'two':2, 'four':4, 'six':6}

for key in reversed(even_nums):
    print(key,'->',even_nums[key])

for key,value in reversed(even_nums.items()):
    print(key,'->',value)

for key in reversed(even_nums.keys()):
    print(key,'->',even_nums[key])

for value in reversed(even_nums.values()):
    print(value)

'''Every loop in this example uses reversed() to iterate through different elements of an
ordered dictionary in reverse order.
Regular dictionaries also support reverse iteration.
However, if you try to use reversed() with a regular dict object in a
Python version lower than 3.8, then you get a TypeError:'''

'''If you need to iterate over the items in a dictionary in reverse order,
then OrderedDict is a good ally. Using a regular dictionary dramatically reduces
your backward compatibility because reverse iteration wasn’t added to regular dictionaries until Python 3.8.'''

# move_to_end() method in OrderedDict()
letters = OrderedDict(b=2, d=4, a=1, c=3)

print(letters)

letters.move_to_end('b')

print(letters)

letters.move_to_end('b',last=False)

print(letters)

'''Another interesting feature of OrderedDict is its enhanced version of .popitem().
By default, .popitem() removes and returns an item in LIFO (Last-In/First-Out) order.
In other words, it removes items from the right end of the ordered dictionary'''

characters1 = OrderedDict(first='a',second='b',third='c')

print(characters1)

print(characters1.popitem())
print(characters1.popitem())
print(characters1.popitem())

try:
    print(characters1.popitem())

except Exception as e:

    print(e)

'''Here, you remove all the items from numbers using .popitem().
Every call to this method removes a single item from the end of the underlying dictionary.
If you call .popitem() on an empty dictionary, then you get a KeyError.
Up to this point, .popitem() behaves the same as in regular dictionaries.
In OrderedDict, however, .popitem() also accepts a Boolean argument called last, which defaults to True. 
If you set last to False, then .popitem() removes the items in FIFO (First-In/First-Out) order, 
which means that it removes items from the beginning of the dictionary:'''

characters2 = OrderedDict(first='a',second='b',third='c')

print(characters2)

print(characters2.popitem(last=False))
print(characters2.popitem(last=False))
print(characters2.popitem(last=False))

try:
    print(characters2.popitem())

except Exception as e:

    print(e)

# NOTE : In normal dicts there is no popitem(last=False)

print("***********Equality Operator b/w dict() and OrderedDict()*************")

# When you test two OrderedDict objects for equality in a Boolean context, the order of items plays an important role.
# For example, if your ordered dictionaries contain the same set of items,
# then the result of the test depends on their order:

letters_0 = OrderedDict(a=1, b=2, c=3, d=4)
letters_1 = OrderedDict(b=2, a=1, c=3, d=4)
letters_2 = OrderedDict(a=1, b=2, c=3, d=4)

print(letters_0 == letters_1)
print(letters_0 == letters_2)

# In this example, letters_1 has a slight difference in the order of its items compared
# to letters_0 and letters_2, so the first test returns False.
# On the second test, letters_0 and letters_2 have the same set of items, which are in the same order,
# so the test returns True.

# If you try this same example using regular dictionaries, then you’ll get a different result:

letters_00 = dict(a=1, b=2, c=3, d=4)
letters_11 = dict(b=2, a=1, c=3, d=4)
letters_22 = dict(a=1, b=2, c=3, d=4)

print(letters_00 == letters_11)
print(letters_00 == letters_22)
print(letters_00 == letters_11 == letters_22)

# Here, when you test two regular dictionaries for equality, you get True if both dictionaries
# have the same set of items. In this case, the order of items doesn’t change the final result.
# Finally, equality tests between an OrderedDict object and a regular dictionary
# don’t take the order of items into account:

letters_000 = OrderedDict(a=1, b=2, c=3, d=4)
letters_111 = dict(b=2, a=1, c=3, d=4)

print(letters_000 == letters_111)

# When you compare ordered dictionaries with regular dictionaries, the order of items doesn’t matter.
# If both dictionaries have the same set of items, then they compare equally,
# regardless of the order of their items.

# OrderedDict objects have a .__dict__ attribute that you can’t find in regular dictionary objects.

letters_main = OrderedDict(b=2, d=4, a=1, c=3)
print(letters_main.__dict__)

letters_main1 = dict(b=2, d=4, a=1, c=3)

try:

    print(letters_main1.__dict__)

except AttributeError as ae:

    print(ae)

# In the first example, you access the .__dict__ attribute on the ordered dictionary letters.
# Python internally uses this attribute to store writable instance attributes.
# The second example shows that regular dictionary objects don’t have a .__dict__ attribute.

# Python 3.9 added two new operators to the dictionary space.
# Now you have merge (|) and update (|=) dictionary operators.
# These operators also work with OrderedDict instances:

physicists = OrderedDict(newton="1642-1726", einstein="1879-1955")
biologists = OrderedDict(darwin="1809-1882", mendel="1822-1884")

scientists = physicists | biologists

print(scientists)

physicists1 = OrderedDict(newton="1642-1726", einstein="1879-1955")
physicists_2 = OrderedDict(newton="1642-1726/1727", hawking="1942-2018")
physicists1 |= physicists_2

print(physicists1)

# What are the differences b/w ordered and normal dict()'s ??

# 1) Key insertion order maintained in both types
# 2) Readability is high in OrderedDict when compared to normal dict()
# 3) Control over order of items is high in OrderedDict() as it has move_to_end and
#    pop_item() methods when compared to normal dict()
# 4) Operations Performance : OrderedDict() is low when compared to dict()
# 5) Memory Consumption : OrderedDict() consumes more memory than dict()
# 6) Support for reverse iteration : Available in both
# 7) Support for | and |= : Avialable in both
# 8) Dynamic appending of objects using __dict__ : Not available in dict() and available in OrderedDict()

# You can use the ordered dictionary’s .__dict__ attribute to store dynamically created writable instance attributes.
# There are several ways to do this. For example, you can use a dictionary-style assignment,
# like in ordered_dict.__dict__["attr"] = value. You can also use the dot notation,
# like in ordered_dict.attr = value.

print("*****************************************************************************************")

'''A common issue that you can face when working with Python dictionaries is how to handle missing keys.
If your code is heavily based on dictionaries, or if you’re creating dictionaries on the fly all the time, 
then you’ll soon notice that dealing with frequent KeyError exceptions can be quite annoying and can add 
extra complexity to your code. With Python dictionaries, you have some
available ways to handle missing keys:'''

# They are:
'''
1) Use get() and provide default value
2) Use setdefault() method
3) Use try-catch blocks
'''

'''The Python standard library provides collections, which is a module that implements specialized container types.
One of those is the Python defaultdict type, which is an alternative to dict that’s specifically designed to 
help you out with missing keys. defaultdict is a Python type that inherits from dict'''

print(issubclass(defaultdict,dict))

'''The main difference between defaultdict and dict is that when you try to access or modify a key 
that’s not present in the dictionary, a default value is automatically given to that key'''

'''The instance variable .default_factory will hold the first argument passed into defaultdict.__init__().
This argument can take a valid Python callable or None. If a callable is provided, 
then it’ll automatically be called by defaultdict whenever you try to access or modify the 
value associated with a missing key.All the remaining arguments to the class initializer are treated 
as if they were passed to the initializer of regular dict, including the keyword arguments.'''

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(d)

# Do not use list with brackets as list() while initializing defaultdict(), it raises TypeError

# In the above example,
# When each key is encountered for the first time, it is not already in the mapping;
# so an entry is automatically created using the default_factory function which returns an empty list.
# The list.append() operation then attaches the value to the new list.
# When keys are encountered again, the look-up proceeds normally (returning the list for that key) and
# the list.append() operation adds another value to the list.
# This technique is simpler and faster than an equivalent technique using dict.setdefault():

# The equivalent code using dict() for the above defaultdict() is :

# d = {}
# for k, v in s:
#    d.setdefault(k, []).append(v)

# A typical use of the Python defaultdict type is to set default_factory() to list and then
# build a dictionary that maps keys to lists of values. With this defaultdict,
# if you try to get access to any missing key, then the dictionary runs the following steps:
#
# 1) Call list() to create a new empty list
# 2) Insert the empty list into the dictionary using the missing key as key
# 3) Return a reference to that list

dd = defaultdict(list)
dd['key'].append(1)
print(dd)
dd['key'].append(2)
print(dd)
dd['key'].append(3)
print(dd)

# Here, you create a Python defaultdict called dd and pass list to .default_factory.
# Notice that even when key isn’t defined, you can append values to it without getting a KeyError.
# That’s because dd automatically calls .default_factory to generate a default value for the missing key.

# Let's talk about real-time example about a company and its employees

dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe')]

# Using defaultdict()
dep_dd = defaultdict(list)
for department, employee in dep:
    dep_dd[department].append(employee)

print(dep_dd)

# Using dict()
dep_d = dict()
for department, employee in dep:
    dep_d.setdefault(department, []).append(employee)
print(dep_d)

dep1 = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe')]

# We can group unique items by passing set as default_factory:
depp_dd = defaultdict(set)
for department, employee in dep:
    depp_dd[department].add(employee)
print(depp_dd)

# In the above example, you set .default_factory to set.
# Sets are collections of unique objects, which means that you can’t create a set with repeated items.
# This is a fascinating feature of sets, which guarantees that you won’t have repeated items
# in your final dictionary.

# We can count items also,
# If you set .default_factory to int, then your defaultdict will be useful for counting the items
# in a sequence or collection. When you call int() with no arguments, the function returns 0,
# which is the typical value you’d use to initialize a counter.

dd_item = defaultdict(int)
for department, _ in dep:
     dd_item[department] += 1
print(dd_item)

# Another example using int as default factory,
string = 'mississippi'
dd_str = defaultdict(int)
for letter in string:
     dd_str[letter] += 1
print(dd_str)

# We can even process the raw data accumulated in tables as,
incomes = [('Books', 1250.00),
           ('Books', 1300.00),
           ('Books', 1420.00),
           ('Tutorials', 560.00),
           ('Tutorials', 630.00),
           ('Tutorials', 750.00),
           ('Courses', 2500.00),
           ('Courses', 2430.00),
           ('Courses', 2750.00),]


dd_incomes = defaultdict(float)
for product, income in incomes:
    dd_incomes[product] += income
print(dd_incomes)

# defaultdict() vs dict()

print(set(dir(defaultdict)) - set(dir(dict)))

# From the above line, There are only 3 differences b/w defaultdict and normal dict , they are:
# {'__copy__', 'default_factory', '__missing__'}

'''
.__copy__() -> Provides support for copy.copy()
.default_factory -> Holds the callable invoked by .__missing__() to automatically provide 
                    default values for missing keys
.__missing__(key) -> Gets called when .__getitem__() can’t find key
'''

# defaultdict is equal to a dict with the same items

std_dict = dict(numbers=[1, 2, 3], letters=['a', 'b', 'c'])
defa_dict = defaultdict(list, numbers=[1, 2, 3], letters=['a', 'b', 'c'])

print(std_dict == defa_dict)

# Let's talk about default factory more,
# The first argument to the Python defaultdict type must be a callable that takes no arguments and returns a value.
# This argument is assigned to the instance attribute, .default_factory.
# For this, you can use any callable, including functions, methods, classes, type objects, or any other valid callable.
# The default value of .default_factory is None.
# If you instantiate defaultdict without passing a value to .default_factory, then the dictionary will
# behave like a regular dict and the usual KeyError will be raised for missing key lookup or modification attempts:

# On the other hand, if you pass a non-callable object to the initializer of the Python
# defaultdict type, then you’ll get a TypeError

try :

    x = defaultdict(0)

except TypeError as te:

    print(te)

# Keep in mind that .default_factory is only called from .__getitem__() and not from other methods.
# This means that if dd is a defaultdict and key is a missing key, then dd[key] will call .default_factory
# to provide a default value, but dd.get(key) still returns None instead of the value that .default_factory
# would provide. That’s because .get() doesn’t call .__getitem__() to retrieve the key.

xx = defaultdict(list)

print(xx['missing']) # returns [] as xx[''] calls __getitem__ internally which in turn calls defaultfactory()

print(xx.get('some missing')) # returns None
# Note : 'None' is returned by default factory only when default factory object is called using get() function.

#  you can always change or update the callable you initially assign to .default_factory
#  in the same way you would do with any instance attribute.

yyz = defaultdict(list)

print(yyz['something']) # prints []

yyz.default_factory = float

print(yyz['do some'])


# default factory in defaultdict vs setdefault() in dict()
# Both does the same work, assigns a default value for the un available key

poke = dict()
poke.setdefault('miss',[])
print(poke)

moke = defaultdict(list)
print(moke['miss'])
print(moke)

# IMP NOTE : You can assign any type of Python object using .setdefault().
# This is an important difference compared to defaultdict if you consider that
# defaultdict only accepts a callable or None.

# On the other hand, if you use a defaultdict to accomplish the same task,
# then the default value is generated on demand whenever you try to access or modify a missing key.
# Notice that, with defaultdict, the default value is generated by the callable you pass upfront to the
# initializer of the class.

# default factory initializers examples

print(list())
print(tuple())
print(int())
print(float())

# Finally, using a defaultdict to handle missing keys can be faster than using dict.setdefault()

# Note that .__missing__() is automatically called by .__getitem__() to handle missing keys and
# that .__getitem__() is automatically called by Python at the same time for subscription operations like d[key].

# So, how does .__missing__() work? If you set .default_factory to None, then .__missing__() raises
# a KeyError with the key as an argument. Otherwise, .default_factory is called without arguments to
# provide a default value for the given key. This value is inserted into the dictionary and finally returned.
# If calling .default_factory raises an exception, then the exception is propagated unchanged.
#
# The following code shows a viable Python implementation for .__missing__():

# def __missing__(self, key):
#     if self.default_factory is None:
#         raise KeyError(key)
#     if key not in self:
#         self[key] = self.default_factory()
#     return self[key]

# Keep in mind that the presence of .__missing__() in a mapping has no effect on the behavior of other methods
# that look up keys, such as .get() or .__contains__(), which implements the in operator.
# That’s because .__missing__() is only called by .__getitem__() when the requested key is not found in the dictionary.
# Whatever .__missing__() returns or raises is then returned or raised by .__getitem__().

# Do not pass None as a default factory even by default default factory returns None

try:
    tkk = defaultdict(None)

    print(tkk['okkk'])

except KeyError as k:

    print("Key error was raised")

# Using lambda as default factory,

def do_factory(arg):
    # Do some processing here...
    result = arg.upper()
    return result


defff_dict = defaultdict(lambda: do_factory('default value'))

print(defff_dict['tokesh'])
print(defff_dict)


# another example
lstttp = [1, 1, 2, 1, 2, 2, 3, 4, 3, 3, 4, 4]
def_dict101 = defaultdict(lambda: 1)
for number in lstttp:
     def_dict101[number] *= number
print(def_dict101)






















