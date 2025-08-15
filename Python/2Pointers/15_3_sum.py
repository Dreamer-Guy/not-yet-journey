#url: https://leetcode.com/problems/3sum/
class Solution(object): 
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        nums=sorted(nums)
        res=[]
        for i in range(0,n-2,1):
            if i>0 and nums[i]==nums[i-1]:
                continue
            low=i+1
            high=n-1
            while low<high:
                sum=nums[i]+nums[low]+nums[high]
                if sum==0:
                    res.append([nums[i],nums[low],nums[high]])
                    low+=1
                    high-=1
                    while low<high and nums[low]==nums[low-1]:
                        low+=1
                    while low<high and nums[high]==nums[high+1]:
                        high-=1
                    continue
                if sum<0:
                    low+=1
                    continue
                high-=1
        return res

    
nums=[-1,0,1,2,-1,-4]
sol=Solution()
print(sol.threeSum(nums))