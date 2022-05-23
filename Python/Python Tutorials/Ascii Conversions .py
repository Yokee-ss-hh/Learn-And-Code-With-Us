# bin() , oct() and hex() builtin functions.
print(bin(10))
print(oct(10))
print(hex(10))

print(bin(21).strip('0b')) # To remove 0b at front .

print("*********************************************************************************")
# ord() and chr() functions.

# ord() : This function returns the Unicode code from a given character.
# This function accepts a string of unit length as an argument and returns-
# -the Unicode equivalence of the passed argument.

print(ord('B'))
print(ord("B"))

print(ord('f'))

print(ord('$'))
print(ord('ć'))
print(ord('ç'))
print("*************")

for word in "Yokesh":
    print(ord(word),end="\n")
print("**************************************************")

# chr() : Python chr() function takes integer argument and return the string representing-
#         -a character at that code point.
# The valid range for the argument is from 0 through 1,114,111.
# ValueError will be raised if the input integer is outside that range.

print(chr(41))
print(chr(123))

try:
    print(chr(-19))
except ValueError:
    print("Value error occured! OOPS")

# Convert ASCII Unicode Character 'A' to 65
y = ord('A')
print(type(y), y)

large_alphabet_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small_alphabet_list = 'abcdefghijklmnopqrstuvwxyz'
# Prints 65-90
for i in large_alphabet_list:
    print(ord(i), end=" , ")
print("\n")
print("**********")
# Prints 97-122
for j in small_alphabet_list:
    print(ord(j), end = " , ")

print("***************************************************")
