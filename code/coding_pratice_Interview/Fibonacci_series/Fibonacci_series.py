def Fibonacci_series(n):
    a = []
    a = [0,  1]
    
    for i in range(2, n):
        number = a[-1] + a[-2]
        a.append(number)
    
    for j in a:
        print(j)

Fibonacci_series(5)