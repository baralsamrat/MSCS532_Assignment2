
# pip install memory_profiler

from typing import List
import timeit
import tracemalloc
from memory_profiler import memory_usage
import random

def quick_sort(arr: List[int]) -> List[int]:
    """
    Sorts an array using the Quick Sort algorithm.
    
    :param arr: List of integers to be sorted.
    :return: Sorted list of integers.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr: List[int]) -> None:
    """
    Sorts an array using the Merge Sort algorithm.
    
    :param arr: List of integers to be sorted. The list is sorted in place.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # Recursive call to sort the two halves
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy remaining elements of L[], if any
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy remaining elements of R[], if any
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def measure_performance(sort_function, data):
    """
    Measures and prints the performance of the sorting function in terms of execution time and memory usage.
    
    :param sort_function: Function that implements a sorting algorithm.
    :param data: List of integers to be sorted.
    """
    # Measure execution time
    start_time = timeit.default_timer()
    sort_function(data.copy())
    end_time = timeit.default_timer()
    execution_time = end_time - start_time

    # Measure memory usage
    def wrapper():
        sort_function(data.copy())

    mem_usage = memory_usage(wrapper)
    
    # Output performance metrics
    print(f"Execution Time: {execution_time:.6f} seconds")
    print(f"Memory Usage: {max(mem_usage) - min(mem_usage)} MiB")

if __name__ == "__main__":
    data_size = 1000  # Adjust data size as needed
    random_data = [random.randint(0, 10000) for _ in range(data_size)]

    print("Quick Sort Performance:")
    measure_performance(quick_sort, random_data)
    
    print("\nMerge Sort Performance:")
    measure_performance(merge_sort, random_data)
