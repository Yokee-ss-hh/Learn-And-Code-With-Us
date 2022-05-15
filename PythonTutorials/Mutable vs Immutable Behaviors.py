# Discuss why immutable objects even undergo copying points to original memory address!

print("***************IMMUTABLE*****************")
'''
strings,tuples,frozensets,integers,floating integers..
'''
print("In maximum cases, copying original immutable object won't create a new object in the memory, but"
      "it makes the copied variable to point the original immutable object, In case of strings"
      "un-modified strings even after copying points to original string.")
# Why immutable objects don't need copying ?

print("Changing contents of Immutable objects after their creation is not possible, even if we try to change "
      "the contents python will create a new object in the memory, the best example for these is"
      "string methods. So, Basically there is no need to create 2 memories for the same content objects")

print("Strings and integers goes under interning! that makes strong memory optimization")

print("Tuples and frozensets behaves the same way as strings like copied objects will points to the same"
      "original objects memory address")
'''
1) strings don't have copy() method to copy a string, all they have is to use various techniques
- like i specified in (string copying techniques) file.
2) tuples don't have any builtin methods to copy a tuple, so basically we don't have any way to copy a tuple.
3) frozen sets has copy() method, but copied method points to original frozenset.
4) integers even copied and due to interning points to original integer.
'''

print("****************MUTABLE********************")
'''
lists,dictionaries,sets...
'''
print("Copying mutable data types allocates new memory for copied object,All 3 mutable data types "
      "have copy() methods to copy the original object.")

print("Existing items of list,dict can be modified but existing items of set cannot be modified"
      "We can add new items to list,dict,set using builtin methods.")

