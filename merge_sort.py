import time
import random
import matplotlib.pyplot as plt

def merge_sort(arr):
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

if __name__ == "__main__":
    elements = [5000, 10000, 15000, 20000, 25000]
    times = []

    for n in elements:
        arr = [random.randint(1, 100000) for _ in range(n)]
        start = time.time()
        merge_sort(arr)
        end = time.time()
        times.append(end - start)
        print(f"Sorted {n} elements in {end - start:.4f} seconds.")

    # Plotting
    plt.plot(elements, times, marker='o', color='green')
    plt.title("Merge Sort Time Complexity")
    plt.xlabel("Number of Elements (n)")
    plt.ylabel("Time taken (seconds)")
    plt.grid()
    plt.savefig("merge_sort_time_complexity.png")
    plt.show()