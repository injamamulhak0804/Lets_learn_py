def factorial(n):
    sum = 1 
    for i in range(1, n + 1):
        sum *= i 
    print(f"The Factorial of {n} is: ", sum)
    
factorial(5)