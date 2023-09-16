import matplotlib.pyplot as plt
import numpy as np
import time
start=time.time()
def bs(arr,low,high,x):
    if high>=low:
        mid=(high+low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return bs(arr,low,mid-1,x)
        else:
            return bs(arr,mid+1,high,x)
    else:
        return -1
arr=[]
n=int(input("enter the no of elements"))
for i in range(n):
    arr.append(int(input("enter the elements")))
print("sorted array",arr)
x=int(input("enter the key elements"))
result=bs(arr,0,len(arr)-1,x)
if result !=-1:
    print("element is present at index",str(result))
else:
    print("element is not present in array")
end=time.time()
print({end-start})
xpoints=np.array([500,1000,1500,2000,2500])
ypoints=np.array([0.00009,0.0010,0.0020,0.0030,0.0040,0.0050])
plt.plot(xpoints,ypoints)
plt.show()