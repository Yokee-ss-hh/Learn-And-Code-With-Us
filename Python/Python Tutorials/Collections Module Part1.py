from collections import Counter,namedtuple,deque,ChainMap

print("************************************************************************")
# A counter is a sub-class of the dictionary.
# It is used to keep the count of the elements in an iterable in the form of an unordered dictionary
# where the key represents the element in the iterable and value represents the count of that element
# in the iterable.
# Note: It is equivalent to bag or multiset of other languages.

# can create Counter object using "Counter()" constructor

# Counter() with direct iterables as arguments

print(Counter([2,4,6,8,1,3,5,7,1,2,3,4,5,6,7,8,9])) # List as iterable
print(Counter((4,2,6,8,1,3,5,7,1,2,3,4,5,6,7,8,9)))  # Tuple as iterable
print(Counter({'A':3, 'B':5, 'C':2, 'D':6})) # Dictionary in a counter
print(Counter(A = 3, B = 5, C = 2, D = 6)) # Keyword arguments as arguments to Counter()

# The outputs will be in the decreasing order of the counts
# Highest Count values are first following the next highest count elements
# 2 elements with same count follows the priority in which they are inserted

# In example1 , 2 comes before 4 so in output 2 comes before 4 even though both has same count
# In example2, 4 comes before 2 so in output 4 comes before 2 even though both has same count

# Can create a Counter() object and can update the values using that object also,


c = Counter()

# Syntax : <counter_object>.update(DATA)


c.update([1, 2, 3, 1, 2, 1, 1, 2])

print(c)

c.update([1, 2, 4])

print(c)

# Using update() the new data is being appended to the existing Counter() object but not replaced.
# First c object has a element 1 count of 4
# After updating new data count of 1 increased to 5.

# The count of elements in the Counter() can be zero and Negative also.

c1 = Counter()
c2 = Counter()

c1.update(A=4, B=3, C=10)
c2.update(A=10, B=3, C=4)

c1.subtract(c2)

print(c1)

print(Counter(['blue', 'red', 'blue', 'yellow', 'blue', 'red']))


# Once initialized, counters are accessed just like dictionaries.
# Also, it does not raise the KeyValue error (if key is not present) instead the value’s count is shown as 0.

colors = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']

colors_counter = Counter(colors)

print(f"The count of the color green in the colors_counter is : {colors_counter['green']}")
print(f"The count of the color orange in the colors_counter is : {colors_counter['orange']}")

# The elements() method returns an iterator that produces all the items known to the Counter.
# Note : Elements with count <= 0 are not included.

c3 = Counter([7,2,8,1,3,2,4,6,8,9,6,5,4,1,2,3,5])
c4 = Counter([7,2,6,8,9,6,5,4,1,2,3,5,4,8,4,3])
c3.subtract(c4)
print(c3)

print(c3.elements())  # {2: 1, 1: 1, 7: 0, 8: 0, 3: 0, 6: 0, 9: 0, 5: 0, 4: -1}
print(list(c3.elements()))  # Prints 2,1 as 2 and 1 are the only elements with +ve count in the c3 counter object

c5 = Counter(a=3,b=-4,c=0,d=6,e=2)

print(list(c5.elements()))

# most_common() is used to produce a sequence of the n most frequently
# encountered input values and their respective counts.
# Returns List of tuples, Each tuple have 2 elements
# index 0 of tuple is element name and index1 element of tuple is the count of that element

coun = Counter(a=1, b=2, c=3, d=120, e=1, f=219)

print(coun.most_common(3))

# can use for loop as,

for item,value in coun.most_common(3):

    print(item,':',value)

print(issubclass(Counter,dict))
print(isinstance(coun,Counter))
print(type(coun))

print("************************************************************************")

# Python supports a type of container like dictionaries called “namedtuple()” present in the module, “collections“.
# Like dictionaries, they contain keys that are hashed to a particular value.
# But on contrary, it supports both access from key-value and iteration, the functionality that dictionaries lack.

# namedtuple() is used to create a namedtuple object
# Syntax : class collections.namedtuple(typename, field_names)

Student = namedtuple('Student',['fname','lname','age','country']) # namedtuple() declaration

# Let's add data

s1 = Student('yokesh','chowdary',23,'india')

# printing the namedtuple() object :

print(s1)

# Accessing via index

print(s1[0], s1[1], s1[2], s1[3])

# Accessing using a for loop

for item in s1:

    print(item)

# Accessing using a for loop range()

for item in range(len(s1)):

    print(s1[item])

# Accessing using key 'names'

print(s1.fname)
print(s1.lname)
print(s1.age)
print(s1.country)

# Accessing using getattr() method

print(getattr(s1,'age'))

# There are 5 ways to access data from the namedtuple() object as shown above.

# namedtuple() is immutable, so we cannot modify after their creation.
try:
    s1.fname = 'yokiyokee'

except AttributeError as e:

    print(e)


# some methods on namedtuple()
# _make() :- This function is used to return a namedtuple() from the iterable passed as argument.

data_list = ['kusuma','chowdary',24,'india']

print(Student._make(data_list))

# The above returning can be assigned to a variable to make that variable as an object of type 'Student'.

s2 = Student._make(data_list)

for item in s2:

    print(item)


# We can make an namedtuple() object into a dictionary using _asdict() method
# _asdict() :- This function returns the OrderedDict() as constructed from the mapped values of namedtuple().
print(s2._asdict())

# using “**” (double star) operator :- This function is used to convert a dictionary into the namedtuple().

another_data_list = {'fname':'hema','lname':'chowdary','age':23,'country':'india'}

s3 = Student(**another_data_list) # Unpacking the dictionary into keyword arguments using ** spread operator

print(s3)


# _fields: This function is used to return all the keynames of the namespace declared.

print(s3._fields) # returns a tuple with field names

s4 = s3._replace(fname = 'hema sree')

print(s4)

# NOTE : _replace() returns the new object of 'Student' type
# s3 will not be affected here
print(s3)

# Look, s3 has fname = 'hema' and s4 has fname = 'hema sree'

# Let's check whether s3 and s4 are equal in memory

print(s3 is s4) # False as they both are different objects

print(len(s3)) # gives number of fields s3 object has

# How namedtuple() differ from inbuilt dict() ??

# 1) namedtuples() are immutable but dicts() are mutable data types.
# 2) Accessing data in namedtuple() is very easy when compared to dict()
#    as namedtuple.fname is easier than my_dict['fname'].
# 3) Can access data via indexing in namedtuple() but not possible in dict()
# 4) Creating a namedtuple() is user friendly
#    mynamedtuple = MyNamedTuple(firstvalue, secondvalue) is easy when compared to
#    mydict = {'fieldname': firstvalue, 'secondfield': secondvalue}
# 5) In dicts, only the keys have to be hashable, not the values.
#    namedtuples don't have keys, so hashability isn't an issue
# 6) Tuples are immutable, whether named or not. namedtuple only makes the access more convenient,
#    by using names instead of indices. You can only use valid identifiers for namedtuple,
#    it doesn't perform any hashing — it generates a new type instead.
# 7) Dictionary lies between a plain tuple and a named tupled in terms of performance and readability.
#    Named tuples clearly win in readability but lag in creation and access times.
#    Plain tuples are fast to create and access but using indices 0, 1, 2 makes my head spin

print("************************************************************************")
# Deque (Doubly Ended Queue) in Python is implemented using the module “collections“.
# Deque is preferred over a list in the cases where we need quicker append and
# pop operations from both the ends of the container, as deque provides an O(1) time complexity
# for append and pop operations as compared to list which provides O(n) time complexity.

# Syntax : collections.deque([iterable[, maxlen]])

# deque() is mutable data type
# Supports indexing and do not support slicing

print(deque())   # Empty deque
print(deque(range(10))) # deque filling with range()
print(deque((1,2,3,4,5)))  # deque using tuple
print(deque([1,2,3,4,5]))  # deque using list
numbers = {"one": 1, "two": 2, "three": 3, "four": 4}
print(deque(numbers))  # deque using dictionary (takes keys by default)
print(deque(numbers.keys()))  # deque using dictionary keys
print(deque(numbers.values())) # deque using dictionary values
print(deque(numbers.items()))  # deque using dictionary items which is a list of tuples
print(deque('abrakadabra'))

# appendleft() and popleft() methods

even_nums = deque([2,4,6,8,10])

print(even_nums) # deque initially

even_nums.popleft() # pops 2
even_nums.popleft() # pops 4

print(even_nums) # deque after popping 2 items from left

even_nums.appendleft(4) # adds 4 from left
even_nums.appendleft(2) # adds 2 from left

print(even_nums) # deque after appending popped items from left

# In the above We popped 2 items from left and again re appended those 2 items from left

# append() and pop() methods

even_nums.pop() # pops 10
even_nums.pop() # pops 8

print(even_nums) # deque after popping 2 items from right

even_nums.appendleft(8) # appends 8 from right
even_nums.appendleft(10) # appends 10 from right

print(even_nums) # deque final

''' deque is implemented as a doubly linked list. 
So, every item in a given deque holds a reference (pointer) to the next and previous item in the sequence.
Doubly linked lists make appending and popping items from either end light and efficient operations. 
That’s possible because only the pointers need to be updated. 
As a result, both operations have similar performance, O(1). 
They’re also predictable performance-wise because there’s no need for reallocating memory 
and moving existing items to accept new ones.
Appending and popping items from the left end of a regular Python list requires shifting all the items, 
which ends up being an O(n) operation. Additionally, adding items to the right end of a list often requires Python 
to reallocate memory and copy the current items to the new memory location. After that, it can add the new items. 
This process takes longer to complete, and the append operation passes from being O(1) to O(n).'''


# Python’s deque returns mutable sequences that work quite similarly to lists.
# Besides allowing you to append and pop items from their ends efficiently, deques provide a
# group of list-like methods and other sequence-like operations to work with items at arbitrary locations.

vowels = deque('abde')
print(vowels) # deque initially
vowels.insert(2,'c')
print(vowels) # deque dynamically expanded
vowels.remove('c')
print(vowels) # deque after removing 'c', deque shrank dynamically

# Can use indexing to get elements as,

print(vowels[0])
print(vowels[-1])
# print(vowels[1:3]) gives error as deque() do not allow slicing
'''Deques support indexing, but interestingly, they don’t support slicing. 
When you try to get a slice from a deque, you get a TypeError. 
In general, performing a slicing on a linked list would be inefficient, so the operation isn’t available.'''

# extend() and extendleft() is used to append multiple values into deque()

odd_nums = deque([1,2,3])
print(odd_nums) # deque initially
odd_nums.extend([4,5,6])
print(odd_nums) # deque after using extend() that adds items from right
odd_nums.extendleft([7,8,9])
print(odd_nums) # deque after using extendleft() that adds items from left
# In the above line first 7 is added then 8,9 is added to the left of odd_nums deque
# That means first element of the iterable is appended from left followed by the rest of elements in the iterable.
# Calling extendleft() with an iterable extends the target deque to the left.
# Internally, extendleft() performs a series of individual appendleft() operations that process
# the input iterable from left to right.
# This ends up adding the items in reverse order to the left end of the target deque.

# index(element,start,stop), count() and reverse()

some_data = deque([1,2,3,4,5,6,7,8,9,2,4,6,8,1,3,5,7,9])

print(some_data.index(3,0,len(some_data))) # 3 is at 2nd position
print(some_data.index(3,6,len(some_data)))

print(some_data.count(7)) # 7 is repeated 2 times so count = 2

some_data.reverse()

print(some_data)

# rotate(-value), rotate(value)
# This function rotates the deque by the number specified in arguments.
# If the number specified is negative, rotation occurs to the left. Else rotation is to right.

raw_data = deque([2,3,5,7,11,13,17,19])

print(raw_data) # original deque
# rotate() by default has value of 1

raw_data.rotate()

print(raw_data)

raw_data.rotate(5)

print(raw_data)

raw_data.rotate(-5)

print(raw_data)

raw_data.rotate(-1)

print(raw_data) # came back to original deque

# max_len parameter in deque()
# when max_len is used while creating deque() , deque appends items of iterable starting from the last as,
# If you want to create a empty deque with specified max-length use the below syntax,
# some_var = deque(maxlen = value)
four_numbers = deque([0,1,2,3,4],4)
print(four_numbers) # deque has 1,2,3,4 as we gave max_len as 4
# elements are added from the left of the deque starting from the last index of iterable
# Next 4 is added to deque from left, count = 1
# Next 3 is added to deque from left, count = 2
# Next 2 is added to deque from left, count = 3
# Next 1 is added to deque from left, count = 4
# Limit reached, So no further adding of elements

# What if we append even the limit is reached ?
four_numbers.append(5)
print(four_numbers)
# Notice , now deque has 2,3,4,5 instead of 1,2,3,4
# Because appending 5 from right of deque will pop out one element
# from left to maintain the maximum length of 4. Thats why deque
# automatically removes 1 from deque(1,2,3,4)

four_numbers.append(6)
print(four_numbers)

four_numbers.appendleft(2)
print(four_numbers)

four_numbers.appendleft(1)
print(four_numbers)

# We can get the maximum length of deque as,
print(four_numbers.maxlen)

print("************************************************************************")

# deque() real time examples

# Having a maxlen to restrict the maximum number of items makes deque suitable for solving several problems.
# For example, say you’re building an application that scrapes data from search engines and social media sites.
# At some point, you need to keep track of the three last sites your application requested data from.

websites = (
    'google.com',
    'yahoo.com',
    'bing.com'
)

pages = deque(maxlen = 3)

for site in websites:

    pages.appendleft(site)

print(pages) # Top 3 used websites till now

pages.appendleft('facebook.com')

print(pages) # Top 3 used websites after 12 hours

pages.appendleft('instagram.com')

print(pages) # Top 3 used websites after 24 hours

print("************************************************************************")

# A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries.

# Syntax : class collections.ChainMap(dict1, dict2)

print(ChainMap()) # empty ChainMap

dd1 = {'a': 1, 'b': 2}
dd2 = {'c': 3, 'd': 4}
dd3 = {'e': 5, 'f': 6}

chainmap = ChainMap(dd1,dd2,dd3)

print(chainmap)


# You can also create ChainMap objects using the class method .fromkeys().
# This method can take an iterable of keys and an optional default value for all the keys:

print(ChainMap.fromkeys(['one','two','three'])) # By default, value = None for all keys
print(ChainMap.fromkeys(['one','two','three'],0))
print(ChainMap.fromkeys(['one','two','three'],[1,2,3]))


# ChainMap supports the same API as regular dictionaries for accessing existing keys.
# Once you have a ChainMap object, you can retrieve existing keys with
# dictionary-style key lookup, or you can use .get():

print(chainmap['a'])
print(chainmap.get('f'))
print(chainmap.get('g',9999))  # 9999 acts as default value for dd3 unavailable key

# Without providing default value python raises 'KeyError'

try:

    print(chainmap['l'])

except KeyError:

    print("The key is not available in the dd2")

# A key lookup searches all the mappings in the target chain map until it finds the desired key.
# If the key doesn’t exist, then you get the usual KeyError.
# Now, how does a lookup operation behave when you have duplicate keys?
# In that case, you get the first occurrence of the target key:

for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
vet_treatment = {"dogs": 4, "cats": 3, "turtles": 1}
pets = ChainMap(for_adoption, vet_treatment)

print(pets)

print(pets['dogs'])
print(pets.get('cats'))

'''When you access a duplicate key, such as "dogs" and "cats", the chain map only 
returns the first occurrence of that key.
Internally, lookup operations search the input mappings in the same order they appear in the internal list of mappings, 
which is also the exact order you pass them into the class’s initializer.'''
# If the order is pets = ChainMap(for_adoption, vet_treatment) then, accessing pets['dogs']
# will return 4 as we need to follow the order of dicts we passed into ChainMap().

# The above behavior is observed while iterating also
for key in pets:
    print(key, "->", pets[key])

for key in pets.keys():
    print(key, "->", pets[key])

for value in pets.values():
    print(value)

# Again, the behavior is the same.
# Every iteration goes through the first occurrence of each key, item, and value in the underlying chain map.
# Can use pets.keys(), pets.values() and pets.items() same as these methods used on normal dicts.

print(pets.keys())
print(list(pets.keys()))
print(pets.values())
print(list(pets.values()))
print(pets.items())
print(list(pets.items()))

# maps() : This function is used to display keys with corresponding values of all the dictionaries in ChainMap.
# maps() returns List of dictionaries that are passed to ChainMap() constructor

new_dic = pets.maps
print(new_dic)

print(new_dic[0])
print(new_dic[1])

# ChainMap also supports mutations.
# In other words, it allows you to update, add, delete, and pop key-value pairs.
# The difference in this case is that these operations act on the first mapping only:
# That means changes made are reflected only on first element/dictionary of ChainMap()

nums_listt = {"one": 1, "two": 2}
letters_listt = {"a": "A", "b": "B"}
nums_letters = ChainMap(nums_listt,letters_listt)
print("Initially nums_letters is :",nums_letters)

# Adding new key-value pair
nums_listt['c'] = 'C'
print("nums_letters after adding a new key-value :",nums_letters)

# Updating existing key
nums_listt['b'] = 'b'
print(nums_letters)

# popping keys
print(nums_letters.pop('two'))

try:

    print(nums_letters.pop('a'))

except Exception as e:

    print(e)

# deleting keys
del nums_letters['c']
print("nums_letters after deleting a key named 'c' :",nums_letters)

try:

    del nums_letters['a']

except Exception as e1:

    print(e1)


# clearing
nums_letters.clear()
print(nums_letters)

# FinalThoughts :
# Operations that mutate the content of a given chain map only affect the first mapping,
# even if the key you’re trying to mutate exists in other mappings in the list.
# For example, when you try to update "b" in the second mapping,
# what really happens is that you add a new key to the first dictionary.
# 1) Adding new key to ChainMap object will reflect in the first dictionary of ChainMap()
# 2) Updating a key with new value will rename the value if the exists in the first dictionary of ChainMap
# else, a new key-value pair is created in the first dictionary of ChainMap
# 3) popping will permanently remove key-vcalue pair from ChainMap object if that key is available in the
# first dictionary else key error is raised
# 4) deleting also follows the same rule mentioned in above line
# 5) clear() method empties the first dictionary of the ChainMap object

# You can take advantage of this behavior to create updatable chain maps that don’t modify your
# original input dictionaries. In this case, you can use an empty dictionary as the first argument to ChainMap:

numbers111 = {"one": 1, "two": 2}
letters111 = {"a": "A", "b": "B"}
alpha_num111 = ChainMap({}, numbers111, letters111)

print(alpha_num111)

alpha_num111["comma"] = ","
alpha_num111["period"] = "."

print(alpha_num111)

# Here, you use an empty dictionary ({}) to create alpha_num.
# This ensures that the changes you perform on alpha_num will never affect your two original input dictionaries,
# numbers and letters, and will only affect the empty dictionary at the beginning of the list.


# can use reverse(0 method to reverse the contents

alpha_num111.maps.reverse()

print(alpha_num111)


# new_child() and parents are one of the most important methods in ChainMap()

mom = {"name": "Jane", "age": 31}
dad = {"name": "John", "age": 35}

family = ChainMap(mom, dad)
print(family)
ChainMap({'name': 'Jane', 'age': 31}, {'name': 'John', 'age': 35})

son = {"name": "Mike", "age": 0}

family = family.new_child(son)

print(family)

# We can get the original family by ignoring 'son' dictionary using parents
# Another interesting feature of ChainMap is .parents. This property returns a new ChainMap instance
# with all the mappings in the underlying chain map except the first one.
# This feature is useful for skipping the first mapping when you’re searching for keys in a given chain map

print(family.parents)

# With .new_child(), you can create a subcontext that you can update without altering any of the existing mappings.
# For example, if you call .new_child() without an argument, then it uses an empty dictionary
# and places it at the beginning of .maps. After this, you can perform any mutations over
# your new empty mapping, keeping the rest of the mapping read-only.

print(family.new_child())
print(family.parents)


# ChainMap vs Dictionary

dict_one = {'prime':2,'not_prime':3}
dict_two = {'even':2,'odd':3}

# 2 dicts with non-repeatable data will have no effect when compared

dict_chain_map = ChainMap(dict_one,dict_two)
dict_normal = {}
dict_normal.update(dict_one)
dict_normal.update(dict_two)

print(dict_chain_map)
print(dict_normal)

print('\n')

# The real problem raises when 2 dicts has some duplicates in them as,

dict_primes = {'prime1':2,'prime2':3,'prime3':5}
dict_odds = {'prime2':7,'prime3':11}

dict_chained = ChainMap(dict_primes,dict_odds)

dict_normals = {}
dict_normals.update(dict_primes)
dict_normals.update(dict_odds)


# While accessing ChainMap() only uses first occurences and ignores duplicates
# While accessing dict() only uses last occurences and ignores previous duplicates

for item in dict_chained:

    print(item,'->',dict_chained[item])

print('\n')

for item in dict_normals:

    print(item,'->',dict_normals[item])

# Look at the differences in the output

