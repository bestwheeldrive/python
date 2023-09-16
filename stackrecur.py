def push(stack,item):
    stack.append(item)
def pop(stack):
    if not stack:
        raise Exception("stack is empty")
    return stack.pop()
def peek(stack):
    if not stack:
        raise Exception("Stack is empty")
    return stack[-1]
def size(stack):
    return len(stack)
def empty(stack):
    return not bool(stack)
def call_stack(n):
    if n<=0:
        return
    push(stack,n)
    call_stack(n-1)
    print(pop(stack))
stack=[]
call_stack(5)