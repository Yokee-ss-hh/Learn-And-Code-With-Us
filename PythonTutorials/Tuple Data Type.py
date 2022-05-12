'''
There are 3 sequence data types in python
1) list
2) tuple
3) range
'''

# Tuples are Ordered, Indexed, Immutable, Allows Duplicates and Unchangeable.

# While creating a tuple with one item, remember to include a comma at the last.
# The comma tells python that this datatype is a tuple,
# If we don't include comma, python treats it as un defined variable / un-initialized string.
print("**tuple()**")
# passing string to tuple() will split each character into elements,
print(tuple('Python'))
print(tuple(' '))
tuple_from_list = tuple([1,2,3,'list'])
print(f"Tuple from the list : {tuple_from_list}")
a = {'a':1,'b':2,'c':3}
tuple_from_dict = tuple(a)
print(f"Tuple from dictionary : {tuple_from_dict}")
print(f"Tuple from dictionary Keys : {tuple(a.keys())}")
print(f"Tuple from dictionary Values : {tuple(a.values())}")
print("**tuples order check**")
t3 = ('one','two')
t4 = ('two','one')
print(t3 == t4) # Returns False as tuples are ordered.
print("***************************************")
t1 = ('hi','hello',123)
t2 = ('hi','hello',123)
print(t1 == t2)
print(t1 is t2)
print(id(t1),id(t2))
print("*****************************************")
tup0 = (12,) # tup0 = ('hi',)

tup1 = (12,'yoki',6+6j,2.2222)

print(f"Type of tup1 is : {type(tup1)}")

print(f"Length of tup1 is :{len(tup1)}")

# Allows duplicate,

tup2 = ('tuple','list','tuple')
print(f"Tuple with duplicates : {tup2}")

print("**Accessing Tuples**")
# Using slicing
tup3 = ('twitter','google','2300USD',999,9+99j,3.321)
print(tup3[2])
print(tup3[-3])
print(tup3[1:4])
print(tup3[2:5:-1]) # empty tuple comes as output
print(tup3[-2:-5]) # empty tuple comes as output
print(tup3[-5:-2])
# slicing using slice() constructor,
print(tup3[slice(0,3)])
print(tup3[slice(-1,-5,-1)])
print("\n")
print("**Updating tuple elements**")
'''
1) Tuples are immutable and unchangeable, so we cannot update them.
2) We can change tuple to list using list() constructor and we can modify them using list methods.
3) Like Lists we don't have slicing techniques to add items and we don't have built-in methods like-
- append(), insert(), extend().
4) Like lists we don't have methods to remove elements like remove(),pop(),clear().
5) Both lists and tuples have concatenation as common to add elements.
6) Both lists and tuples have del operator to delete respective iterable.
'''
# Concatenation works with tuple.
tup4 = (1,2,3)
tup5 = (4,5)
tup6 = tup4 + tup5
print(tup6)
print("\n")
print("**Removing tuple elements**")
tup7 = (3,6,9)
del tup7
# print(tup7) gives error.
print("\n")

print("**Packing and Unpacking Tuple**")
# Packing
packing_tuple = ('apple','banana','cherry')
print("Packing a Tuple example :",packing_tuple)
# Unpacking means assigning packed tuple elements to some variables.
a,b,c = packing_tuple
print(f"Unpacking tuple to variables : {a} b : {b} c : {c}")

# The number of variables must match the number of values in the tuple,
# if not, you must use an asterisk to collect the remaining values as a list.
# This *some_variable is called as args and generally it is a list with the elements
# *args = [element1,element2,element3,...]

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
*f1,f2,f3 = fruits
f4,*f5,f6 = fruits
f7,f8,*f9 = fruits

print(f'f1 : {f1} , f2 : {f2} , f3 : {f3}')
print(f'f4 : {f4} , f5 : {f5} , f6 : {f6}')
print(f'f7 : {f7} , f8 : {f8} , f9 : {f9}')

print(f"The second element in f1 is : {f1[1]}")

print("*********************************************************************")
print("**Joining tuples to existing tuples**")
t1 = ('one',1)
t2 = ('two',2)
t3 = t1+t2
print(t3)

print("**Tuple Repetetion**")
print(t1 * 5)

print("**count(value) and index(value,start,stop)**")

print('The count of 2 in the tuple is ',('one','two',1,2,3,21,2,1,2).count(2))
print('The index of 2 in the tuple is ',('one','two',1,2,3,21,2,1,2).index(2))
print('The second index of 2 in the tuple is ',('one','two',1,2,3,21,2,1,2).index(2,4))
print('The third index of 2 in the tuple is ',('one','two',1,2,3,21,2,1,2).index(2,7))

print("**All methods that work on tuples**")
'''
1) index(value,start,stop)
2) count(value)
3) concatenation operator '+'
4) Repetition operator '*'
5) len() method
6) tuple() constructor
7) slicing operator [start,stop,step]
'''
print("NOTE:Read the commented matter")
print("**************")
'''
For Updating and removing elements, use list() to convert tuple into list later use lists methods-
- to make changes to that list converted tuple, save the changes and later convert again to tuple.
'''
