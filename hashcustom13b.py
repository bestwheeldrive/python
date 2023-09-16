class student:
    def __init__(self,name,email):
        self.name=name
        self.email=email
s=student("logan","james@wx.com")
result=hash(s)
print("hash value=",result)