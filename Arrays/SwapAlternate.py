def swap_alternate(arr):
    end =len(arr)-1
    start = 0
    while start<end:
        arr[start],arr[start+1] = arr[start+1],arr[start]
        start+=2

arr = [1,2,3,4,5]
swap_alternate(arr)
print(arr)

    

    
