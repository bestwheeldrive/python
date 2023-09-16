def stack():
    stack=[]
    return stack
def checkempty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
    print("pushed element="+item)
def pop(stack):
    if (checkempty(stack)):
        return "stack is empty"
    return stack.pop()
s=stack()
push(s,str(1))
push(s,str(2))
push(s,str(3))
print("popped element"+pop(s))
print("stack after popping an element"+str(stack))
