# Write a palindrome program for string and a number

def palindrome(value):
    if (type(value) == int):
        revstr = int(str(value)[::-1])
    else:
        revstr = value[::-1]
    if(value == revstr):
        print("palindrome")
    else:
        print("Not a palindrome")

palindrome("dad")