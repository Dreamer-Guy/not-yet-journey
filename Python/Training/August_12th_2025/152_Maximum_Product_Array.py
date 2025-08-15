#url: https://leetcode.com/problems/maximum-product-subarray/description/

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=nums[0]
        maxNega=None
        prefixProduct=1
        for num in nums:
            if num==0:
                res=max(res,0)
                prefixProduct=1
                maxNega=None
                continue
            prefixProduct*=num
            if prefixProduct<0:
                if maxNega is None:
                    res=max(res,prefixProduct)
                    maxNega=prefixProduct
                else:
                    res=max(res,prefixProduct/maxNega)
            else:
                res=max(res,prefixProduct)
        return res
    

nums = [-2,0,2]
sol=Solution()
print(sol.maxProduct(nums))