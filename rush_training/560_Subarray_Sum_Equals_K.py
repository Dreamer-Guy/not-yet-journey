#url: https://leetcode.com/problems/subarray-sum-equals-k/description/
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        count=0
        map={0:1}
        prefix=[0]*n
        for i,num in enumerate(nums):
            t=prefix[i-1] if i>=1 else 0
            t+=nums[i]
            prefix[i]=t
        for sum in prefix:
            remaining=sum-k
            if remaining in map:
                count+=map[remaining]
            if sum in map:
                map[sum]+=1
            else:
                map[sum]=1
        return count
    
nums = [-1,1,0]
k =0
sol=Solution()
print(sol.subarraySum(nums,k))
    
            