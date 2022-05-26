print("*****************************************************************")
print("*** seek,seekable,tell,truncate")

'''
1) Make sure Files Texts5.txt has the contents that is in the lines 36 and 37.
2) If not, erase the contents in the file, and re upload the content from line 36 and 37.
'''

obj = open("Files Texts5.txt",'r')

# seekable returns True if the file can use seek() method or not.
print(obj.seekable())

# Initially, file pointer starts from the 1st character in the file.
#  seek() function is used to change the position of the file pointer to a given specific position.
#  which defines from where the data has to be read or written in the file.

obj.seek(10) # means we can access file contents from the 11th character onwards.

print(obj.read(10))

# tell() returns where the file pointer currently exists,let's see where file pointer is:
# tell() calculates the no of chars from the beginning of the file until the file pointer.

print(obj.tell())
obj.close()
# until 19 chars read() method has accessed, so tell() method-
# -returns 20


# The truncate() method resizes the file to the given number of bytes.
# If the size is not specified, the current position will be used.
# Go to file manager,click on properties of the file 'Files Texts5.txt'
# Initially, Files Texts5.txt has content as,
'''
In Kali-yuga, wealth alone will be considered the sign of a man’s good birth, proper behavior and fine qualities.
And law and justice will be applied only on the basis of one’s power.
'''
obj = open('Files Texts5.txt','a')

obj.truncate(100)

obj.close()


obj = open("Files Texts5.txt",'r')

print(obj.read())

# After truncate file content is :
'''
In Kali-yuga, wealth alone will be considered the sign of a man’s good birth, proper behavior and 
'''


