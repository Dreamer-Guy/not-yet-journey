#url: https://leetcode.com/problems/target-sum/description/

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        total_sum=sum(nums)
        if total_sum<abs(target) or (total_sum-target)%2!=0:
            return 0
        nega_sum=(int)(total_sum-target)//2
        dp=[[0]*(nega_sum+1) for _ in nums]
        dp[0][0]+=1
        if nums[0]<=nega_sum:
            dp[0][nums[0]]+=1
        for i in range(1,n,1):
            for j in range(nega_sum+1):
                dp[i][j]+=dp[i-1][j]
                if(nums[i]<=j):
                    dp[i][j]+=dp[i-1][j-nums[i]]
        return dp[n-1][nega_sum]
    
nums = [2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53]
target = 1000
sol=Solution()
print(sol.findTargetSumWays(nums,target))