'''
Lists are mutable data types. Once lists are created we can change the contents again and again.
Lists are not Interned, that means 2 or more lists with the same content always have different-
-memory locations.
Lists containing interning supported data types such as strings and integers points to same addresses.
Deep copy of lists breaks the interning supported elements pointing to original lists.
'''

lisstt1 = ['yoki',123]
lisstt2 = ['yoki',123]
print(id(lisstt1))
print(id(lisstt2))
# From the output, we can see that even 2 lists with the same content will have different memory addresses.
# That means, every list will have different memory addresses and there is no memory optimization techniques like-
# -interning for lists.

print("****aliasing******")
l1 = [1,'a',2.32,'yokesh']
print(id(l1))

# aliasing makes another variable name pointing to original content of another variable.
# aliasing is done using assignment operator

l2 = l1
print(id(l2))

# l1---->[1,'a',2.32,'yokesh']<------l2

# Changing contents of l2 will reflect in l1 as lists are mutable.
l2.append("hello!")

print(f"l1 : {l1}, l2 : {l2}")

# With aliasing we saw that aliased copy is pointing to original list.
# How can we copy some list to different memory address ? Some techniques are there for this!
print("**list copying techniques**")
l3 = ['apple',12,3+9j]
l4 = list(l3)
print(id(l3), id(l4))
print(id(l3) == id(l4))
print(l3 == l4)
print("Copying a list using list() creates new list in the memory")
l44 = [*l3]
print(id(l3), id(l44))
print(l3 is l44)
print(l3 == l44)
print("copying a list into [] using unpacking operator creates new list in the memory  ")
'''
Note : Two Lists with same content in different order are not equal.
'''
l5 = [3+9j,'apple',12]
print(l3 == l5)
print("l3 == l5 returns False, as order of items matters in the List data type!")
print("**copy and deepcopy**")
l6 = ['prime',8.321]
l7 = l6.copy()
print(l6 == l7)
print(id(l6) , id(l7))

# using copy() method we can copy the original list and different location.
# changes made to copied list will not reflect in original list

l8 =[99+7.65j,'yokiyokeee']
l9 = l8.copy()
l9.append('ok')
print(f'l8 : {l8}')
print(f'l9 : {l9}')

print("Important topic")
'''
Two lists with same content and same order will store at different memory locations, but-
- if the elements inside those lists supports interning then those elements points-
-to same memory address.
'''

my_list1 = [1212,'yokesh']
my_list2 = [1212,'yokesh']
print(f"id of my_list1 : {id(my_list1)}")
print(f"id of my_list2 : {id(my_list2)}")

# But the id's of elements of these 2 lists have same memory addresses.
print(x1:=id(my_list1[0]), y1:=id(my_list2[0]), z1:=id(1212))
print(x1 == y1)
print(y1 == z1)
print(z1 == x1)

# Why this happens is 12 which is a integer supports interning concept for memory optimization.
# same happens with strings also, lets see,
print(x11:=id(my_list1[1]), y11:=id(my_list2[1]), z11:=id("yokesh"))
print(x11 == y11)
print(y11 == z11)
print(z11 == x11)


import copy

'''
Both copy and deepcopy works same on simple lists by just copying the contents of original list-
- and pasting in different memory locations.
copy.copy() is called shallow copy. 
A shallow copy creates a new object which stores the reference/aliases of the original elements.
So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects.
This means, a copy process does not recurse or create copies of nested objects itself.
copy.deepcopy() is called deep copy.
A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.
'''
print("References/aliasing on lists")
main_list = [1,2,34]
alias_list = main_list
alias_list[2] = 321
print(main_list)
print(alias_list)
# We saw that changes made to alias list reflected in main list.That's how aliasing works.
# aliasing makes references that points to same memory addresses.
# shallow copy uses aliasing while copying contents from original list, depending upon the mutable/immutable
# elements of the original list, changing copied list elements via shallow copy reflects in original list.
print("**shallow copy example**")
original_list = ['a',12,['b',143]]
copied_list1 = copy.copy(original_list)
print('ID of original list :',id(original_list))
print('ID of copied list using shallow copy :',id(copied_list1))

# The elements in the original_list are immutable string,immutable integer and mutable list.
# If i change the immutable elements in the original list using shallow copy,It won't reflect in copied list-
# -because modifying a immutable object is not possible and even if we modify the immutable object creates-
# - a new memory for that object and that reference to old memory address is breaked.

original_list[0] = 'A'
original_list[1] = 13

print(original_list)
print(copied_list1)

# If i modify the mutable element in the original list , it will create a impact on copied list as modifying the mutable
# element in the original list will not create a new object in the memory as mutable objects can be modified-
# -and copied list maintain reference to the old list.

original_list[2][0] = 'B'

print(original_list)
print(copied_list1)
# Look in the output , modifying mutable type element in original list also modifies the mutable element in -
# - copied list, because shallow copy maintain references or aliases of elements in  original list.
# As we know aliases of 2 lists will point of same memory address, so changing mutable data type in original-
# - list reflected in copied list.

print("**Deep copy example**")
# We can break down the aliases/references of mutable elements inside a list using copy.deepcopy() method.
copied_list2 = copy.deepcopy(original_list)
original_list[2][0] = 'C'
print(copied_list2)
print(original_list)


# In deep copy , even though we changed the mutable element in the original list, it is not reflecting in-
# -the copied list .
# As deep copy recursively copies the elements of the original list into copied list, we don't have any-
# -problem with mutable types.


list_of_lists = [[]]

list_of_lists *= 3

print(list_of_lists)

list_of_lists[0].append(3)

print(list_of_lists)

# Even though we updated item1 of list, all 3 items get auto updated because 3 lists formed-
# - inside a main list has reference to that single list item in line 3.
'''
-------
When you shallow copy arr1 (as shown below), you get arr2. arr1 and arr2 have DIFFERENT id but referencing the same
child elements. aka. each child have the same id
arr1 = [1,2,[3,4],5]
arr2 = copy.copy(arr1)
id(arr1) == id(arr2)        => FALSE
arr1 == arr2                    => TRUE
id(arr1[0]) == id(arr2[0])  => TRUE
id(arr1[1]) == id(arr2[1])  => TRUE
id(arr1[2]) == id(arr2[2])  => TRUE
id(arr1[3]) == id(arr2[3])  => TRUE
-----------------------------------------------------
Let's modify one of the elements.
arr1[0] = "a"
when you now print arr1 and arr2 you'll get the result as shown below
print(arr1[0])              => ['a', 2, [3, 4], 5]
print(arr2[0])              => [1, 2, [3, 4], 5]
The reason that the first element changed for arr1 but not for arr2 is because the first
element `1` is an int which is immutable. Therefore, when you "modify" it from `1` to "a",
you essentially create a new string object and now the first element of arr1 is pointing to
that new object "a". But the first element of arr2 is still pointing at `1`.
-----------------------------------------------------
Let's now modify an element in the list
arr1[2][0] = "b"
when you now print arr1 and arr2 you'll get the result as shown below
print(arr1[0])              => ['a', 2, ['b', 4], 5]
print(arr2[0])              => [1, 2, ['b', 4], 5]
This is what really tripped me first! But this is also due to mutability/immutability.
Now (looking at the arr1 before modifying), arr1[2] is [3,4] which is a list, hence mutable.
So, modifying that list won't create a new object like above. Therefore, modifying any element
inside the list is being shown on both arr1 and arr2. 
-----------------------------------------------------
'''

# As we see above, 2 or more lists with same content in the same order of elements always-
# - hold different memory locations.
# From lines 67 to 88, we saw that even lists with immutable data types will be having different
# memory locations, let us check with lists with mutable data types.

s1 = [[1,2,3],[4,5,6]]
s2 = [[1,2,3],[4,5,6]]

print('Id of s1 : ',id(s1))
print('Id of s2 : ',id(s2))

print(s1 is s2)
print(s1 == s2)

# Finally, Lists with mutable/immutable data types of the same order will never go interning and
# always have different memory locations.

