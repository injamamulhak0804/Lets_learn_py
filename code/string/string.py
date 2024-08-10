#1. String formation 
# - Python use a C type formatting The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list)
# - operator %
# - some basic argument specifiers

"""
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
%x/%X - Integers in hex representation (lowercase/uppercase)

There are 10 string methods they are
1.upper()
2.lower()
3.title()
4.capitalize()
5.strip()
6.replace()
7.find()
8.split()
9.join()
10.isdigit()
11.slice
"""

name = "John"
age = 23
print("Hello, %s!" % name)
print("%s is %d years old." % (name, age))

#==================or=======================
print(f"Name: {name} and {age}") 

# Sample string
text = "   Hello, World! Welcome to Python.   "

# 1. str.upper()
upper_text = text.upper()
print("Uppercase:", upper_text)  # Output: "   HELLO, WORLD! WELCOME TO PYTHON.   "

# 2. str.lower()
lower_text = text.lower()
print("Lowercase:", lower_text)  # Output: "   hello, world! welcome to python.   "

# 3. str.title()
title_text = text.title()
print("Title Case:", title_text)  # Output: "   Hello, World! Welcome To Python.   "

# 4. str.capitalize()
capitalize_text = text.capitalize()
print("Capitalize:", capitalize_text)  # Output: "   hello, world! welcome to python.   "

# 5. str.strip()
stripped_text = text.strip()
print("Stripped:", stripped_text)  # Output: "Hello, World! Welcome to Python."

# 6. str.replace(old, new)
replaced_text = stripped_text.replace("Python", "Programming")
print("Replaced:", replaced_text)  # Output: "Hello, World! Welcome to Programming."

# 7. str.find(substring)
find_index = stripped_text.find("World")
print("Find 'World':", find_index)  # Output: 7

# 8. str.split(delimiter)
split_text = stripped_text.split()
print("Split Text:", split_text)  # Output: ['Hello,', 'World!', 'Welcome', 'to', 'Python.']

# 9. str.join(iterable)
joined_text = " ".join(split_text)
print("Joined Text:", joined_text)  # Output: "Hello, World! Welcome to Python."

# 10. str.isdigit()
digit_check = "1234".isdigit()
print("Is Digit (1234):", digit_check)



text = "Hello, World!"
# Slice from index 0 to 5
slice_text = text[0:5]
print("Sliced Text:", slice_text)  # Output: "Hello"

# Example of slicing a list
numbers = [1, 2, 3, 4, 5, 6]
# Slice from index 2 to 4
slice_numbers = numbers[2:5]
print("Sliced Numbers:", slice_numbers)  # Output: [3, 4, 5]

# Slicing with step
slice_numbers_step = numbers[1:5:2]
print("Sliced Numbers with Step:", slice_numbers_step)  # Output: [2, 4]