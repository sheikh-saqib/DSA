def rotateArrayLeft(arr: list, k: int) -> list:
    n = len(arr)
    temp = arr
    for i in range(n):
        temp[(i - k) % n] = arr[i]
    
    arr = temp
    return arr

# Example usage
arr = [1, 3, 6, 11, 12, 17]
k = 2
rotated_arr = rotateArrayLeft(arr, k)
print(rotated_arr)  # Output: [3, 4, 5, 1, 2]
