class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

idx = -1
def create_btree(preorder):
    ## TC = O(n)

    global idx
    idx += 1
    
    if preorder[idx] == -1:
        return None
    
    root = Node(preorder[idx])
    root.left = create_btree(preorder)
    root.right = create_btree(preorder)

    return root

preorder = [1,2,4,8,-1,-1,-1,5,-1,-1,3,6,-1,9,-1,-1,7,-1,10,-1,-1]

"""
                1              
             2     3
           4   5  6   7
         8         9    10

"""

root = create_btree(preorder)

def sumNodes(root):
    if root is None:
        return 0
    left_sum = sumNodes(root.left)
    right_sum = sumNodes(root.right)
    return left_sum + right_sum + root.data

print(sumNodes(root))
    