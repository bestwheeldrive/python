import matplotlib.pyplot as plt
import numpy as np
import time
start=time.time()
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            (arr[i],arr[j])=(arr[j],arr[i])
    (arr[i+1],arr[high])=(arr[high],arr[i+1])
    return i+1
def qs(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        qs(array,low,pi-1)
        qs(array,pi+1,high)
array=[]
n=int(input("enter the no. of elements"))
for i in range(n):
    array.append(int(input("enter the elements")))
end=time.time()
print({end-start})
xpoints=np.array([500,1000,1500,2000,2500])
ypoints=np.array([0.00009,0.0010,0.0020,0.0030,0.0040,0.0050])
plt.plot(xpoints,ypoints)
plt.show()