import bisect

# Function to perform binary search
def binary_search(arr, x):
    # arr must be sorted
    index = bisect.bisect_left(arr, x) # finds the index where any given element should be inseted to keep the arrat sorted
     
    # Check if x is present at index
    if index < len(arr) and arr[index] == x:
        return index
    else:
        return -1

# Example usage
arr = [1, 2, 4, 4, 8, 10, 12]
x = 4

result = binary_search(arr, x)
if result != -1:
    print(f"Element {x} is present at index {result}")
else:
    print(f"Element {x} is not present in the array")
