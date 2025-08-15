#url: https://leetcode.com/problems/product-of-array-except-self/description/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        res=[1]*n
        product=1
        for i in range(n):
            res[i]*=product
            product*=nums[i]
        product=1
        for i in range(n-1,-1,-1):
            res[i]*=product
            product*=nums[i]
        return res

nums=[1,2,3,4]
sol=Solution()
print(sol.productExceptSelf(nums))