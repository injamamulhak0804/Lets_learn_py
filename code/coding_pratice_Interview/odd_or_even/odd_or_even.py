def odd_or_even(num):
    count_even = 0
    count_odd = 0
    for i in num:
        if(i % 2 == 0):
            count_even += 1
        else:
            count_odd += 1
    print("Even: ", count_even)
    print("Odd: ", count_odd)

odd_or_even([2,4,567,5,6])