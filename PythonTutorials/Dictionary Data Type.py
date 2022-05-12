# Dictionary is a mapping MUTABLE datatype.
# Dictionary follows OCI property i.e, Ordered, Changeable and Indexed.
# Dictionary won't allow duplicate item.
# Even 2 items with same key , python takes the last declared key and ignores the first one.
# Dictionary should have unique names for keys and can have same values for all values.

print("**************************************************************")
dict1 = {'bmw':'germany','toyota':'south korea','tata':'india','ford':'usa'}

print(dict1)           # o/p format : {key1:value1,key2:value2,..........}
print(dict1.keys())    # o/p format : dict_keys([...keys with comma...])
print(dict1.values())  # o/p format : dict_values([..values with commas...])
print(dict1.items())   # o/p format : dict_items([(key1,value1),(key2,value2),.........])

# To remove dict_keys, dict_values and dict_items from the above outputs, use list() or tuple().
print("**dict to list using list()**")
print(list(dict1))
print(list(dict1.keys()))
print(list(dict1.values()))
print(list(dict1.items()))

print("**dict to tuple using tuple()**")
print(tuple(dict1))
print(tuple(dict1.keys()))
print(tuple(dict1.values()))
print(tuple(dict1.items()))

'''
1) As dict() are mutable objects, for each object creation python creates a new memory.
2) Same like lists,two aor more dictionaries with same content and in the same order of elements will-
- be created a new memory for each by python.
'''
print("***********************************************************************")
print("****Dictionary Order and id  Check****")
dict2 = {'one':1,'two':2,'three':3}
dict3 = {'one':1,'two':2,'three':3}
dict4 = {'two':2,'three':3,'one':1}

print(f"ID of dict2 : {id(dict2)}")
print(f"ID of dict3 : {id(dict3)}")
print(f"ID of dict4 : {id(dict4)}")

print("Conclusion : Two dicts with same items in same order will have different memory locations.")
# The above conclusion happens because dict() are mutable items.
print("Conclusion : Two dicts with same items in different order will have different memory locations.")
# The above conclusion is True because dict()'s are ordered data types.

print(dict2 == dict3)
print(dict3 == dict4)
# IMPORTANT :
print("Conclusion : Two dicts with the same items in the same order or different order are equal!")

print("***********************************************************************")
print('***Dict() with duplicate keys are not allowed but values are allowed***')
dd1 = {'prime1':2,'prime2':3,'prime3':5,'prime4':7,'prime5':10,'prime5':11,'prime6':13,'prime7':13}
print(f"dict() with non duplicate keys and duplicate values is : {dd1}")

print("***********************************************************************")
print("****Dictionary Creation using dict() constructor****")
'''
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
'''
# *args and **kwargs in python.
# *args -> non-keyword arguments
# **kwargs -> keyword arguments

print(dict(a=2,b=3,c=4))

print(dict({"name":"yokesh","place":"india","age":23}))
print(dict({"name":"yokesh","place":"india","age":23},designation="SDE",company_type="product based"))

print(dict([('x',22),('y',44),('z',66)]))
print(dict([('x',22),('y',44),('z',66)],a=88))

print(list(zip([1,2,3],[4,5,6])))
print(dict(list(zip([1,2,3],[4,5,6]))))

print(tuple(zip([1,2,3],[4,5,6])))
print(dict(tuple(zip([1,2,3],[4,5,6]))))

print("****************************************************************************")
print("*******Accessing items in a dictionary****************")
# Trying to access keys which doesn't exist throws error.
favorite = {'fruit':'mango','vegetable':'potato','drink':'coconut water','dish':'biryani'}
# Accessing using key,
print(favorite['dish'])
# using get()
print(favorite.get('drink'))


# The returned list is a view of the items of the dictionary,
# meaning that any changes done to the dictionary will be reflected/ updated in the-
# - keys/values/items lists.
x1 = favorite.keys()
x2 = favorite.values()
x3 = favorite.items()

print(f"Keys before updating favorite dictionary : {x1}")
print(f"Values before updating favorite dictionary : {x2}")
print(f"Items before updating favorite dictionary : {x3}")

# let's update favorite with one item,

favorite['sport'] = 'cricket'

print(f"Keys after updating favorite dictionary : {x1}")
print(f"Values after updating favorite dictionary : {x2}")
print(f"Items after updating favorite dictionary : {x3}")


print("*************************************************************************")
print("*****Check if key,value exist in dictionary")

print("vegetable" in favorite)
print('dish' in favorite.keys())
print('biryani' in favorite.values())
print(('fruit','mango') in favorite.items())


print("**************************************************************************")
print("****Changing/Updating existing dictionary items and adding new items****")
names = {"name1":"yokesh","name2":"yoki","name3":"yokeee"}

# adding new item
names['name4'] = 'yokiyokee'
print(f'names after adding item4 is : {names}')

# using update() we can update existing item / we can add new item.
# If the key is already available in the dictionary, update() will override it.
names.update({'name4':'python baba'})
print(f'adding item using names dict() is : {names}')

# updating existing item using update() method,
names.update({'name4':'python dsa baba'})
print(f'updating existing name4 key with new value using update() method : {names}')

print("*****************************************************************************")
print("****Removing items from dictionary****")
to_be_deleted_dict = {'one':1,'two':2,'three':3,'four':4}

# pop() takes dict key as argument and deletes it.
to_be_deleted_dict.pop('four')
print(f'dict after using pop() method : {to_be_deleted_dict}')

# popitem() removes the last item in the dictionary,
to_be_deleted_dict.popitem()
print(f'dict after using popitem() is : {to_be_deleted_dict}')

# clear(0 empties the dictioanry
to_be_deleted_dict.clear()
print(f'dict after clearing it : {to_be_deleted_dict}')

# del keyword used to delete the whole dictionary in the memory
del to_be_deleted_dict
# print(to_be_deleted_dict) gives error as we deleted that dictionary.

print("****************************************************************************")
print("*****Looping through dictionary******")
loop_dict = {'p1':10,'p2':20,'p3':30,'p4':40}

for x in loop_dict:
    print(x, end=" ")   # prints keys by default

print('\n')

for x in loop_dict:
    print(loop_dict[x], end=" ") # prints values

print('\n')

for x in loop_dict.keys():
    print(x, end= " ")     # prints keys

print('\n')

for x in loop_dict.values():
    print(x, end=" ")    # prints values

print('\n')

for x,y in loop_dict.items():
    print(x,y)     # prints items


print("*********************************************************************")
print("****dictionary items copying****")
original_dict1 = {'A':67,'B':68,'C':69}
copied_via_assignment = original_dict1
# changes made to original_dict1 reflects in copied_via_assignment.
original_dict1['D'] = 70
print(copied_via_assignment)
print(original_dict1)

# So use copy() method
original_dict2 = {'odd1':1,'odd2':3,'odd3':5}
copied_via_copymethod = original_dict2.copy()
original_dict2 ['odd4'] = 7
print(original_dict2)
print(copied_via_copymethod)
# changes made to original_dict2 reflects in copied_via_copymethod.

print("**********************************************************************")
print("****Nested Dictionaries****")
Nations = {
    'India' : {
        'population' : 'billions',
        'major religion' : 'hindu',
        'langauge':'hindi'
    },
    'China' : {
        'population' : 'some billions',
        'major religion' : 'no religion',
        'language' : 'mandarin'
    },
    'australia' : {
        'population' : 'some millions',
        'major religion' : 'christianity',
        'language' : 'english'
    }
}

d1 = {'d11':1,'d22':2}
d2 = {'d33':3,'d44':4}
d3 = {'d55':5,'d66':6}

d = {
    'd1':d1,
    'd2':d2,
    'd3':d3
}

print("*******************************************************************************")
print("*****Joining 3 dictionaries*****")
j1 = {'even1':2,'even2':4}
j2 = {'even3':6,'even4':8}

j3 = dict(**j1,**j2)
print(j3)
# or
j4 = {**j1,**j2}
print(j4)

'''
**j1 is equal to unpacking of keyword arguments i.e, even1=2,even2=4
**j2 is equal to unpacking of keyword arguments i,e, even3=6,even4=8
Now,
**j1,**j2 is equal to even1=2,even2=4,even3=6,even4=8
dict(**j1,**j2) or {**j1,**j2} is equal to dict(even1=2,even2=4,even3=6,even4=8),
and returns final output as, {'even1': 2, 'even2': 4, 'even3': 6, 'even4': 8}
'''
# merging using update() method,
j5 = {}

j5.update(j1)
j5.update(j2)

print('merging j1 and j2 to form j5 is : ',j5)

# merging using | operator,
j6= j1 | j2
print('merging j1 and j2 using | operator to get j6 is : ',j6)

print("****************************************************************************")
# fromkeys() and setdefault() methods,
# fromkeys(iterable,value), default value : None
fk1 = [1,2,3]
fk2 = ('one','two','three')

fk_dict1 = dict.fromkeys(fk1,10)
fk_dict2 = dict.fromkeys(fk2)

print(fk_dict1)
print(fk_dict2)
print(dict.fromkeys(fk1,fk2))
print(dict.fromkeys('hello'))

print("*****setdefault()*****")
# setdefault(key,value[optional][default = None])

# When key is in the dictionary,
person1 = {'name1': 'Yokesh', 'age1': 23}

age1 = person1.setdefault('age1')
print('Person1 = ',person1)
print('Age1 = ',age1)

print(person1)

# When key is not in the dictionary,
person2 = {'name2': 'Phill'}
# key is not in the dictionary
salary2 = person2.setdefault('salary2')
print('person2 = ',person2)
print('salary2 = ',salary2)

# key is not in the dictionary
# default_value is provided
age2 = person2.setdefault('age2', 22)
print('person2 = ',person2)
print('age2 = ',age2)

print(person2)

print("**********************************************************************************")
print('***Why dict() keys should not be of type mutable***')
'''
1) After dict() is initialized with some content, python takes each and every key from the dictionary-
- and do hashing using hash() function.
2) The outputs of the hash() functions is used to store the values associated with those keys in the memory.
'''
hashable_dict = { 'tall': 12, 'grande': 16, 'venti': 20 }
print(hash('tall'))
print(hash('grande'))
print(hash('venti'))

# hashed value of each and every key are different from each other.
# Here all the keys are immutable data types, means these are not changeable.
print(hashable_dict['grande'])
# For the above line, python tells hash() function to do hashing for 'grande' key , hash() returns
# hashed value i.e, -7287751947317497759. This hashed value is used to locate the value associated
# with that key.
# If suppose(lets assume) grande is mutable, if someone changes grande to grandin, and hashing grandin
# using hash() function will not return -7287751947317497759, and we never know the value associated \
# with the key.
# That's why dict() keys should be immutable

# example = {[1,2,3]:'one'}, printing this we will get TypeError: unhashable type: 'list'

example = {(1,2,3):'tuple'}
print(example)

# This worked as (1,2,3) is immutable tuple data type.
