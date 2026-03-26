import time
import random
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10000)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

if __name__ == "__main__":
    elements = [5000, 10000, 15000, 20000, 25000]
    times = []

    for n in elements:
        arr = [random.randint(1, 100000) for _ in range(n)]
        start = time.time()
        quick_sort(arr, 0, len(arr) - 1)
        end = time.time()
        times.append(end - start)
        print(f"Sorted {n} elements in {end - start:.4f} seconds.")

    # Plotting
    plt.plot(elements, times, marker='o')
    plt.title("Quick Sort Time Complexity")
    plt.xlabel("Number of Elements (n)")
    plt.ylabel("Time taken (seconds)")
    plt.grid()
    plt.savefig("quick_sort_time_complexity.png")
    plt.show()