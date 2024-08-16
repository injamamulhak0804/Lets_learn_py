def Kth_largest_element(arr):
    big = arr[0]
    for i in range(len(arr)):
        if(arr[i] > big):
            big = arr[i]
    
    print("Kth largest element is: ", big)

Kth_largest_element([1,2,4,5,45,23,56])