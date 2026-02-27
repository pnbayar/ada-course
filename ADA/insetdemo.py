import random
import time
from matplotlib import pyplot as plt

def insert_sort(A):
    n=len(A)
    for i in range(1,n):
        v=A[i]
        j=i-1
        while j>=0 and A[j]>v:
            A[j+1]=A[j]
            j=j-1
        A[j+1]=v

n_list=[5000,6000,7000,8000,9000,10000]
sort_time=[]
for n in n_list:
    arr=[random.randint(1,100) for _ in range(n)]
    s_t=time.time()
    insert_sort(arr)
    e_t=time.time()
    sort_time.append(e_t-s_t)
plt.plot(n_list,sort_time)
plt.show()