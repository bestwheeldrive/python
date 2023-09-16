class bstnode:
    def __init__(self,val=None):
        self.left=None
        self.right=None
        self.val=val
    def insert(self,val):
        if not self.val:
            self.val=val
            return
        if self.val==val:
            return
        if val<self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left=bstnode(val)
            return
        if self.right:
            self.right.insert(val)
            return
        self.right=bstnode(val)
    def preorder(self,vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals
    def inorder(self,vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals
    def postorder(self,vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals
nums=[12,6,18,19,21,11,3,5,4,24,18]
bst=bstnode()
for num in nums:
    bst.insert(num)
print("preorder:")
print(bst.preorder([]))
print("postorder:")
print(bst.postorder([]))
print("inorder:")
print(bst.inorder([]))