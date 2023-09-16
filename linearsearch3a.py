import matplotlib.pyplot as plt
import numpy as np
import time
start=time.time()
def linear(ar,n,k):
    for i in range(n):
        if ar[i]==k:
            return i
        return -1
arr=[]
n=int(input("enter the no. of elements"))
for i in range(n):
    arr.append(int(input('enter the element')))
print("array elements are:",arr)
k=int(input("enter the key elements"))
res=linear(arr,len(arr),k)
if res==-1:
    print("element not found")
else:
    print("element %d found at index"%k,res)
end=time.time()
print({end-start})
xpoints=np.array([500,1000,1500,2000,2500,5000])
ypoints=np.array([0.00009,0.0029,0.0049,0.0079,0.0089,0.00219])
plt.plot(xpoints,ypoints)
plt.show()