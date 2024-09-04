import math
def sum_of_digits(num):
    sum = 0
    i = len(str(num))
    while(num > 0):
        r = num % 10
        sum += r
        num = math.trunc(num /10)
    print(sum)
    
sum_of_digits(123)