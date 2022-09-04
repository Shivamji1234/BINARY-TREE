from unittest import result


class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

class binary:
    def __init__(self):
        self.root=None
    
    def comp(self,root):
        if root is None:
            return True
        q=[root]
        nq=[]
        level=[]
        result=[]
        while len(q)>0:
            for root in q:
                level.append(root.key)
                if root.left is not None:
                    nq.append(root.left)
                if root.right is not None:
                    nq.append(root.right)
                if root.left is None and root.right is not None:
                    return False, "not a complete binary tree"
            result.append(level)
            level=[]
            q=nq
            nq=[]
        return True,"complete binary tree"
# Driver program to test above function
  
""" Let us construct the following Binary Tree which
      is not a complete Binary Tree
            1
          /   \
         2     3
        / \     \
       4   5     6
    """

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
l=binary()
print(l.comp(root))
