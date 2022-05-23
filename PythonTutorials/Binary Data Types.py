'''
1) The byte and bytearrays are used to manipulate binary data in python.
2) These bytes and bytearrys are supported by buffer protocol, named memoryview.
3) The memoryview can access the memory of other binary object without copying the actual data.
4) bytes -> immutable , bytearray -> mutable.
5) string methods works on both bytes() and bytearray()
6) From python docs, The core built-in types for manipulating binary data are bytes and bytearray-
-they are supported by memoryview() which uses the buffer protocol to access the memory of other binary objects-
-without needing to make a copy.
'''
print("***************************** bytes() *********************************")
# We can create bytes literal using single,double quotes and 3 single or 3 double quotes.

# Single quotes: b'still allows embedded "double" quotes'

# Double quotes: b"still allows embedded 'single' quotes"

# Triple quoted: b'''3 single quotes''', b"""3 double quotes"""

# Bytes objects are immutable sequences of single bytes.

# A zero-filled bytes object of a specified length: bytes(x), 0 <= x < 256

# From an iterable of integers: bytes(range(20))

# Copying existing binary data via the buffer protocol: bytes(obj)

a = b'hello bro'

b = b'''How are you'''

print(type(a), type(b))

byte_variable_from_string = bytes('Nice', encoding = 'utf8')

print(type(byte_variable_from_string))

byte_from_integer = bytes(10) # Look at line 17,
print(byte_from_integer)

# byte_from_float = bytes(22.321)
# print(byte_from_float)
# Gives Error as floating objects cannot convert to bytes objects.

byte_from_iterables = bytes([1,2,3,4,5,6])
print(byte_from_iterables)

# byte_variable.hex(byte_per_sep)
print(byte_variable_from_string.hex()) # converting bytes to hexa-decimal. (b'hello bro' -> '4e696365')
value = b'\xf0\xf1\xf2'
print(value.hex())
print(value.hex('@'))
print(value.hex('#',2))
print(value.hex('#',4))
print(value.hex('%',-2))
print(value.hex('%',-4))
# The first parameter, acts as seperator between each character in the output-
# -by default b/w each character of hex.
# The second parameter if +ve , seperation is done from right to the output.
# The second paramter if -ve, seperation is done from left to the output.
print(bytes.fromhex('4e696365')) # converting hexa-decimal to original bytes string. ('4e696365' -> b'hello bro')

# All methods working on strings, will work on bytes data type.

print(b'hello'.replace(b'l',b'g'))
print(b'hey bro how are you huggs'.count(b'h'))

print("*************************** bytearray() **********************************")
# bytearray objects are a mutable counterpart to bytes objects.

# There is no dedicated literal syntax for bytearray objects,
# instead they are always created by calling the constructor:
#
# Creating an empty instance: bytearray()
#
# Creating a zero-filled instance with a given length: bytearray(10)
#
# From an iterable of integers: bytearray(range(20))
#
# Copying existing binary data via the buffer protocol: bytearray(b'Hi!')

x =  bytearray(10) # return all 0's in hexa format
print(x)
y = bytearray('yokesh',encoding = 'utf8')
print(y)
z = bytearray([1,2,3,4,5,6]) # iterable of integers in the range 0 to 256.
print(z)

print(y.hex())
print(bytearray.fromhex('796f6b657368'))
# All methods of strings will work on bytearray objects also.

print(y.replace(b'y',b'l'))
print(bytearray(b'apples contains apple which is from amber').count(b'a'))

print('****** Differences Between bytes() and bytearray() ******')

# 1) bytes() are immutable, bytearray() is mutable.
# 2) All string methods will work on bytes() and bytearray().
# 3) Changing contents of byte() object creates new object in the memory as immutable string does.
# 4) Changing contents of bytearray() object will reflect on that object itself same as mutable list.

immutable_byte_object = bytes('Hello There',encoding = 'utf8')
print(immutable_byte_object, id(immutable_byte_object))

immutable_byte_object = immutable_byte_object + b'how are you'
print(immutable_byte_object, id(immutable_byte_object))

# See from the output that original object has 1 memory address and modified object entirely-
# - created a new object in the memory
# The object in line 89 will be cleaned by garbage collector as it has no references.

mutable_byte_array_object = bytearray('Python Is Good', encoding = 'utf8')
print(mutable_byte_array_object, id(mutable_byte_array_object))

mutable_byte_array_object[0:6] = bytearray('Yokesh',encoding = 'utf8')

print(mutable_byte_array_object, id(mutable_byte_array_object))

# As, bytearray() is mutable, we can use item assignment via slicing . If we do the same with immutable bytes(),
# We will get error as immutable bytes() does not support item assignment.


print("************************ Memoryview() *********************************")

'''
memoryview objects allow Python code to access the internal data of an object that-
-supports the buffer protocol without copying. 
The memoryview() function allows direct read and write access to an object’s byte-oriented-
-data without needing to copy it first. 
That can yield large performance gains when operating on large objects since it doesn’t create a copy when slicing.
'''

'''
Buffer protocol provides a way to access the internal data of an object.
This internal data is a memory array or a buffer. 
It allows one object to expose its internal data (buffers) and the other to access those buffers-
-without intermediate copying.
Buffer protocol is only accessible to us at the C-API level and not using our normal codebase.
So, to expose the same protocol to a normal Python codebase, memory views are present.
'''

print("***memoryview() on bytes***")

place = bytes("london",encoding="utf8")
print(type(place))

print("Hexa conversion of place variable gives :",place.hex()) # 6c6f6e646f6e
print("Converting one bit of hexa value to ascii gives :",0x6c) # 108
print("Converting that ascii to character gives :",chr(108)) # 'l'

mv_place = memoryview(place)
print("Memory view of place variable gives :",mv_place) # <memory at 0x000001FDCFC9DA80>

print("The actual object memory view mv_place is holding is :",mv_place.obj)
print("The size of the object that memory view mv_place holding is :",mv_place.nbytes)
print("Each character memory view mv_place holding has a size of :",mv_place.itemsize)
# In the above output, byte size of each character in place variable is of 1 byte memory size.
# i.e, l,o,n,d,o,n has 1 byte size.

print("Converting memory view to lost gives ascii values of characters",mv_place.tolist())
# output :  [108, 111, 110, 100, 111, 110]

for x in mv_place.tolist():
    print(chr(x),end="")     # london

print('\n')

# slice operator on memory view returns the contents storing in that memory in the form of a list.
print("we can get first character of the original variable using slicing: ",mv_place[0])
# The above line returns first byte ascii value , i.e, ascii value of 'l' in london is 108
print("Second character of the variable we used memoryview() upon :",mv_place[1])

print("Memory addresses of n to o",mv_place[2:5])
# returns address where the characters from 'n' to 'o' stores in b'london'

print(mv_place[2:5].tobytes()) # b'ndo'


print("***memoryview() on bytearray***")

a = bytearray(b'abcdef')
print("Hexa of a :",a.hex()) # o/p : 616263646566
print(0x61) # taking one byte from above output : 97
print(chr(97))

v = memoryview(a)
print("Memory view of variable a :",v)
print("The actual object memory view v is holding is :",v.obj)
print("The size of the object that memory view v holding is :",v.nbytes)
print("Each character memory view v holding has a size of :",v.itemsize)
# In the above output, byte size of each character in place variable is of 1 byte memory size.
# i.e, a,b,c,d,e,f has 1 byte size

print("byte array Variable a :",a)
print("Memory view of bytearray a :",v)
print("memory view of a to bytes :",v.tobytes())
print("memory view of a to list :",v.tolist())
print("Ascii characters of a variable in list:",)
print("variable a characters in the range from 2 to 5 :",v[2:5].tobytes())

# As, bytearray is mutable we can change contents in it.as,
# let's change the contents of variable a , We can see that memory view
# - address also changes.

a[3] = 99

print("bytearray a after modification",a)
print("memory view v after adding new character to bytearray a",v[2:5].tobytes())
# In the above line,Memory view also updated with new value






