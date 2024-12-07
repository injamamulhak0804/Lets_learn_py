

# 1. Odd or Even 
# def OddOrEven(num):
#     if (num%2==0) :
#         print("The Given number is Even")
#     else:
#         print("The Given Numbe is Odd")
# OddOrEven(13)

# 2. Find a given Character is Vowel or Contant

# def FindVowel(character):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     for i in vowels:
#         if(character == i):
#             print ("The Given Character is Vowels")
#             return
#     print("The Given character is Constants")
# FindVowel('i')
    
# 3. Count a Vowels
# def CountVowel(character):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     count = 0
#     for i in character:
#         for j in vowels:
#             if(i ==j):
#                 count+=1
#     print("The Total Number of Vowels in a character is: ", count)
# CountVowel("Hello")

# 4. Find the Greatest Number
# Using Buildin Function 

# def FindGreatest(nums):
#     res = max(nums)
#     print(res)
# FindGreatest([12,34,45,23])

# Without buildin 

# def FindGreatest(nums):
#     maximum = nums[0]
#     n = len(nums)
#     for i in range(0, n):
#         if(nums[i] > maximum):
#             maximum = nums[i]
#     print("The Maximum Number in a Array is: ", maximum)
# FindGreatest([12,34,23])

# 5. Positive Or Negative

# def PositiveOrNegative(num):
#     if(num == 0):
#         print("The Given number is Neutral Number")
#     if(num > 0):
#         print("The Given Number is positive number")
#     else:
#         print("The Given number is Negative Number")
# PositiveOrNegative(-23)

# 6. isAlphabet 

# def isAlphabet(character):
#     if(re.search("[A-Za-z]", character)):
#         print("The Given Character is String")
#     elif(re.search("[0-9]", character)):
#         print("The Given Charater is Number")
#     elif(re.search("r[^A-Za-z0-9]", character)):
#         print("The Given Character is Special Chracter")
# isAlphabet("jamam")

# 7. return Character Code

# def CharacterCode(c):
#     print(ord("a"))
# CharacterCode("z")

# 8. length of Character

# def LCharacter(c):
#     Len = len(list(c))
#     print("The Character length is: ", Len)
# LCharacter("zamam")

# 9. Sum of Digits

# def sumOfDigit(num):
#     sum = 0
#     while(num > 0):
#         n = num%10
#         sum += n
#         num = int(num/10)
#     print(sum)
# sumOfDigit(123)

# 10. Reverse a number

# def revNum(num):
#     ans = str(num)
#     print(ans[::-1])
# revNum(23)

# 11. Product of Digit

# def ProductOfDigit(nums):
#     product = 1
#     while(nums > 0):
#         n = nums%10
#         product*=n 
#         nums = int(nums/10)
#     print("The Product of Digit is: ", product)
# ProductOfDigit(123)

# 12. Sum of Naturtal Numbers

# def sumNaturalNum(nums):
#     sum = 0
#     for i in range (0, nums + 1):
#         sum += i
#     print("The Sum of Given Natural number is: ", sum)
# sumNaturalNum(3)


# 13. Prime or  not

# def PrimeOrNot(nums):
#     flag = 0
#     for i in range(1, nums + 1):
#         if(nums%i==0):
#             flag+=1
#     if(flag==2):
#         print("The Given Number is Prime Number")
#     else: 
#         print("The Given number is not Prime number")
# PrimeOrNot(11)
    

# 14. Print prime number from 0 to n

# def primeno(nums):
#     ans = []
#     for i in range(1, nums + 1):
#         flag = 0
#         for  j in range(1, i+1):
#             if(i%j==0):
#                 flag += 1
#         if(flag == 2):
#             ans.append(j)
#     print(ans)
# primeno(20)


# 15. power

# def power(a,b):
#     print(pow(a, b))
# power(2,3)

# 16. Amstrong

# def Amstrong(nums):
#     power = len(str(nums))
#     original = nums
#     sum = 0
#     while(nums > 0):
#         n = nums%10
#         sum += pow(n, power)
#         nums = int(nums / 10)
#     if(original == sum):
#         print("The Given number is Amstrong")
#     else:
#         print("The Given Number is not a Amstrong")
# Amstrong(372)


# 17. Toggle a String
# import re

# def ToggleStr(c):
#     ans = []
#     for i in range(0, len(c)):
#         if(re.search("[A-Z]", c[i])):
#             ans.append(c[i].lower())
#         elif(re.search("[a-z]", c[i])):
#             ans.append(c[i].upper())
#     print(''.join(ans))
# ToggleStr("ApPlE")


# 18. plaindrome
# def pali(c):
#     temp = c
#     rev = c[::-1]
#     if(temp == rev):
#         print("The Given String is plaindrome")
#     else:
#         print("The Given String is not Palindrome")
# pali("mom")

# 19. reverse a string

# def rev(c):
#     print(c[::-1])
#     print(''.join(reversed(c)))
# rev("mass")

# 20. Sum of interger in a str
# import re
# def SumIntInStr(str):
#     sum = 0
#     for i in str:
#         if(re.search("[0-9]", i)):
#             sum+=int(i)
#     print(sum)
# SumIntInStr("ja123mam45")

# 21. plaindrome a number

# def plainNum(num):
#     print(str(num)[::-1])
# plainNum(1234)

# 22. plaindrome without build in function

# def plainNum(num):
#     rev = 0
#     while(num > 0):
#         n = num % 10
#         rev = (rev*10) + n
#         num = int(num / 10)
#     print("reversed Number: ", rev)
# plainNum(1234)

# 23. count upper case
# import re
# def countUpperCase(c):
#     count = 0
#     for i in c:
#         if(re.search("[A-Z]", i)):
#             count+=1
#     print("The Upper Case Count is: ", count)
# countUpperCase("HellO World BhaI")

# 24. Reverse a Array 
# def revArr(nums):
#     ans = list(nums)
#     ans.reverse()
#     print(ans)
# revArr([1,2,3])

# def revArr(nums):
#     ans = []
#     for i in range(len(nums) - 1, -1, -1):
#         ans.append(nums[i])
#     print("reversed a Array: ",ans)
# revArr([1,2,3])

# 25. Search an element

# def search(arr, k):
#     for i in range(0, len(arr)):
#         if(arr[i]==k):
#             print("The Given Element index is: ", i)
# search([1,36,34,73,45,23], 45)

# 26. sum of Array 
# from functools import reduce

# def sumArr(num):
#     sum = reduce(lambda x, y: x + y, num)
#     print("The sum of Array is: ", sum)
# sumArr([1,2,3,4])

# 27. sort
# def sortArr(nums):
#     nums.sort()
#     print(nums)
# sortArr([2,1,4])

# def sortArr(nums):
#     for i in range(0, len(nums)):
#         for j in range(i + 1, len(nums)):
#             if(nums[i] > nums[j]):
#                 temp = nums[i]
#                 nums[i] = nums[j]
#                 nums[j] = temp 
#     print(nums)    
# sortArr([2,1,4])


# 28. sum of Positive

# def sumOfPositive(nums):
#     sum = 0
#     for i in nums:
#         if(i > 0):
#             sum += i 
#     print(sum)
# sumOfPositive([-3,-1,23,45,12,-45,23,-34])

# 29. Max maximum number

# def Maximum(nums):
#     print(max(nums))
# Maximum([12,34,45,12,45,78,23,98,8945,67])

# def Maximum(nums):
#     m = nums[0]
#     for i in nums:
#         if(i > m):
#             m = i 
#     print("The Maximum number in a Array: ", m)
# Maximum([12,34,45,12,45,78,23,98,8945,67])

# 30. SecondLargest

# def SecondLargest(nums):
#     ans = sorted(nums)
#     print("The second largest number is: ", ans[-2])
# SecondLargest([12,45,12,56,23,78,34,9])