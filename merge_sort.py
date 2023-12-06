# quick_sort.py

def merge(array1, array2):
    """
    Merges two sorted arrays into a single sorted array.

    Parameters:
    array1 (list): The first sorted array.
    array2 (list): The second sorted array.

    Returns:
    list: A new sorted list containing all elements from array1 and array2.

    Example:
    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    """
    combined = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            combined.append(array1[i])
            i += 1
        else:
            combined.append(array2[j])
            j += 1

    while i < len(array1):
        combined.append(array1[i])
        i += 1

    while j < len(array2):
        combined.append(array2[j])
        j += 1

    return combined


def merge_sort(my_list):
    """
    Sorts a list using the merge sort algorithm.

    Parameters:
    my_list (list): The list to be sorted.

    Returns:
    list: A new sorted list.

    Example:
    >>> merge_sort([6, 2, 8, 4, 1, 3, 5, 7])
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list) / 2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)
