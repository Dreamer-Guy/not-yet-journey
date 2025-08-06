#url: https://leetcode.com/problems/find-the-duplicate-number/description/

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i,num in enumerate(nums):
            if nums[abs(nums[i])]<0:
                return abs(nums[i])
            else:
                nums[abs(nums[i])]*=(-1)
        return -1

nums=[1,2,3,4,2]
sol=Solution()
print(sol.findDuplicate(nums))