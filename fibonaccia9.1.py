def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input("enter the number"))
if n<0:
    print("enter the positive number")
else:
    fib_ser=[]
    for i in range(n):
        fib_ser.append(fib(i))
    print("the fibonacci series is:",fib_ser)
    print("the fibonacci of given number is:",fib_ser[-1])
