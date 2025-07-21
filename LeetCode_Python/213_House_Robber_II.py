#url: https://leetcode.com/problems/house-robber-ii/
# class Solution(object):
#     def solveRob(self,nums,dp,i,isTakingFirst):
#         if i==len(nums)-1:
#             if isTakingFirst==0:
#                 return nums[i]
#             else:
#                 return 0
#         if i>=len(nums):
#             return 0
#         if dp[i][isTakingFirst]!=-1:
#             return dp[i][isTakingFirst]
        
#         taking=nums[i]+self.solveRob(nums,dp,i+2,isTakingFirst)
#         notTaking=self.solveRob(nums,dp,i+1,isTakingFirst)
#         dp[i][isTakingFirst]=max(taking,notTaking)
#         return dp[i][isTakingFirst]

#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n=len(nums)
#         dp=[[-1,-1] for _ in range(n)]
#         takingFirst=nums[0]+self.solveRob(nums,dp,2,1)
#         notTakingFirst=self.solveRob(nums,dp,1,0)
#         return max(takingFirst,notTakingFirst)

class Solution(object):
    def solveRob(self,nums):
        n=len(nums)
        if n==1:
            return nums[0]
        dp=[-1]*n
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n):
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        
        return dp[n-1]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if(n==1):
            return nums[0]
        takingFirst=self.solveRob(nums[0:n-1])
        notTakingFirst=self.solveRob(nums[1:])
        return max(takingFirst,notTakingFirst)

nums = [4,1,2,7,5,3,1]
sol=Solution()
print(sol.rob(nums))