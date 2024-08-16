import math
def sum_of_digits(n):
    sum = 0
    while(n > 0):
        r = n % 10
        sum += r
        n = math.trunc(n / 10) 
    print(*"sum_of_digits: ", sum)

sum_of_digits(123)