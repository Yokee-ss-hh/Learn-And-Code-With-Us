'''
As we know, after writing the data to files,
first it goes in internal buffer then after closing the files data goes into disk.
what if the data still in buffer and power cut off? so flush() method forcefully send the data to disc.
'''
'''
1) Make sure that Files Texts6.txt is empty while running this file.
2) So that you can observe the output.
'''
# opening file
fileObject = open("Files Texts6.txt", "w+")

# writing into the file
fileObject.write("I Love Python")

# closing the file (clear the buffer)
fileObject.close()

# opening the file to read its content
fileObject = open("Files Texts6.txt", "r")

# reading the contents before flush()
fileContent = fileObject.read()

# displaying the contents
print("\nBefore flush():\n", fileContent)

# clearing the input buffer
fileObject.flush()

# reading the contents after flush()
# reads nothing as the internal buffer is cleared
fileContent = fileObject.read()

# displaying the contents
print("\nAfter flush():\n", fileContent)

# closing the file
fileObject.close()

