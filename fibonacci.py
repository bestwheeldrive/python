def fibonacci(n):
    list=[0,1]
    a=0
    b=1
    if n<0:
        print("incorrect input")
    elif n==0:
        return[0]
    elif n==1:
        return list
    else:
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
            list.append(c)
        return list
n=int(input("enter the number"))
list=fibonacci(n)
print("the fibonacci list is:",list)
print("the fibonacci of given number is:",list[n])