def prime_num(n):
    flag = 0
    for i in range(2, n):
        if(n % i == 0):
            flag = 1
    
    if(flag):
        print("It's Not a Prime Number")
    else:
        print("It's a Prime Number")

        


prime_num(7)