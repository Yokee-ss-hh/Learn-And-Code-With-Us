'''
1) frozenset() is an in-built function in python that takes iterable as argument and make them immutable.
2) frozenset() items are immutable, we can't add new items to frozenset object,-
-we can't remove the items from frozenset object.
3) frozenset() is also called immutable set.
4) Like sets, frozenset() takes mutable(it will implicitly unpacks them) and immutable data types as arguments into it.
5) frozenset() exactly takes one argument only, if we try to give 2 arguments it raises error.
6) Same like sets, frozensets should have immutable items only, if the input iterables to the frozenset()-
- have mutable items, then error(Unhashable list) is raised.( see line 12,13).
'''

# print(frozenset([1,2,3,[4,5]]))
# The above line prints error as , the list iterable has a list datatype as one of the element.

# print(frozenset((1,2,3,[4,5])))
# The above line prints error as , the tuple iterable has a list datatype as one of the element.


f_list = [2,4,6,'a','e']
f_tuple = (1,3,5,'i','o')
f_dict = {'one':1,'two':2,'twenty three':23}
f_set = {'apple','banana','cherry',23,3.321}

a = frozenset(f_list)   # the list is unpacked impllicitly
b = frozenset(f_tuple)  # the tuple is unpacked impllicitly
c = frozenset(f_dict)   # the dict is unpacked impllicitly
d = frozenset(f_set)    # the sett is unpacked impllicitly

print(a)
print(b)
print(c)
print(d)

'''
6) We can give multiple arguments to frozenset() using unpacking technique,later merging under one-
- entity to either list/tuple.
'''
e = frozenset([*f_list,*f_tuple])
print(e)

'''
7) We cannot change and remove existing items of frozenset after it is created.
'''

print(sum(frozenset([1,2,3,4,5])))
print(sum(frozenset((1,3,5,7,9))))
print(max(frozenset(["a",'e','B']))) # can use tuple/set in place of list
print(min(frozenset(['a','e','B']))) # can use tuple/set in place of list

print(max(frozenset([33,0,-21])))    # can use tuple/set in place of list
print(min(frozenset([-321,999,32]))) # can use tuple/set in place of list


'''
8) As we know, tuples are immutable lists, similarly frozensets are immutable sets.
9) As items in the tuple cannot be changed after its creation, frozenset items also cannot be changed after-
- it's creation.
10) As tuples are converted back to lists for adding new items and deleting existing items, similarly-
- frozensets are converted to sets for adding new items and removing existing items.
11) After doing our work , we can revert back to our tuple and frozenset again using tuple() and frozenset()-
- constructors.
'''

print("*************************************************************************************")
print("**frozenset items modifying techniques**")

frozed_set = frozenset([1,2,3])
print(f"Frozed Set before changes : {frozed_set}")
# frozed_set.add(4)
# print(frozed_set) , gives error as item assignment is not supported for frozen sets.

unfrozed_set1 = set(frozed_set)
unfrozed_set1.add(4)
frozed_set = frozenset(unfrozed_set1)
print(f"Frozed Set after changes : {frozed_set}")
# similarly, we can delete an existing item from frozenset

unfrozed_set2 = set(frozed_set)
unfrozed_set2.pop()
frozed_set = frozenset(unfrozed_set2)
print(f"Frozed Set after removing random item : {frozed_set}")

print("In the above, we added new item 4 into frozenset using add() and removed one "
      "random item from frozenset using pop()")

print("*********************************************************************************")
print("As frozensets are immutable, so even copying of original frozenset, the copied frozenset will "
      "have same memory address, The same behavior is observed in immutable strings.")

f1 = frozenset([2,4,6,'a','e'])
f2 = frozenset([2,4,6,'a','e'])
print(f1 is f2)
# Only frozensets formed with frozenset() constructor will have different memory locations.

f3 = f1.copy()
print(f3 is f1) # Both f1 and f3 points to same memory

f4 = frozenset(f2)
print(f4 is f2) # Both f4 and f2 points to same memory

'''
Set Methods like union,intersection,difference,symmetric difference,issuperset,issubset,isdisjoint-
- works on frozen sets.
'''
print("***copying using copy module***")

cf1 = frozenset([1,2,3,4,5])

cf2 = copy.copy(cf1)
cf3 = copy.deepcopy(cf1)

print(cf1 is cf2)
print(cf1 is cf3)

# deep copying allocates new memory for the copied object. 
