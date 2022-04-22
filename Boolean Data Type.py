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

