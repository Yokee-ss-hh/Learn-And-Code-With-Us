print("**************************************************")
# We can literally add boolean and int data types, that means True acts as 1 , and False acts as 0

a = True
b = 0

print(type(a))
print(type(b))

print(a+b)
print(b < a)
print(False+True)

print(True in [1])
print(1 < True)
print(1 < 0 < 1)  # should evaluate as 1<0 and 0<1 =>False and True => False, This is expression chaining

print("****************************************************")
x = True
y = False
print(not x == y)
# print(x == not y)

print("*********************************************************")

print('*****int,float and complex behavior*****')
# floating variables with nothing except 0's after floating point is always equal to its integer equivalent.
# objects with same value is equal even they are of different type,That's why == returns True and is returns False.
int1 = 22
float1 = 22.0
float2 = 22.00000000
complex1 = 22+0j
complex2 = 22+0.00000j

print('**==**')
print(int1 == float1)
print(float1 == float2)
print(float2 == int1)
print(float2 == complex1)
print(complex1 == complex2)
print(complex2 == int1)
print('\n')
print('**is**')
print(int1 is float1)
print(float1 is float2)
print(float2 is int1)
print(float2 is complex1)
print(complex1 is complex2)
print(complex2 is int1)


# How this works?
'''
1 == 1.0 == 1.000.... == True

In 1.0, after floating point there is no precision so interpreter simply ignores the 0/0's after the floating point.
We already proved on the top of the file that 1 == True and 0 == False.
'''
print("********Some Good Examples**********")
print(0 == 0.00000000000000)
print(0 == 0+0j)
print(2.22 == 2.22+0j)
print(True == 1+0j)
print(0 == False)
print(0.000 == False)
print(2.000 == (True+1))
print(0+0j == (1-True))
print((True+False) == (1.0000+0))
print((not False) == 1+0j)
print(3 == ((not 0.0000) + (1+0j) + (not False)))



