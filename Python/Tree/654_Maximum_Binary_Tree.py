#url: https://leetcode.com/problems/maximum-binary-tree/description/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(nums)==0:
            return None
        n=len(nums)
        maxi=max(nums)
        indexOfMax=nums.index(maxi)
        cur=TreeNode(nums[indexOfMax])
        cur.left=self.constructMaximumBinaryTree(nums[0:indexOfMax])
        cur.right=self.constructMaximumBinaryTree(nums[indexOfMax+1:])
        return cur        
    
nums=[3,2,1,6,0,5]
sol=Solution()
print(sol.constructMaximumBinaryTree(nums))