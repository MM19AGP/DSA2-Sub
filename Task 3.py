def quicksort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)
        # Sort the left subarray
        quicksort(arr, low, pivot_index - 1)
        # Recursively sort the right subarray
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    # Choose the pivot as the middle element
    pivot_index = (low + high) // 2
    pivot = arr[pivot_index]
    # Move the pivot to the end 
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    
    # Partitioning process
    i = low  # Indicator for the smaller element

    for current_index in range(low, high):
        if arr[current_index] < pivot:
            arr[i], arr[current_index] = arr[current_index], arr[i]
            i += 1

    # Put the pivot back in its correct position
    arr[i], arr[high] = arr[high], arr[i]
    
    return i

# Test
words = ["apricot", "cherry", "elderberry", "banana", "dragonfruit"]
quicksort(words, 0, len(words) - 1)

print("Sorted words:", words)
