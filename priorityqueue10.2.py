class pq:
    def __init__(self):
        self.queue=[]
    def insert(self):
        data=int(input("enter the number"))
        self.queue.append(data)
    def delete(self):
        maxvalue=0
        for i in range(len(self.queue)):
            if self.queue[i]>self.queue[maxvalue]:
                maxvalue=i
        item=self.queue[maxvalue]
        del self.queue[maxvalue]
        print("removed element is",item)
        print()
    def display(self):
        if(len(self.queue)==0):
            print("queue empty")
        else:
            print(self.queue)
q=pq()
while True:
    print('queue operation\n 1.append 2.delete 3.display 4.exit')
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