# main.py
import time

from heap_sort import heap_sort
from merge_sort import merge_sort
from quick_sort import quickSort
from lcg import LCG

# Example: Generate a sequence of random numbers between 0 and 1
seed = 12345
a = 1664525
c = 1013904223
m = 2 ** 32
lcg = LCG(seed, a, c, m)

# Generate random sequence
random_sequence = lcg.generate_sequence(14000000)

# Measure execution time of quick sort
start_time = time.time() * 1000  # Convert to milliseconds
random_sequence_quick = random_sequence.copy()
quickSort(random_sequence_quick, 0, len(random_sequence_quick) - 1)
end_time = time.time() * 1000  # Convert to milliseconds
print("Time taken for quick sort (ms): {:.4f}".format(end_time - start_time))

# Measure the execution time of Merge sort
start_time = time.time() * 1000  # Convert to milliseconds
sorted_random_sequence = merge_sort(random_sequence)
end_time = time.time() * 1000  # Convert to milliseconds
print("Time taken for merge sort (ms): {:.4f}".format(end_time - start_time))


# Measure the execution time of Heap sort
start_time = time.time() * 1000  # Convert to milliseconds
sorted_random_sequence_heap = random_sequence.copy()
heap_sort(sorted_random_sequence_heap)
end_time = time.time() * 1000  # Convert to milliseconds
print("Time taken for heap sort (ms): {:.4f}".format(end_time - start_time))




