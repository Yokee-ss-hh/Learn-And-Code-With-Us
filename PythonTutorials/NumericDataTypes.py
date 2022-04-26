# Numeric Data Types(int , float , complex)

a = 2 
b = -23
c = 24143412
d = -4143.123
e = 2.21
f = 3 + 4j
g = -2.3 + 6j
h = -543j


# Type Checking Using type() method,
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))

print("*************************************************************************")

# Checking a variable is of it's type or not using isinstance() method,
print(isinstance(a,int))
print(isinstance(b,int))

print(isinstance(d,float))
print(isinstance(e,float))

print(isinstance(f,complex))
print(isinstance(h,complex))

print("**************")
print(type(a) is int)
print(type(c) is int)
print(type(e) is float)
print(type(f) is complex)
print("*************************************************************************")

# Implicit Type Conversions
# Python interpreter implicitly converts it.....
'''
  int + int = int
  int + float = float
  float + float = float
  float + complex = complex
  complex + float = complex
'''
print(type(23+2.321))
print(type(-3.321+76))
print(type(3+7j+2.2))
print(type(-7j+21))

print("*************************************************************************")

# Explicit Type Conversions
# Programmer convert it using constructors of its respective datatype [int() , float() and complex()]
print(int())
print(int(4.21))
print(float())
print(float(21))
# print(int(2+9j)) , cannot convert complex to any datatype
# print(float(-23+89j)) , cannot convert complex to any datatype
print(complex())
print(complex(33))
print(complex(-3.333221))
print(complex(4+4j))

print("*************************************************************************")


# While using base keyword in an int() / float() , remember to use first argument as a string only 
# int() wont accept nan/NaN , InF/inf and InFiNiTy/infinity
print(int('10',base=2))
print(int('7',base=8))
print(int('f',base=16))
print(int('10',base=10))
print(int('0b10',base=2))
print(int('0B10',base=2))
print(int('0o7',base=8))
print(int('0O7',base=8))
print(int('0xf',base=16))
print(int('0Xf',base=16))

print("*************************************************************************")


# float() accepts nan/NaN , InF/inf and InFiNiTy/infinity , removes trailing and leading white space characters, and does not accepts character strings 
print(float('nan'))
print(float("NaN"))
print(float("inf"))
print(float("InF"))
print(float("infinity"))
print(float("InFiNiTy"))
# only accepts decimal point strings other tham nan,NaN,inf,InF.infinity,InFiNiTy
# print(float("hello")) gives error
print(float('2.321'))
print(float(21))
print(float(    -9    ))
print(float('   4.43\n'))
# float() doesn't accept base keyword as a second argument/ float() dont have keyword arguments
# print(float('f',base=8)) gives error

print("*************************************************************************")

print(complex())
print(complex(2,2))
print(complex(66))
print(complex(0,12))
print(complex(11,0))

# string as parameter
print(complex('2.23+9j'))
# print(complex("2.23 + 9j")) gives value error as complex() arg is a malformed string
# shouldn't give 2 strings as a complex() parmeters
# print(complex("11","7.65")) gives TypeError as complex() cant take second arg is first arg is a string
# print(complex(10111,base=2)) gives error as there is no base as a argument for complex()

# Operators in python 
print("************Arithmetic Operators*****************")
'''
    + , - , * , / , // , % , **
'''
# Addition and Subtraction
print(10+2.32)
print(-21.12121+12)
print(3+8j-7.77)
print("**************************************")

# Multiplication
print(2*21)
print(2*-12)
print((4+5j)*10)
print(5.55*2)
print("**********************************")

# Division
print(21/3)
print(15/4)
print(20/3)
print(-12/5)
print(12/-5)
print(-13/-4)
print(0/21) # gives float as output
print(-0/12)
print("***********************************")

# Floor Division
print(21//3)
print(15//4)
print(20//3)
print(-12//5)
print(12//-5)
print(-13//-4)
print(0//21)
print(-0//12)
print("***********************************")

# Modulo Operator
'''
Formula : mod(a,n) = a - {n * Floor(a/n)}
'''
print(21%3)
print(15%4)
print(20%3)
print(-12%5)
print(12%-5)
print(-13%-4)
print(0%21)
print(-0%12)
print("*************************************")

# Exponentation Operator
print(2**4)
print(5**2)
# can use e in place of power of 10 as ,
print(2e5) 
# 2e5 means 2*(10**5), and returns floating output
print(2*(10**5))
'''
Note : while using e it gives float , while using ** it gives int output
       python interpreter wont recognize if we write print(e4), so write print(1e4)
'''
# print(e6) gives error
print(1e6)

print("******************Comparsion Operators*******************")
# comparsion operators returns True/False only
'''
    > , >= , < , <= , == , !=
'''
print(2>1.99999)
if 3>=3:
  print("WoW")
  
print(-2 < -1)
print(-5 <= -3)

#  '==' operator checks whether the value stored in left and right operands are same or not
num1 = 21
num2 = 21
print(num1 == num2)
print(num1 != num2)


print("*****************Logical Operators*********************")
'''
    and , or , not
'''
if 2%2 == 0 and 9%3==0:
  print("Perfect")
  
if 2>3 or 2<3:
  print("Ok")
  
if not(False):
  print("Woaaahhh")
  
  
print("*************************Identity Operators************************")
'''
   is , is not
'''
# 'is' checks whether both left and right operands points to the same object or not , if same 
# it returns True , else it returns False

number_one = 21
print(type(number_one) is int)
print(type(number_one) is not float)

print("**********************Membership operators************************")
'''
in , not in 
'''
# returns True when left operand value present in right operand value , else it returns False.
print('x' in "xmas")
print('yokesh' in ['yok','yoki','yokee','yokesh'])
print('ge' in "genre")
print('hay' in 'hello')

print("*********************Bitwise Operators**************************")
'''
    AND : & , OR : | , XOR : ^ , NOT : ~ , LEFT SHIFT : < , RIGHT SHIFT : >>
'''
print(0b0101 & 0b1010) # returns 1 only when both bits are 1 , else returns 0
print(0b0101 | 0b1010) # retuns 1 when either of bits are 1 else 0
print(0b1111 ^ 0b1010) # retuns 1 when either of bits are 1 , else 0
print(~0b1100) # returns 1's compliment of a number
print(0b1111 << 2)
print(0b1101 >> 2)

'''
Tricks:   a<<b = a*(2**b)
          a<<b = a//(2**b)
          ~a = -(a+1)
'''
print("******************Assignment Operator**************************")
my_var = 33
# The above line means 33 is stored in the memory with the name my_var 
# We can use comparsion and bitwise operators with assignment operator as,
apple = 12
print(apple) # 12
apple +=12   # means apple = apple+12
print(apple) # 24
apple-=10    # means apple = apple-10
print(apple) # 14
apple*=2     # means apple = apple*2
print(apple) # 28
apple/=2     # means apple = apple/2
print(apple) # 14.0
apple//=2    # means apple = apple//2
print(apple) # 7.0
apple%=2     # means apple = apple%2
print(apple) # 1.0

banana = 3 
banana**=3   # banana = banana**3
print(banana)# 27


cherry = 2
berry = 4
cherry&=2 # cherry = cherry&2 
print(cherry)
berry|=2  # berry = berry|2
print(berry)

# We cannot use ~ operator with = operator as , some_var~=2
orange = 6
orange^=6
print(orange)

papaya = 4
papaya>>=2
print(papaya)

kiwi = 2
kiwi<<=2
print(kiwi)

print("*******************Operator Precendence and Associtivity***************************")
# Precendence decreases from top to bottom
'''
1) ()                brackets (L-R)
2) **                exponentation (R-L)
3) ~                 bitwise Not (L-R)
4) *,/,//,%          mul, div, floor div ,modulo (L-R)
5) +,-               add, sub  (L-R)    
6) <<, >>            bitwise left, bitwise right (L-R)
7) &                 bitwise and  (L-R)
8) ^                 bitwise xor (L-R)
9) |                 bitwise or (L-R)
10) >, <, >=, <=, ==, !=  comparsion operators (L-R)
11) =, +=, -=             assignment operators (R-L)
12) is, is not            identity   operators (L-R)
13) in, not in            membership operators (L-R)
14) and, or, not          logical    opeartors (L-R) 
'''

