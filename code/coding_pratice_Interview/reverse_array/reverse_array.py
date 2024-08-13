def reverseArray(arr):
    # Method1
    # ans = arr[::-1]

    # Method2
    # For this reverse you have to print arr becoz it change the default array that means it affect the original array.
    # arr.reverse()

    # Method3
    ans1 = list(reversed(arr))

    print(ans1)
reverseArray([1,2,3])