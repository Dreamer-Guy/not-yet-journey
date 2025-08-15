#url: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        n=len(nums)
        for i in range(1,n,1):
            if nums[i]==nums[k]:
                continue
            nums[k+1]=nums[i]
            k+=1
        return k+1

