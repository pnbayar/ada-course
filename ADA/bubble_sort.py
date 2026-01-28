import random
import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Values of n (> 5000)
n_values = [5000, 7000, 9000, 11000, 13000]
time_taken = []

for n in n_values:
    arr = [random.randint(1, 100000) for _ in range(n)]

    start_time = time.time()
    bubble_sort(arr)
    end_time = time.time()

    elapsed_time = end_time - start_time
    time_taken.append(elapsed_time)

    print(f"n = {n}, Time Taken = {elapsed_time:.4f} seconds")

# Plotting the graph
plt.plot(n_values, time_taken, marker='o')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Bubble Sort: Time Complexity Analysis")
plt.grid(True)
# Save the plot
plt.savefig("bubble_sort_time_complexity.png", dpi=300, bbox_inches='tight')
plt.show()

