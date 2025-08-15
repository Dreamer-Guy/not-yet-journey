#url: https://leetcode.com/problems/house-robber/
class Solution(object):
    def solveRob(self,nums,dp,i):
        if i>=len(nums):
            return 0
        if dp[i]!=-1:
            return dp[i]
        taking=nums[i]+self.solveRob(nums,dp,i+2)
        notTaking=self.solveRob(nums,dp,i+1)
        dp[i]=max(taking,notTaking)
        return dp[i]
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[-1]*n
        return self.solveRob(nums,dp,0)
    
nums = [2,7,9,3,1]
sol=Solution()
print(sol.rob(nums))
        