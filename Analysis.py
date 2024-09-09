# Installation:

# conda init
# conda create -n sorting_analysis python=3.9
# conda activate sorting_analysis
# conda install numpy matplotlib pandas memory_profiler

from typing import List
import timeit
import tracemalloc
from memory_profiler import memory_usage
import random
import numpy as np
import matplotlib.pyplot as plt

def quick_sort(arr: List[int]) -> List[int]:
    """Quick Sort algorithm."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr: List[int]) -> None:
    """Merge Sort algorithm."""
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def measure_performance(sort_function, data):
    """Measures execution time and memory usage."""
    # Measure execution time
    start_time = timeit.default_timer()
    sort_function(data.copy())
    end_time = timeit.default_timer()
    execution_time = end_time - start_time

    # Measure memory usage
    def wrapper():
        sort_function(data.copy())

    mem_usage = memory_usage(wrapper)
    
    return execution_time, max(mem_usage) - min(mem_usage)

def analyze_algorithms():
    datasets = {
        'Random': [random.randint(0, 10000) for _ in range(1000)],
        'Sorted': list(range(1000)),
        'Reverse Sorted': list(range(1000, 0, -1))
    }

    results = {
        'Algorithm': [],
        'Dataset': [],
        'Execution Time (s)': [],
        'Memory Usage (MiB)': []
    }

    for name, data in datasets.items():
        print(f"Analyzing {name} Dataset...")
        
        for sort_function, algo_name in [(quick_sort, 'Quick Sort'), (merge_sort, 'Merge Sort')]:
            exec_time, mem_usage = measure_performance(sort_function, data)
            results['Algorithm'].append(algo_name)
            results['Dataset'].append(name)
            results['Execution Time (s)'].append(exec_time)
            results['Memory Usage (MiB)'].append(mem_usage)

    return results

def plot_results(results):
    """Plots the results of the performance analysis."""
    import pandas as pd

    df = pd.DataFrame(results)
    
    # Plot execution time
    plt.figure(figsize=(14, 6))
    for algo in df['Algorithm'].unique():
        subset = df[df['Algorithm'] == algo]
        plt.plot(subset['Dataset'], subset['Execution Time (s)'], marker='o', label=algo)
    
    plt.title('Execution Time by Algorithm and Dataset')
    plt.xlabel('Dataset')
    plt.ylabel('Execution Time (s)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot memory usage
    plt.figure(figsize=(14, 6))
    for algo in df['Algorithm'].unique():
        subset = df[df['Algorithm'] == algo]
        plt.plot(subset['Dataset'], subset['Memory Usage (MiB)'], marker='o', label=algo)
    
    plt.title('Memory Usage by Algorithm and Dataset')
    plt.xlabel('Dataset')
    plt.ylabel('Memory Usage (MiB)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    results = analyze_algorithms()
    plot_results(results)
