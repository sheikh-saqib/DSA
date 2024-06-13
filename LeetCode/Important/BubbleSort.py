def bubble_sort(arr):
    n = len(arr)-1
    j = n
    while j >= 1:
        swap = False
        for i in range(j):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]= arr[i+1],arr[i]
                swap = True
        j-=1
        # optimization
        if swap == False:
            break
    return arr



 



arr = [10,1,7,6,14,9]

print(bubble_sort(arr))