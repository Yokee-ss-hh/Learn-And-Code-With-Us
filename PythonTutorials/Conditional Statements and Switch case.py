print("***********************if,elif,else**************************")
'''
if <condition = True/False>:
    ...statements...
elif <condition>:
    ...statements...
else:
    ...statements...
'''

if True:
    print("EX1 : This is printed")

if True == 1 == 1.0:
    print('EX2 : Chaining is done here!')

if '':
    print("Nothing is printed")  # empty string returns False

if any([1,2,3]):
    print("EX3 : Holaaa!..")

if all([False,False]):
    print("He hehehe")
print('EX4 : Ok bro')


if age:=18 > 15:
    print("age is greater than 15")
elif age == 18:
    print("eligible to vote")
else:
    print("This is else statement of age condition")

# If any of if,elif,else has one statement , we can write them in one line as,

if "yokesh".upper() == "YOKESH": print("yokesh changed to YOKESH") # one liner if condition

if bin(2) == '0b110': pass
elif bin(2) == '0b10' : print("Binary format of 2 is : ",bin(2))

if 2>3 : pass
elif 3>4 : pass
else: print("Else is printed in one liner statement")

print("*************Switch Cases/ match cases*****************")

match http_code:=int(input("enter status code : ")):

      case 400:
          print("Bad Request")
      case 401:
          print("Un authorized Request")
      case _:
          print("Oh dear, nothing is matched")




