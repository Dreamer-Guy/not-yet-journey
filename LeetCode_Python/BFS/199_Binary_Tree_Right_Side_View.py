#url: https://leetcode.com/problems/binary-tree-right-side-view/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return []
        res=[]
        queue=[root,None]
        isFirstFlag=True
        while len(queue)>1:
            cur=queue.pop(0)
            if cur is None:
                isFirstFlag=True
                queue.append(None)
                continue
            if isFirstFlag:
                res.append(cur.val)
                isFirstFlag=False
            if cur.right:
                queue.append(cur.right)
            if cur.left:
                queue.append(cur.left)
        return res


node5 = TreeNode(5)
node4 = TreeNode(4)
node2 = TreeNode(2,right=node5)
node3 =TreeNode(3,right=node4)
root = TreeNode(1, left=node2, right=node3)
sol=Solution()
print(sol.rightSideView(root))