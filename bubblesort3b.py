import matplotlib.pyplot as plt
import numpy as np
import time
start=time.time()
def bs(ar):
    n=len(ar)
    for i in range(n-1):
        for j in range(0,n-1-i):
            if(ar[j]>ar[j+1]):
                ar[j],ar[j+1]=ar[j+1],ar[j]
arr=[]
n=int(input("enter the no of elements"))
for i in range(n):
    arr.append(int(input('enter the element')))
print("unsorted array",arr)
bs(arr)
print("sorted array",arr)
end=time.time()
print({end-start})
xpoints=np.array([500,1000,1500,2000,2500,5000])
ypoints=np.array([0.00009,0.0010,0.0020,0.0030,0.0040,0.0050])
plt.plot(xpoints,ypoints)
plt.show()