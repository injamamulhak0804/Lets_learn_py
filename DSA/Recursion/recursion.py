# 1. Print your name in the number of times

# def recursionName(s, e):
#     if(s > e):
#         return 
#     print("zamam")
#     recursionName(s + 1, e)
# recursionName(1, 5)

# 2. print 1 to N

# def recursionN(i, e):
#     if(i > e):
#         return 
#     print(i)
#     recursionN(i+1, e)
# recursionN(1, 5)

# 3. print N to 1

# def recursion1ToN(i, e):
#     if(e < i):
#         return
#     print(e)
#     recursion1ToN(i, e-1)
# recursion1ToN(1, 5)

# 4. Recursion N to 1 without + operator

# def recursion4(s, e):
#     if(e < 1):
#         return
#     recursion4(s, e-1)
#     print(e)
# recursion4(3,3)

# 5. Recursion in Sum and Multiply

# def recursionSum(i,sum):
#     if(i < 1):
#         print(sum)
#         return  
#     recursionSum(i - 1, sum + i)
# recursionSum(3,0)

# 6. Reverse an Array using double pointer

# def recursionRevArr(arr, l, r):
#     if(r < l):
#         print(arr)
#         return
#     temp = arr[l]
#     arr[l] = arr[r]
#     arr[r] = temp
#     recursionRevArr(arr, l+1, r-1)
# recursionRevArr([1,2,3,4], 0, 3)

# using single pointer

# def recursionRevArr(arr, i, n):
#     if(i == int(n/2)):
#         print(arr)
#         return
#     temp = arr[i]
#     arr[i] = arr[n - i - 1]
#     arr[n - i - 1] = temp
#     recursionRevArr(arr, i + 1, n)
# recursionRevArr([1,2,3,4], 0, 4)

# 7. Recursion for Fibbonacci Series

# def recursionFibb(n):
#     if(n<=1):
#         return n 
#     last = recursionFibb(n - 1)
#     SecondLast = recursionFibb(n  - 2)
#     return last + SecondLast
# print(recursionFibb(4))

# 8. plaindrome

def recursionPalin(character, l, r):
    if l >= r:
        return ''.join(character)

    character[l], character[r] = character[r], character[l]
    return recursionPalin(character, l + 1, r - 1)
character = "zamam"
character_list = list(character)
palindrome = recursionPalin(character_list, 0, len(character_list) - 1)
print(palindrome)
