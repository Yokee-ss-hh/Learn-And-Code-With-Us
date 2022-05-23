# Booleans are either True / False depending on the logic of the statement we executes
a = 1
b = 0
 
visited = True 
print(bool(a))
print(bool(b))
print(type(bool(a)))
print(type(bool(b)))

# bool comes under <class 'bool'> 
# comparsion and logical opeartors gives bool as output.

print(type(True) is bool)
print(visited == bool(1))

# if and while uses bool to start the execution
# In-Built any() and all() functions uses 
print("*********boolean True to numeric data types conversion**************")
print(int(True))
print(float(True))
print(complex(True))
print(str(True))
print("*********boolean True to numeric data types conversion**************")
print(int(False))
print(float(False))
print(complex(False))
print(str(False))


# any datatype with some value returns True if converted to bool
print("************************************")
print(bool(0))
print(bool(783216))
print(bool(-21))
print(bool(89.72167))
print(bool(-12.2))
print(bool()) # bool with nothing returns False


print("*************************************************************")
print('*****Boolean on list,tuple,dict,set,frozenset')

print("**list**")
print(bool([]) == False)
print(bool(list()) == False)
print([0][0] == False) # A list with 0 as its only element

print("**tuple**")
print(bool(()) == False)
print(bool(tuple()) == False)
print((0,)[0] == False)

print("**dict**")
print(bool({}) == False)
print(bool(dict()) == False)
print(list({'one':None,'two':2}.values())[0] == None) # None is used to indicate that the variable will be edited with
                                                      # a new value in future.

print("**set**")
print(bool(set()) == False)
print(bool(set({})) == False)


print("**frozenset**")
print(bool(frozenset()) == False)
print(bool(frozenset({})) == False)

print("*******************************************************************************")
print("****************all() and any() methods************************")
# any() takes exactly 1 iterable as input and checks that iterable has atleast 1 item that evaluates to True.
print(any([2,3,4,5]))
print(any([])) # empty iterable list
print(any([1,0,0,0,0,False,0.0]))
print(any((12,)))
print(any(())) # empty iterable tuple
print(any({})) # empty iterable dictionary
print(any(set())) # empty iterable set
print(any(frozenset())) # empty iterable frozenset
print(any('yokesh')) # string is also iterable
print(any('')) # empty string


# a11() takes exactly 1 iterable as input and checks the all iterable items evaluates to True.
print(all([2,3,4,5]))
print(all([])) # empty iterable list
print(all([1,0,0,0,0,False,0.0]))
print(all((12,)))
print(all(())) # empty iterable tuple
print(all({})) # empty iterable dictionary
print(all(set())) # empty iterable set
print(all(frozenset())) # empty iterable frozenset
print(all('yokesh')) # string is also iterable
print(all('')) # empty string

'''
     case:                                          any()                   all()
    --------                                       ----------               ----------
     All true values                                 True                     True
     All false values                                False                    False
     One item is true, other items are false         True                     False
     One item is false, other items are true         True                     False
     Empty iterable with no items                    False                    True
'''
