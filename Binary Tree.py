class Node:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right = None

def inorder(self,root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

