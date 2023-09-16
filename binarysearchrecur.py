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
        return-1
arr=[]
n=int(input("enter the number of elements"))
for i in range(n):
    arr.append(int(input("enter elements")))
x=int(input("enter key elements"))
result=bs(arr,0,len(arr)-1,x)
if result!=-1:
    print("element present at index",str(result))
else:
    print("element not in array")