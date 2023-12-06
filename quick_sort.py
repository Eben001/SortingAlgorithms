# quick_sort.py
# Function to find the partition position
def partition(array, low, high):
    # Select the rightmost element as pivot

    pivot = array[high]
    # Pointer
    i = low - 1
    # Traverse through all elements
    # Compare each element with pivot

    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found swap it with the greater element at index i + 1
            i = i + 1
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    # Return the position of the pivot element
    return i + 1


# Function to perform Quick Sort
def quickSort(array, low, high):
    if low < high:
        # Call of the partition function
        pi = partition(array, low, high)
        # Recursive call to the left of pivot
        quickSort(array, low, pi - 1)
        # Recursive call to the right of pivot
        quickSort(array, pi + 1, high)
