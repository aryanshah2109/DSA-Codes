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

preorder = [1,2,-1,-1,3,4,-1,-1,5,-1,-1]

root = create_btree(preorder)

def preorder_traverse(root):
    if root == None:
        return 
    print(root.data, end=" ")
    preorder_traverse(root.left)
    preorder_traverse(root.right)

preorder_traverse(root)