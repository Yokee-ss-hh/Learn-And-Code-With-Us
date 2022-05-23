'''
There are 3 sequence data types in python
1) list
2) tuple
3) range
'''

# Range(start,stop,step) is one of the sequence data type in python
print(type(range(0)))

for x in range(5):            # By default range(5) = range(0,5,1)
    print(x, end="")
print("\n")
for y in range(2,7):           # By default range(2,7) = range(2,7,1)
    print(y, end="")
print("\n")
for z in range(1,9,2):
    print(z,end="")
print("\n")
for a in range(-8,-4,1):
    print(a,end="")
print("\n")
for b in range(-1,-8,-1):
    print(b,end="")
print("\n")
# range(x) -> x : stop by default
# range(x,y) -> x : start, y : stop
# range(x,y,z) -> x : start, y : stop, z : step

# In the range() method we need to give either +ve or -ve numbers only.
# We should not give string or floating values as arguments to range() method.If we do so we will get TypeError.
# We should not give 0 as step to range(), If we do so we will get ValueError.

try:
 for g in range(0,5,0):
    print(g,end="")
except ValueError as e:
    print(e)
print("\n")

try:
    for h in range('yokesh'):
        print(h,end="")
except TypeError as e:
    print(e)
print("\n")

try:
    for i in range(4.321):
        print(i,end="")
except TypeError as e :
    print(e)\

