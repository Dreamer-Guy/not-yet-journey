#url: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def traverse(self,cur,p,q):
        if not cur:
            return None
        if cur==p or cur==q:
            return cur
        left=self.traverse(cur.left,p,q)
        right=self.traverse(cur.right,p,q)
        if left and right:
            return cur
        return left if left else right
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.traverse(root,p,q)
        