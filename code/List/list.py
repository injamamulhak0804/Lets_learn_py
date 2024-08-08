#1. list syntax is []
# - list is very similar to array.
# - u can store any type of variables at a single list
# - [1,2,3,"zamam"]

"""
list methods
There are 11 types of list methods:
1.append()
2.extend([])
3.insert(position, "value")
4.remove("value")
5.pop([index]) or pop()
6.clear()
7.index("value")
8.count("value")
9.sort() or sort(reverse = True)
10.reverse()
11.copy() Returns a shallow copy of the list.
"""


# Initial list
shopping_list = ['milk', 'eggs', 'bread']

# Adding items
shopping_list.append('butter')
shopping_list.extend(['cheese', 'ham'])

# Inserting an item
shopping_list.insert(2, 'yogurt')

# Removing an item
shopping_list.remove('bread')

# Popping an item
last_item = shopping_list.pop()

# Sorting the list
shopping_list.sort()

# Reversing the list
shopping_list.reverse()

# Copying the list
new_list = shopping_list.copy()
shopping_list.remove("milk")

print(shopping_list)
print(new_list)

