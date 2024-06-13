def insertion_sort(arr):
    n = len(arr)  # Length of the array
    for i in range(1, n):  # Iterate over each element of the array starting from the second element
        temp = arr[i]  # Store the current element in a temporary variable
        j = i - 1  # Initialize j to be the index of the element before the current element
        # Iterate over the sorted part of the array (from arr[0] to arr[i-1]) and shift elements to the right to make space for temp
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]  # Shift the element to the right
            j -= 1  # Move to the previous element
        arr[j + 1] = temp  # Place temp in its correct sorted position
