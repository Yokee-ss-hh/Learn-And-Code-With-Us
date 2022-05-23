import string

# In string module , we have
'''
9 constants
2 classes
1 method
'''
print(dir(string)) # This gives all methods and constants that are pre-defined in string module.
print("******************************************************************")
# 1) Template() class using along with substitute().
templated_method = string.Template("This is $original string")
final_string = templated_method.substitute(original = "final")
print(final_string)

# We can write in single line without using all the temporary variables as,
print(string.Template("There is a $large $dang named $Desi Programmers").substitute(large="small",dang="gang",Desi="Urban"))

# Note : The number of $'s should be equal to number of parametres in the substitute method.
print("*********************************************************************")
# If the number of $'s is not equal to number of parametres in the substitute method, use safe_substitute().
print(string.Template("He works $at $Noogle").safe_substitute(Noogle="Google").replace('$',""))

print("****************************************************************************")
# Formatter() class
'''
Python’s built-in str class has format() method using which string can be formatted. 
Formatter object behaves similarly. 
This may be useful to write customized formatter class by subclassing this Formatter class.
'''
f = string.Formatter()
print(f.format("name : {name}, age : {age}",name="yokesh",age=22))
# The above line behaves similar to format() string method , Lets see
print("name : {name}, age : {age}".format(name="yokesh",age=22))
# Look at the above 2 outputs , we got the same...

# syntax : get_value(our_key , args, kwargs)
print(f.get_value(3,"yokesh",{"age":22}))
print(f.get_value("place","yokesh",{"age":22,"name":"YokiYokee","place":"india"}))
# In the above 2 lines , we used get_value() method .
# If our_key is int , then it returns the key th index of the parameter 2
# If our_key is string , then parameter 3 should be dictionary and it returns the value of parameter3 th key.
print("************************************************************************")
# string module constants
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.punctuation)
print(string.printable)
# print(string.whitespace) o/p : ' \t\n\r\x0b\x0c'

print("***************************************************************************")
'''
capwords() Method : Splits the given string argument into words using str.split().
                    Capitalizes each word using str.capitalize()
                    and joins the capitalized words using str.join().
'''
my_str = "All are very good, some are too good"
print(string.capwords(my_str))

print("****************************************************************************")