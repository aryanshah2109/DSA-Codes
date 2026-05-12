# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isIdentical(self, node, subRoot):
        if node is None or subRoot is None:
            return node == subRoot
        return (
            self.isIdentical(node.left, subRoot.left) and
            self.isIdentical(node.right, subRoot.right) and
            node.val == subRoot.val
        )

    def searchSubRoot(self, root, subRoot):
        if root is None or subRoot is None:
            return root == subRoot
            
        if root.val == subRoot.val and self.isIdentical(root, subRoot):
            return True
        return self.searchSubRoot(root.left, subRoot) or self.searchSubRoot(root.right, subRoot)

    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        return self.searchSubRoot(root, subRoot)
        
        