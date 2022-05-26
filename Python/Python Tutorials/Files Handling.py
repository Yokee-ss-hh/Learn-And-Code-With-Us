'''
1) Open a file
2) Read/Write Operation
3) Close the file
'''
'''
1) While running this file, Make sure that
2) Files Texts3 and Files Texts4 is not exist at all.
3) If these exists first delete those and run this file.
'''
# Syntax : f = open(file_name,mode)

'''
Modes : 
1) r - read mode, opens a existing file to read .This mode is default.Raises error if the
       specified file is not exist.
2) w - write mode, opens a file for writing, creates a new file if specified is not exist,
       if specified file exists, it overwrites it's contents.
3) a - append mode, opens a file to add some more content, if specified file is not exist,
       it creates a new file.
4) x - create mode, creates the specified file, if that file already exists , it raises error.
'''

# There are 3 ways to create a new file using file modes(w,a,x modes).

'''
Additional Modes :
1) t - text mode, This is the default mode for every file
2) b - binary mode, (ex : images,jpg,jpeg,png formats)
'''


'''
Hybrid Modes : 
1) rb - read mode of binary file for reading
2) r+ - opens a file to read and write 
3) rb+ - read,write mode of binary file
4) wb - write mode of binary file
5) w+ - write and read mode
6) wb+ - write,read mode of binary file
7) ab - opens binary type file to append some data
8) a+ - open a file to append some data and to read data
9) ab+ - opens binary type file to append and read data
'''


f = open('Files Texts.txt','r') # If file not exists , gives error
print(F"The Mode of the file opened is : {f.mode}")
print(F"The Name of the file opened is : {f.name}")

print("*****************************************************")
print("******* Read Mode *********")

# read() reads all the lines in specified file
# A line of gap is kept b/w the o/p lines, if reading of a whole line ends and starts-
# reading a new line in the input file.
# read() reads whole file in single go
# read(limit),readline(limit) reads upto the specified limit of chars
# readline() reads complete one single line
# readlines() reads complete file by creating a list of elements by taking 1 line per element
# readlines(limit) reads upto limit by taking a list of elements by taking 1 line per element upto
# - specified limit.
content1 = f.read(100)
print(F"The contents of the files are : {content1}")
content2 = f.read(10) # reads next 10 characters after the output in line 32
print(content2)
content3 = f.readline() # reads the entire line that is left over the output in line 37
print(content3)
content4 = f.readline(20) # Reads the line of 20 chars
print(content4)
content5 = f.readline() # Reads the rest of the line that was read by line 43
print(content5)
# readlines() gives a list with elements as each line of long strings from the output continued from line46.
# ['line1\n','line2\n','line3\n',..................'linen\n']
# readlines() takes no limit but readline() takes
content6 = f.readlines()
print(content6)

print(f.readable())

f.close()
print(f.closed) # if f file object is closed, then return True
print("************************************************************")
print("******** Write Mode **********")

g = open('Files Texts2.txt','w')  # Initially there is no file named Files Texts2.txt
# So python creates it, as we are in write mode.
# After running this, You can see a new file is created in the file explorer as Files Texts2.txt

print(g.writable())

print(g.name)

print(g.mode)

# NOTE : Do not open an existing file in write mode, If you open an existing file in write mode-
# - and use write() method to write some content into it. It overwrites the existing file content.
# SO, Beware of using file in write mode.

'''
writelines expects an iterable of strings (list of strings)
write expects a single string.
'''
# multiple write() methods will add strings in the same line only
# If we want strings to be added in seperate lines, use writelines() method
g.write("Hello Guys How Are You")
g.write("Is Everything Ok There")
g.write("I'm probably coming soon!..........")
g.close()
print(g.closed)

g = open("Files Texts2.txt",'r')
print(g.read())
g.close()

g = open("Files Texts2.txt",'w')
g.writelines(['So\n','Guys Be Happy In Your Life And Enjoy Well\n','\n','Do Not Forget To Work Hard\n','yokesh is one of the best owner and ceo in the world\n'])
g.close()

g = open('Files Texts2.txt','r')
print(g.read(10))
print(g.readline())
print(g.read(10))
print(g.readlines())

# content wrote in w mode using write() is replaced by content written in w mode using writelines()
# in the "Files Texts3.txt".That's why write mode is tough to use.

# BIG NOTE : After running this python file, You will get a new file named "Files Texts2.py" in the
# current directory.
# If you want to run again this.py file, delete that "Files Texts2.txt" and run, so that you can
# avoid overwriting the contents again and again.


print("**********************************************************")
print("******** Append Mode *********")

# append mode is used to add content to an existing file, if the file does not exist , it creates new file.

# Initially, there is no "Files Texts3.txt", so in append mode it newly creates it.
# So, there are no lines in it.

# If we open an existing file ,then append mode will append lines to the existing content of a file.

h = open("Files Texts3.txt","a")

print(h.mode)
print(h.name)

h.write("This content is written by yokesh in append mode")
h.close()

h = open("Files Texts3.txt",'r')
print(h.read())
h.close()

h = open("Files Texts3.txt",'a')
h.writelines(['\n','Do you know what is python\n','It is a programming langauge\n'])
h.close()

h = open("Files Texts3.txt",'r')
print(h.read())
h.close()
print(h.closed) # if h file object is closed, then return True
# NOTE : Make sure to delete the file 'Files Texts3.py' when we want to run again . Because it will-
# - add same content to existing content and we get duplicate content. so either erase the content-
# - or delete the whole file.

print("****************************************************************")
print("***** create mode *****")

k = open("Files Texts4.txt",'x')
# The above line creates a new file in the directory, If the file we specified is already exists,
# It will raise error.
# opening file in 'x' mode creates new file with empty content.

print(k.name)
print(k.mode)
print(k.close())
print(k.closed) # if k file object is closed, then return True
print("******************************************************************")
print("***** Delete a file *****")

'''
1) import OS Module
2) Check whether the file exist or not 
3) delete that file using remove() method
'''

# Let us delete the empty file that was created by 'x' mode in the line 152.
'''
if os.path.exists("Files Texts4.txt"):
  os.remove("Files Texts4.txt")
else:
  print("The file does not exist")
'''


