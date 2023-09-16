class queue:
    def __init__(self):
        self.queue=[]
    def insert(self):
        data=int(input("enter the number"))
        self.queue.append(data)
    def delete(self):
        if len(self.queue)<1:
            return None
        else:
            print("removed element is",self.queue.pop(0))
    def display(self):
        if(len(self.queue)==0):
            print("queue empty")
        else:
            print(self.queue)
q=queue()
while True:
    print('queue operation \n'
          '1.Append\n'
          '2.Delete\n'
          '3.Display\n'
          '4.Exit')
    c=int(input("enter your choice"))
    if c==1:
        q.insert()
    elif c==2:
        q.delete()
    elif c==3:
        q.display()
    elif c==4:
        break
    else:
        print("invalid input")