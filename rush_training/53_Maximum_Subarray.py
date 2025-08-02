#url: https://leetcode.com/problems/maximum-subarray/description/
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        prefixSum=0
        minSum=0
        res=nums[0]
        for num in nums:
            prefixSum+=num
            res=max(res,prefixSum-minSum)
            minSum=min(minSum,prefixSum)
        return res


nums = [-1]
sol=Solution()
print(sol.maxSubArray(nums))    