'''
1) Dictionaries are Mutable datatypes.
2) For every dict() object creation, python allocates new memory address to each object.
3) Same as lists, for every unique or same dict() objects with same content in the same order of -
- elements, python creates different memory locations.\
4) The only difference between mutable list and mutable dict is,
--- 2 lists with same elements in the same order will have different memory locations,
    and == operator returns True.
--- 2 lists with same elements in the different order will have different memory locations,
    and == operator returns False.
--- 2 dicts with same elements in the same order / different order returns True only.
5) Same as Lists, dict will never undergo interning.
'''

# proof:
print("********************************************************************************")
print("******List Behavior******")
l1 = [1,2,3,['a','b','c']]
l2 = [1,2,3,['a','b','c']]
l3 = [['a','b','c'],1,2,3]

print(id(l1), id(l2), id(l3))

print(l1 == l2)
print(l2 == l3)
print(l3 == l1)

print("******Dict Behavior******")
d1 = {'one':1,'two':2,'three':3,'my_list':[1,2,3]}
d2 = {'one':1,'two':2,'three':3,'my_list':[1,2,3]}
d3 = {'three':3,'my_list':[1,2,3],'one':1,'two':2}

print(id(d1), id(d2), id(d3))

print(d1 == d2)
print(d2 == d3)
print(d3 == d1)

print("********************************************************************************")
print('****dict() aliasing and copying****')
x0 = {'whole':'hole','holy':'moly'}
x1 = x0
# changes made t0 x0 will reflect in x1 due to aliasing,

x0.update({'rat':'cat'})

print(x0)
print(x1)
print(id(x0),id(x1)) # Both memory locations are same due to aliasing
# Techniques to copy,

x2 = dict(x0)

print(id(x0), id(x2)) # Both memory locations are not same as we created new dictionary

x3 = x0.copy()
print(id(x0),id(x3))

x4 = x0 | dict()
print(id(x0), id(x4))





