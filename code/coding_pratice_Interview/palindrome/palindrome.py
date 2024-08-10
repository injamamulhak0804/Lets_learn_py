# Write a palindrome program for string and a number

def palindrome(value):
    revstr = int(str(value)[::-1])
    print("rev: ", type(revstr))
    if(value == revstr):
        print("palindrome")
    else:
        print("Not a palindrome")

palindrome(121)