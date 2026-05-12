# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def check_same(self, p, q):
        ## TC = O(n)

        if p is None or q is None:
            return p == q

        return self.check_same(p.left, q.left) and self.check_same(p.right, q.right) and p.val == q.val



    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        return self.check_same(p, q)