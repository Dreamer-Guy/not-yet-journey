#url: https://leetcode.com/problems/maximum-width-of-binary-tree/description/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        q=[root,None]
        res=0
        mini=None
        maxi=None
        root.val=0
        while len(q)>0:
            cur=q.pop(0)
            if cur is None:
                res=max(res,maxi-mini+1)
                maxi=None
                mini=None
                if len(q)==0:
                    break
                q.append(None)
                continue
            mini=min(mini,cur.val) if mini is not None else cur.val
            maxi=max(maxi,cur.val) if maxi is not None else cur.val
            if cur.left:
                cur.left.val=cur.val*2+1
                q.append(cur.left)
            if cur.right:
                cur.right.val=cur.val*2+2
                q.append(cur.right)
        return res
    
        
# Build the tree manually
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)

root.left.left = TreeNode(5)
root.left.right = TreeNode(3)

# root.right.left is None
root.right.right = TreeNode(9)

sol=Solution()
print(sol.widthOfBinaryTree(root))