#url: https://leetcode.com/problems/subarray-sums-divisible-by-k/description/

class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        count=0
        prefixSum=0
        dic={0:1}
        for i,num in enumerate(nums):
            prefixSum+=num
            remainder=((prefixSum%k)+k)%k
            if remainder in dic:
                count+=dic[remainder]
                dic[remainder]+=1
            else:
                dic[remainder]=1
        return count
nums = [4,5,0,-2,-3,1]
k = 5   
sol=Solution()
print(sol.subarraysDivByK(nums,k))

