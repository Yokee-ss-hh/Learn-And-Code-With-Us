'''
1) Sets are mutable data types.
2) Set items are unordered,unindexed,unchangeable,immutable and doesn't allow duplicates.
3) sets wont go under interning.
'''

print("2 or more sets with same items")
s1 = {1,2,3,4,5,6}
s2 = {1,2,3,4,5,6}

print(s1 == s2)
print(f"Id of s1 is {id(s1)} Id of s2 is {id(s2)}")
print(s1 is s2)

# same like lists, dictionaries sets follow the similar memory handling.

print("Two or more sets with same items will always stores at different locations")

print("How 2 empty sets handles memory?")

s3 = set()
s4 = set()
print(s3 == s4)
print(f"Id of s3 is {id(s3)} Id of s4 is {id(s4)}")

print("Even 2 empty sets stores at 2 different memory locations")

print("From the lines 304 to 330, we saw that even copying a sets to form a new sets,the new sets "
      "will have different memory addresses")


