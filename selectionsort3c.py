import matplotlib.pyplot as plt
import numpy as np
import time
start=time.time()
def ss(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arr[min]>arr[j]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
arr=[]
n=int(input("enter the number of element"))
for i in range(n):
    arr.append(int(input("enter the element")))
print("unsorted array",arr)
ss(arr)
print("sorted array",arr)
end=time.time()
print({end-start})
xpoints=np.array([500,1000,1500,2000,2500])
ypoints=np.array([0.00009,0.0010,0.0020,0.0030,0.0040,0.0050])
plt.plot(xpoints,ypoints)
plt.show()