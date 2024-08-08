#1.List Syntax = []
#2.how many types of list methods are there and give example for each method.
#3.In list they use sort() or sorted() method
#4.Does sort() had any argument.
#For More Question  👇👇































"""
4. In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. You must add the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable.

You will also have to fill in the variable second_name with the second name in the names list, using the brackets operator []. Note that the index is zero-based, so if you want to access the second item in the list, its index will be 1.

""" 

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = None


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

#===========================================================================================================
#5. Sample lists for testing

mylist = [1, 2, 3, 4, 5]
another_list = ['a', 'b', 'c', 'd']
mixed_list = [1, 'two', 3.0, [4, 5]]

# Beginner Level

# 1. Accessing elements
element_0 = mylist[0]
element_last = mylist[-1]
slice_1_4 = mylist[1:4]

# 2. List length
length_of_mylist = len(mylist)

# 3. Adding elements
# 3.1. Append
mylist.append(6)

# 3.2. Extend
mylist.extend([7, 8])

# 3.3. Insert
mylist.insert(2, 'new')

# 4. Removing elements
# 4.1. Remove by value
mylist.remove('new')

# 4.2. Remove by index
popped_element = mylist.pop(2)

# 5. Checking for existence
exists_2 = 2 in mylist
exists_10 = 10 in mylist

# 6. List concatenation and repetition
concat_list = mylist + another_list
repeated_list = mylist * 2

# 7. Sorting and reversing
sorted_list = sorted(mylist)  # Returns a new sorted list
mylist.sort()  # Sorts in place
reversed_list = list(reversed(mylist))  # Reverses and returns a new list
mylist.reverse()  # Reverses in place

# Intermediate Level
    
# 8. List comprehension
squared_numbers = [x**2 for x in mylist if isinstance(x, int)]

# 9. Nested list indexing
nested_element = mixed_list[3][1]

# 10. List slicing with step
slice_step = mylist[::2]

# 11. Copying a list
list_copy = mylist.copy()
# write a code for deepcopy by import a copy 

# 12. Clearing a list
mylist.clear()

# Advanced Level

# 13. List with different data types
list_of_lists = [[1, 2], [3, 4], [5, 6]]

# 14. Flattening a list of lists
flattened_list = [item for sublist in list_of_lists for item in sublist]

# 15. List methods with lambda
filtered_list = list(filter(lambda x: x > 2, [1, 2, 3, 4, 5]))
mapped_list = list(map(lambda x: x * 2, [1, 2, 3, 4, 5]))

# 16. List comprehension with multiple for
comprehension_multi_for = [x * y for x in range(3) for y in range(3)]

# 17. Using list methods on lists of objects
class MyObject:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"MyObject({self.value})"

object_list = [MyObject(1), MyObject(2), MyObject(3)]
object_list.append(MyObject(4))
object_list.remove(MyObject(2))
