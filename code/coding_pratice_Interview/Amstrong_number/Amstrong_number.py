def Amstrong_number(num):
    sum = 0
    n1 = num
    for i in num:
        r = num % 10
        sum = sum + r * r * r 
        num = num/10
    if(n1 == sum):
        print("Amstrong number")
    else:
        print("Not a Amstrong Number")    

Amstrong_number(2)