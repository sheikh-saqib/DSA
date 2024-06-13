def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the index of the minimum element in the remaining unsorted portion of the array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap only if the minimum index has changed
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array is:", arr)
