#1. Write a operator for string formation = 
#2.how many types of string methods are there and give example for each method.
#3. explain %s, %d, %. , %x, %X ?
#4. To display list in string formatting which method you used %s or %d and explain why you use it ?
#5. explain the main two types of string formatting methods ? % and ___
"""
4.You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.
https://www.learnpython.org/en/String_Formatting
"""

data = ("John", "Doe", 53.44)
format_string = "Hello"

print(format_string % data)



# Sample strings for testing
text = "   Hello, World! Welcome to Python.   "
text2 = "hello world"
text3 = "1234"
text4 = "Hello World"
astring = "abcdefghijklm"

# String method tests
# 1. str.upper()
print(text.upper())

# 2. str.lower()
print(text.lower())

# 3. str.title()
print(text.title())

# 4. str.capitalize()
print(text.capitalize())

# 5. str.strip()
print(text.strip())

# 6. str.replace(old, new)
print(text.strip().replace("Python", "Programming"))

# 7. str.find(substring)
print(text.find("World"))

# 8. str.split(delimiter)
print(text.split())
print(text.split(","))

# 9. str.join(iterable)
words = ["Hello", "World", "Welcome", "to", "Python"]
print(" ".join(words))

# 10. str.isdigit()
print(text3.isdigit())
print(text4.isdigit())

# Additional examples
# 11. str.startswith(prefix)
print(text.strip().startswith("Hello"))

# 12. str.endswith(suffix)
print(text.strip().endswith("Python."))

# 13. str.splitlines()
multiline_text = "Hello\nWorld\nWelcome to Python."
print(multiline_text.splitlines())

# 14. str.zfill(width)
numeric_text = "42"
print(numeric_text.zfill(5))

# 15. str.lstrip(), str.rstrip(), str.strip() (with specific characters)
text_with_chars = "***Hello***"
print(text_with_chars.lstrip("*"))
print(text_with_chars.rstrip("*"))
print(text_with_chars.strip("*"))

# String slicing tests
# 16. Slicing with start and end indices
print(astring[3:7])  # Output: "defg"

# 17. Slicing with start, end indices, and step
print(astring[3:7:1])  # Output: "defg"

# 18. Slicing with step only (reverse the string)
print(astring[::-1])  # Output: "mlkjihgfedcba"

# 19. Slicing with negative indices
print(astring[-6:-2])  # Output: "ijkl"

# 20. Slicing with omitted start and end
print(astring[3:])  # Output: "defghijklm"
print(astring[:5])  # Output: "abcde"
print(astring[:])  # Output: "abcdefghijklm"

# 21. Slicing with negative step
print(astring[7:3:-1])  # Output: "hgfed"


"""
💀💀💀💀 Read the question clearly 💀💀💀💀


Try to fix the code to print out the correct information by changing the string.
https://www.learnpython.org/en/Basic_String_Operations
"""

s = "Hey there! what should this string be?"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
