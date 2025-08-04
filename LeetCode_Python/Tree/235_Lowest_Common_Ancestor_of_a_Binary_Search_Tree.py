#url: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def traverse(self,cur,lower,greater):
        if not cur:
            return None
        if cur.val>greater.val:
            return self.traverse(cur.left,lower,greater)
        if cur.val<lower.val:
            return self.traverse(cur.right,lower,greater)
        return cur
            
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        greater=p if p.val>q.val else q
        lower=p if p.val<q.val else q
        return self.traverse(root,lower,greater)

# Leaf nodes
node0 = TreeNode(0)
node3 = TreeNode(3)
node5 = TreeNode(5)
node7 = TreeNode(7)
node9 = TreeNode(9)

# Intermediate nodes
node4 = TreeNode(4)
node4.left = node3
node4.right = node5

node2 = TreeNode(2)
node2.left = node0
node2.right = node4

node8 = TreeNode(8)
node8.left = node7
node8.right = node9

# Root node
root = TreeNode(6)
root.left = node2
root.right = node8

sol=Solution()
print(sol.lowestCommonAncestor(root,p=node0,q=node5).val)