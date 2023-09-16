import matplotlib.pyplot as plt
import numpy as np
import time
start=time.time()
def insertionsort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and key<a[j]:
            a[j+1],a[j]=a[j],a[j+1]
            j=j-1
arr=[]
n=int(input("enter the number of elements"))
for i in range(n):
    arr.append(int(input("enter the element")))
print("unsorted array",arr)
insertionsort(arr)
print("sorted array",arr)
end=time.time()
print({end-start})
xpoints=np.array([500,1000,1500,2000,2500])
ypoints=np.array([0.00009,0.0010,0.0020,0.0030,0.0040,0.0050])
plt.plot(xpoints,ypoints)
plt.show()