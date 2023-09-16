class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doubly:
    def __init_(self):
        self.head=None
    #to append a node
    def append(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
            self.head.prev=None
            self.head.next=None
        else:
            last=self.head
            while(last.next is not None):
                last=last.next
            last.next=newnode
            newnode.prev=last
    #to display node
    def display(self):
        current=self.head
        if self.head==None:
            print("list is empty")
            return
        print("node of doubly linked list")
        while current!=None:
            print(current.data)
            current=current.next
d=doubly()
d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.append(5)
d.append(6)
d.display()
