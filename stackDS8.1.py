class stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self):
        data=int(input("enter the number"))
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def display(self):
        if self.items==[]:
            print("list is empty")
        else:
            for i in self.items:
                print(i)
s=stack()
while True:
    print("1.push")
    print("2.pop")
    print("3.Display")
    print("4.Quit")
    ch=input("enter the value for one operation:")
    if ch=="1":
        s.push()
    elif ch=="2":
        if s.isEmpty():
            print("stack is empty")
            break
        else:
            print("removed value:",s.pop())
    elif ch=="3":
        s.display()
    elif ch=="4":
        break