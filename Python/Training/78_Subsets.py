#url: https://leetcode.com/problems/subsets/

class Solution(object):
    def travel(self,nums,res,index):
        if index==len(nums):
            return
        newList=[]
        for arr in res:
            t=arr[:]
            t.append(nums[index])
            newList.append(t)
        res.extend(newList)
        return self.travel(nums,res,index+1)
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]
        self.travel(nums,res,0)
        return res

nums = [1,2] 
sol=Solution()
res=sol.subsets(nums)
print(res)      
        