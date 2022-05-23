'''
for,while
1) looping can be used on iterables.
2) Iterables are those that can be iter upon, like lists,strings,tuples,dictionaries,sets,frozensets etc..
'''

l1 = [1,2,3,4,5,6]

print("printing list using its length in range : ")
for x in range(len(l1)):
    print(x,end=" ")

# or we can directly iterate list as,
print("\n")

print("printing list items using initialized variable of list : ")
for var in l1:
    print(var,end=" ")

print("\n")

print("printing items of a list directly using loop : ")
for item in [2,4,6,8]:
    print(item,end=" ")

print("\n")

# Similarly, We can use tuples,sets in place of list in above examples.

my_dict = {"one":1,'two':2,"three":3}

print("Printing dict() keys : ")
for x in my_dict:    # we can use my_dict.keys() also
    print(x,end=" ")

print("\n")

print("Printing dict() values : ")
for x in my_dict.values():
    print(x, end=" ")

print("\n")

print("printing dict() items : ")
for x,y in my_dict.items():
    print(x,y,end=" ")

print("\n")

my_frozen_set = frozenset([1,2,3,4,5])

print("printing frozen set items : ")
for x in my_frozen_set:
    print(x, end=" ")

print("\n")

print("printing strings : ")
for x in "yokesh":
    print(x,end="")

print("\n")
for y in "God knows who is best!":
    print(y,end="")

print("\n")
# Using Underscore for looping,
print("Using Underscore _ for looping : ")

# We are using one local temporary variable 'x' in all above loops, instead we can use underscore '_' .

print("Printing strings using underscore")
for _ in "hello how are you":
    print(_,end="")

print("\n")

print("Printing dictionary using underscore")
for _,y in {"coke":3,"water":5,"sandwich":2}.items():
    print(_,y,end=" ")

print("\n")

print("Printing list using underscore")
for _ in ['a','b','c','d','e']:
    print(_,end=" ")

print("\n")


print("**************************************************************************************")
print("******while loops******")
i = 3
while i < 5:
    print("We are inside while loop!..")
    i = i+1

j = 5

while j < 10:
    if ( j == 8):
        break
    print("The current value of j is : ", j)
    j = j+1

print("************")
'''
Initially j was 5, everytime console enters while loop, python checks whether the state of j which was 5-
- is equal to 8 or not, if j == 8 then console comes out of the while loop.else it prints the current-
- j value.
'''


for entry in [1,2,3,4,5]:

    if entry == 3:
        continue

    print(entry,end=" ")

'''
We can skip one entry using continue, as soon as 'entry' value becomes 3 at index 2 ,we can skip that entry and -
- console goes to next item in the list i.e, index 3 . 
'''

print("************************************************************************")






