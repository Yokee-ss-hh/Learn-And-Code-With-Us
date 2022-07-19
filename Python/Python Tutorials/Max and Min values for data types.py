print("*****************************************************")
import sys

# Int maximum and minimum values

print(f"Max size of int : {sys.maxsize}")

print(type(sys.maxsize))

print(sys.maxsize == (2**63)-1)

print(f"Min size of int : {-sys.maxsize}")

print(type(sys.maxsize))

print(-sys.maxsize == -((2**63)-1))

print("*****************************************************")
# Float maximum and minimum

print(f"Max size of flaot : {sys.float_info.max}")

print(type(sys.float_info.max))

print(f"Min size of flaot : {sys.float_info.min}")

print(type(sys.float_info.min))

print("*****************************************************")
# For Infinity maximum and minimum values we can use 'inf'

some_maximum = float('inf')
print(type(some_maximum))
print(some_maximum)


some_minimum = float('-inf')
print(type(some_minimum))
print(some_minimum)

print("*****************************************************")

print(float('inf') > 21)

print(float('-inf') > 21)











