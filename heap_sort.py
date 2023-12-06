# heap_sort.py
def heapify(arr, n, i):
    largest = i  # Initialize largest as root-index
    left = 2 * i + 1
    right = 2 * i + 2

    # See if right child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Heapify the root.
        heapify(arr, n, largest)


def build_max_heap(arr):
    n = len(arr)
    for j in range(n // 2 - 1, -1, -1):
        heapify(arr, n, j)


def heap_sort(arr):
    n = len(arr)
    build_max_heap(arr)
    for k in range(n - 1, 0, -1):
        # Swap maximal element with the element at index k
        arr[0], arr[k] = arr[k], arr[0]
        heapify(arr, k, 0)
