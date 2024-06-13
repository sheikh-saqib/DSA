def sort(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        while arr[left] == 0:
            left += 1
        while arr[right] == 1:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

arr = [1, 1, 0, 0, 0, 0, 1, 0]
print(sort(arr))
