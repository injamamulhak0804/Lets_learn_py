def reverse_string(value):
    # Method1
    # print(value[::-1]) #with plugin

    # Method2
    ans = ''.join(reversed(value))
    print(ans)


reverse_string("hello")

