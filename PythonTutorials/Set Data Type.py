# Python sets are classified into 2 types.
'''
1) sets formed with set() is called mutable set.
2) sets formed with frozenset() is called immutable set.
3) mutable set should have immutable elements only.
4) mutable set should not have mutable items like lists,sets and dicts.
5) sets are unindexed,unordered,doesn't allow duplicates and unchangeable.
'''
# How to declare sets?
# Don't use {} to form a empty set as {} resembles empty dictionary by default, so use set() constructor.

my_empty_set = set()
my_empty_dict = {}

print(type(my_empty_set))
print(type(my_empty_dict))

# We can use either of set() or {} to initialize a set with items,

set1 = {'hello','hi','bye'}
set2 = set('hello')

print('set formed using {} is : ',set1)
print('set formed using set() is : ',set2)

# {} or set() wont take mutable objects as input, i.e, dicts,lists and sets
# mutable datatypes are unhashable.
# immutable datatypes are hashable.

# set_a = {[1,2,3,4]}
# print(set_a)
# set_b = {{'one':1,'two':2}}
# print(set_b)
# set_c = {{'a','p','p','l','e'}}
# print(set_c)

print("***The lines from 29 to 34 gives error because , sets formed using {} with mutable elements gives error***")
print("***To overcome these errors use set() constructor***")

set3 = set([1,2,3,4])
print(set3)
set4 = set({'one':1,'two':2})
print(set4)
set5 = set({'a','p','p','l','e'})
print(set5)

print("***Use set() method to give mutable types as elements to a set***")
# How set() constructor overcome the error,

'''
In line 39,41 and 43, Unpacking of list,dict and sets are occurred
'''
print("***We can use mutable data types to create a set with {} using unpacking operators***")
print({*[1,2,3,4]})
print({**{'one':1,'two':2}})
print({*{'a','p','p','l','e'}})

print("**********************************************************************************")
print("***Adding and Removing items to/from the set***")
'''
add(),update(),remove(),discard(),pop(),del
'''
# Though we can't modify the existing elements in the set, we can add/remove the elements from the set.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange") # for single item insertion at end of the set
print(thisset)

thisset.update({'kiwi','mango'}) # for multiple items insertion at end of the set
print(thisset)

thatset = {'milk','bread'}
thatset.update(['coconut milk','brown bread']) # list unpacking occurs implicitly
print(thatset)

thosesets = {'india'}
thosesets.update({'russia':'friend','usa':'dosth'})  # By default unpacking occurs and
                                                     # keys of dictionaries are considered
print(thosesets)
# can add a set to set, but unpacking occurs to that set implicitly.
cheese_set = {'indian cheese'}
cheese_set.update({'usa cheese','russian cheese'})
print(cheese_set)

milk1 = {'heritage','dodla'}
milk1.add(('abc','xyz'))
print(milk1)

'''
add() takes exactly one parameter so, it must be immutable parameter like the above line 85
But, List with 1 element can be unpacked and can be used with add() method as,
But, list with more elements can't be used as parameter to a list, 
For the lists with more items, we can loop through it and can add every looped item into set individually.
Using update() we can add any number of items into a set, no limit !
'''
milk1.add(*['farm diary'])
print(milk1)

to_be_removed_set = {'a','b','c','d','e','f','g'}
to_be_removed_set.remove('g')
print(f'set after removing item \'g\' : {to_be_removed_set}')

# If we specify item that is not present in set, it raises key error.

try:
    to_be_removed_set.remove('x')
except:
    print('x is not present in the set')

# To overcome this error , use discard() method
to_be_removed_set.discard('e')
print(to_be_removed_set)

to_be_removed_set.discard('x') # wont give error
print(to_be_removed_set)

# pop() removes random item from the set, we don't know which item is going to be popped out.

popped_item = to_be_removed_set.pop()
print('popped item is : ',popped_item)

print(f'set after popping item : {to_be_removed_set}')

# clear empties the list.
to_be_removed_set.clear()
print(to_be_removed_set)

# del completely deletes the set from the memory

to_be_deleted = {'apple','banana'}
del to_be_deleted
# printing to_be_deleted will raise error.

print("**********************************************************************************")
print("******set operations******")

print("***union(), | operator***")
# 1) set union using union() method and | operator
# 2) Returns all elements from both sets
u1 = {'a','b','c','d','e'}
u2 = {'a','e','i','o','u'}

u3 = u1.union(u2)
u4 = u2.union(u1)

u5 = u1 | u2
u6 = u2 | u1

print(u3)
print(u4)
print(u5)
print(u6)

print("***update(), |= operator")
# 1) update() and |= adds set2 elements to set1.

sample_fruit = {'apple','banana'}
sample_fruit.update('kiwi')
print(sample_fruit)

sample_fruit |= {'mango','grape'}
print(sample_fruit)


print("***intersection() method,& operator***")
'''
1) Returns items that are common in both sets.
'''
u7 = {'a','b','c'} & {'a','e','i'}
print(u7)

u8 = {'a','b','c'}.intersection({'a','e','i'})
print(u8)

print("***intersection_update() method, &= operator***")

movies1 = {'bahubali','avatar','f2'}
movies2 = {'bahubali','f1','khaleja'}

movies1.intersection_update(movies2) # updates the common items in both sets to movies1.
print(movies1) # prints 'bahubali' as common b/w both sets is bahubali.

# Now movies1 contains only 1 item i.e, 'bahubali'

movies2.intersection_update(movies1)
print(movies2)

movies3 = {'a','b','c'}
movies4 = {'b','d','e'}

movies3 &= movies4
print(movies3)  # common item b/w movies3 and 4 is 'b', so movies3 is updated with only 1 item i.e, 'b'

# now movies3 set has only 1 item , i.e, 'b'

movies4 &= movies3
print(movies4)

print("***difference() method, - operator***")
diff1 = {1,2,3,4,5,6}
diff2 = {1,3,5,7,9,11}

print(diff1 - diff2) # returns those elements from diff1 which are not in diff2
print(diff2 - diff1) # returns those elements from diff2 which are not in diff1

print(diff1.difference(diff2))
print(diff2.difference(diff1))

print("***difference_update()  method, -= operator***")
diff3 = {2,4,6,8}
diff4 = {4,8,12,16}

diff3.difference_update(diff4)
print(diff3) # Now, diff3 becomes {2,6}

diff4.difference_update(diff3)
print(diff4)

print("***symmetric_difference() method and ^ operator***")
sd1 = {1,2,3,4,5,6,7,8,9}
sd2 = {2,4,6,8,10}

# Returns the unmatched elements from both sets,
print(sd1 ^ sd2)
print(sd2 ^ sd1)

print(sd1.symmetric_difference(sd2))
print(sd2.symmetric_difference(sd1))

print("***symmetric_difference_update() method and ^= operator***")
sd3 = {1,2,3,4,5,6,7,8,9}
sd4 = {2,4,6,8,10}

sd3.symmetric_difference(sd4)
print(sd3) # The output is updated to sd3, now sd3 has {1, 2, 3, 4, 5, 6, 7, 8, 9}

sd4.symmetric_difference_update(sd3)
print(sd4)

print("****isdisjoint() method***")
# If 2 sets give no value on intersection() method, then isdisjoint() returns True.
print({1,2,3}.isdisjoint({4,5,6}))   # No common value in both sets
print({2,4,6}.isdisjoint({4,8,12}))  # 4 is the common value in both sets

print("***issubset() method, <= operator***")
# If left operand is a part of right operand,then it returns True

print({1,2}.issubset({1,2,3,4}))
print({3}.issubset({1,2,4,5,}))
print({4}.issubset({4}))
print({1,2} <= {1,2,3,4})
print({1,2} <= {1,2})
print(set() <= set())
print("***Issuperset() method, >= operator***")
# If left operand contains right operand items, then it returns True

print({2,4,6,8} >= {2,4})
print({1,2}.issuperset({1}))
print({1,2}.issuperset({1,2}))
print({1,2} >= {1,2})
print(set() >= set())

print("***A<B and A>B***")
print("**proper subsets and supersets**")
'''
1) A<B evaluates to True if, A<=B and A!=B(means lengths of both sets should not be equal)
2) A proper subset is the same as a subset, except that the sets can’t be identical. 
   A set x1 is considered a proper subset of another set x2 if every element of x1 is in x2, 
   and x1 and x2 are not equal.
3) A>B evaluates to True if, A>=B and A!=B(means lengths of both sets should bot be equal)
4) A proper superset is the same as a superset, except that the sets can’t be identical.
   A set x1 is considered a proper superset of another set x2 if x1 contains every element of x2,
   and x1 and x2 are not equal.
5) A<B determines whether A is a proper subset of B
6) A>B determines whether B is a proper superset of B
'''

print({1,2,3} < {1,2,3,4}) # True because set1 items available in set2 and len(set1) != len(set2)
print({1,2,3} < {1,2,3})  # False because even set1 items available in set2 but len(set1) == len(set2)

print({1,2,3,4,5} > {1,2,3,4}) # True because set2 items available in set1 and len(set1) != len(set2)
print({1,2,3,4} > {1,2,3,4})  # False because set2 items available in set1 but, len(set1) == len(set2)


print("***********************************************************************************************")
print(len(set()))
print(len({1,2,3,4,5,6,6,7})) # duplicate value is removed.
print(max({'a','z','A','D','v'}))
print(min({'a','z','A','D','v'}))
print(max({12,21,33,7,2}))
print(min({12,21,33,7,2}))

print("**********************************************************************************************")
print("**joining 2 or more sets*****")

print({*{1,2,3},*{4,5,6},*{7,8,9}})

print({1,2,3} | {4,5,6} | {7,8,9})

pp_set = {1,2,3,4}
pp_set.update({5,6,7,8,9})
print(pp_set)

print("***********************************************************************************************")
print("*****Copying sets**********")
copy_set = {1,3,5,('apple',),'yoki'}


aliased_set = copy_set
copy_set.pop()
print(copy_set)
print(aliased_set)
print("changes made to copy_set is reflected in aliased_set")

copied_set1 = copy_set.copy()
print(id(copy_set))
print(id(copied_set1))
print("set copied via copy() method creates a new set at new memory location!")

copied_set2 = set(copy_set)
print(id(copy_set))
print(id(copied_set2))
print("set copied using set() constructor creates new set in memory")

copied_set3 = {*copy_set}
print(id(copy_set))
print(id(copied_set3))
print("set copied using unpacking original set into {} creates new set in the memory")

print("************************************************************************************")
