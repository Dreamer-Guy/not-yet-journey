#url: https://leetcode.com/problems/contiguous-array/description/

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={0:-1}
        diff=0
        res=0
        for i,num in enumerate(nums):
            if num==0:
                diff-=1
            else:
                diff+=1
            if diff in dic:
                res=max(res,i-dic[diff])
            else:
                dic[diff]=i
        return res

nums = [0,1,0]
sol=Solution()
print(sol.findMaxLength(nums))