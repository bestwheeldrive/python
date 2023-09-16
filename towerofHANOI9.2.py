def toh(n,spole,dpole,ipole):
    if(n==1):
        print("move disc 1 from pole",spole,"to pole",dpole)
        return
    toh(n-1,spole,ipole,dpole)
    print("move disc",n,'from pole',spole,"to pole",dpole)
    toh(n-1,ipole,dpole,spole)
n=int(input("enter the number of disks"))
toh(n,'A','B','C')