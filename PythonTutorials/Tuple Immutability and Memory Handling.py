'''
The contents of the tuple after initialization are unchangeable.That means tuples are immutable.
'''

a = 'yokesh'

a = 'hello'

print(a) # prints hello, a breaks pointing to 'yokesh' object and starts pointing to 'hello' object
# That's how immutable objects can be changed their contents as elements can't be updated directly.

print("******************************************")
# Similarly tuples also behaves the same way as strings as both are immutable data types.

some_tuple1 = ('tuples',22,3.333)
print(type(some_tuple1))
print("ID Before Change",id(some_tuple1))
some_tuple1 = ('benz car',99.876)
print(type(some_tuple1))
print("ID After Changing whole tuple content",id(some_tuple1))

# In mutable data types like List, even 2 lists have same content both will have 2 different id's
# But in immutable data types like string and tuple, 2 variables with same content will have same id's.
# This is because of interning.

print("**************************************************************")
print('Do tuples have same id with elements in different order?')

t3 = (6+9j,'let us see',99.999,33)
t4 = ('let us see',33,99.999,6+9j)

print('Id of t3 : ',id(t3))
print('Id of t4 : ',id(t4))

# Absolutely No , As tuples follow Ordering of elements.

print(t3 is t4)
print(t3 == t4)

print("*************************************************************")
print('checking tuple interning with immutable datatypes as elements')
t1 = (12,31,7.789)
t2 = (12,31,7.789)

print('Id of t1 : ',id(t1))
print('Id of t2 : ',id(t2))

print(t1 == t2)
print(t1 is t2)
print('Conclusion : Tuples with only immutable datatypes will undergo interning.')
print("**************************************************************")
print('Checking tuple interning with mutable datatypes as elements')

t5 = ([1,2,3],[4,5,6])
t6 = ([1,2,3],[4,5,6])

print('Id of t5 : ',id(t5))
print('Id of t6 : ',id(t6))

print(t5 == t6)
print(t5 is t6)
print('Conclusion : Tuples with only mutable datatypes will not undergo interning.')

print("**************************************************************")
print('Checking tuple interning with both mutable and immutable data types as elements')

t7 = ('some_element',99,[1,3,5,7])

t8 = ('some_element',99,[1,3,5,7])

print('Id of t7 : ',id(t7))
print('Id of t8 : ',id(t8))

print(t7 is t8)
print(t7 == t8)
print('Conclusion : Tuples with both mutable and immutable datatypes will not undergo interning.')

print("**************************************************************")

print("***************************************************************************")
print("**tuple copying techniques***")
copy_tuple1 = (1,2,'tuple',('a','b'))  # tuple with immutable items
copy_tuple2 = ([1,2],[3,4])            # tuple with mutable items
copy_tuple3 = ((1,2),[3,4])            # tuple with both mutable and immutable items

c1 = copy_tuple1
c2 = copy_tuple2
c3 = copy_tuple3

print("aliasing of tuples")
list(copy_tuple1).pop()
list(copy_tuple2).pop()
list(copy_tuple3).pop()

print("copy_tuple1 and c1 after changes : ",copy_tuple1,c1)
print("copy_tuple2 and c2 after changes : ",copy_tuple2,c2)
print("copy_tuple3 and c3 after changes : ",copy_tuple2,c3)

print("We can see aliasing on all 3 tuples and on their aliases!")

c7 = tuple(copy_tuple1)
c8 = tuple(copy_tuple2)
c9 = tuple(copy_tuple3)

print(id(c7),id(copy_tuple1))
print(c7 is copy_tuple1)
print(id(c8),id(copy_tuple2))
print(c8 is copy_tuple2)
print(id(c9),id(copy_tuple3))
print(c9 is copy_tuple3)

print("No copying occurs when we try with tuple() constructor")

'''
tuples don't have any copy() method to perform copying, one method we discussed above.
So converting tuple to list and copying denotes list copying but not the tuple copying, so-
- immutable tuple doesn't need copying , even if we copy copied object points to the original tuple-
- address location only.
Similarly, immutable strings and frozensets behaves the same way.
'''
print("***copying using copy module***")

tple_one = ('1','2','three')

copyof_tple_one = copy.copy(tple_one)

print(tple_one is copyof_tple_one) # Both copied and original tuples are pointing to same address.

deepcopyof_tple_one = copy.deepcopy(tple_one)

print(tple_one is deepcopyof_tple_one) # Both are pointing to same address.
