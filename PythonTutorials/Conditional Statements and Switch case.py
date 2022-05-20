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

    
# Implemented in python recent versions...
print("*************Switch Cases/ match cases*****************")

match http_code:=int(input("enter status code : ")):

      case 400:
          print("Bad Request")
      case 401:
          print("Un authorized Request")
      case _:
          print("Oh dear, nothing is matched")


print('********** one liners if/elif/else ***************')

# if-else one liner
print(20  if 20 % 2 == 0 else '20 is not divisible by 2')

minimum_age = int(input('Enter your age bro!'))

# if-elif-else one liner
print('accepted' if minimum_age > 20 else 'its ok' if minimum_age == 18 else 'not accepted bro!')

# NOTE : We cannot write only if condition without any elif/else in lone liners.
# Python raises error to write else statement if we do so.

