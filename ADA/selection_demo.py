import random
import time
import matplotlib.pyplot as plt

def bubble_sort(l):
    n= len(l)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if(l[j]>l[j+1]):
                l[j+1],l[j]=l[j],l[j+1]

def selection_sort(l):
    n= len(l)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if(l[j]<l[min]):
                min=j
            l[min],l[i]=l[i],l[min]

n_vales=[5000,6000,7000,8000,9000,10000]
selection_sort_time=[]
bubble_sort_time=[]

for n in n_vales:
    arr = [random.randint(1, 100000) for _ in range(n)]
    start_time_b=time.time()
    bubble_sort(arr)
    end_time_b=time.time()
    bubble_sort_time.append(end_time_b-start_time_b)

    start_time_s=time.time()
    selection_sort(arr)
    end_time_s=time.time()
    selection_sort_time.append(end_time_s-start_time_s)

print(bubble_sort_time)
print(selection_sort_time)

# Plotting the graph
plt.plot(n_vales, bubble_sort_time, marker='o')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Bubbble Sort: Time Complexity Analysis")
plt.grid(True)
# Save the plot
plt.savefig("bubble_sort_time_complexity.png", dpi=300, bbox_inches='tight')
plt.show()

