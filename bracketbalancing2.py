def brackets(exp):
    stack=[]
    for char in exp:
        if char["(","{","["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current=stack.pop()
            if current=='(':
                if char!=")":
                    return False
            if current=="{":
                if char!="}":
                    return False
            if current=="[":
                if char!="]":
                    return False
    if stack:
        return False
    return True
exp="{()}[()]"
if brackets(exp):
    print("balanced")
else:
    print("Not balanced")