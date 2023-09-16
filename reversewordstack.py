def reverse(s):
    str=[]
    temp=""
    for i in range(len(s)):
        if s[i]=='':
            str.append(temp)
            temp=""
        else:
            temp=temp+s[i]
    str.append(temp)
    while len(str)!=0:
        temp=str[len(str)-1]
        print(temp,end="")
        str.pop()
    print()
s="no hello bye"
reverse(s)