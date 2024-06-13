def binary_search(arr,key):

    arr.sort()
    mid = 0
    start=0
    end = len(arr)-1
    while start <= end:
        mid = (start+end)//2
        # to avoid overflow of int
        # mid = start//2 + (end-start)//2 #s/2 +e/2 - s/2 = s+e/2
        if arr[mid] == key:
            return mid
        elif arr[mid]<key:
            start = mid+1
        else:
            end = mid-1
    return -1




arr = [3,5,9,13,27,31]

print(binary_search(arr,14))