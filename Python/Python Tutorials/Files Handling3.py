'''
In this File We are learning,

1) using with keyword to open a file.
2) using for loop to print data from a file
'''

with open('Files Texts7.txt','r',encoding='utf8') as z:
     count = 0
     for line in z :
          print(line)
          count+=1
     z.close()
     print("Total number of lines is :",count)


# for loop considers one line for each iteration, so if there are 5 lines in a file,
# then 5 lines are printed in the same format which is in the input file.


