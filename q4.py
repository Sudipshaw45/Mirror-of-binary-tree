class Node:
    def __init__(self, val):  
        self.data = val
        self.right = None

class Solution:
    def mirror(self, root):
        if root is None:
            return
      
        root.left, root.right = root.right, root.left
        
        self.mirror(root.left)
        self.mirror(root.right)
