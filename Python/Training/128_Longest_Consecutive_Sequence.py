#url: https://leetcode.com/problems/longest-consecutive-sequence/
class Solution(object):
    # def longestConsecutive(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     hashmap={}
    #     res=0
    #     for num in nums:
    #         if num in hashmap:
    #             continue
    #         if num-1 in hashmap and num+1 in hashmap:
    #             t1=hashmap[num-1]
    #             t2=hashmap[num+1]
    #             top=num+1+(t2[1]-1)
    #             bottom=num-1-(t1[0]-1)
    #             t3=hashmap[bottom]
    #             t4=hashmap[top]
    #             hashmap[bottom]=(t3[0],t3[1]+1+t4[0])
    #             hashmap[top]=(t4[0]+1+t3[1],t4[1])
    #             res=max(res,hashmap[top][0])
    #             hashmap[num]=(1,1)
    #             continue
    #         if num-1 in hashmap:
    #             t=hashmap[num-1]
    #             bottom=num-1-(t[0]-1)
    #             t1=hashmap[bottom]
    #             hashmap[bottom]=(t1[0],t1[1]+1)
    #             hashmap[num]=(t1[1]+1,1)
    #             res=max(res,t1[1]+1)
    #             continue
    #         if num+1 in hashmap:
    #             t=hashmap[num+1]
    #             top=num+1+(t[1]-1)
    #             t1=hashmap[top]
    #             hashmap[top]=(t1[0]+1,t1[1])
    #             hashmap[num]=(1,t1[0]+1)
    #             res=max(res,t1[0]+1)
    #             continue
    #         hashmap[num]=(1,1)
    #         res=max(res,1)
    #     return res
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #better solution(cleaner,faster)
        myset=set([])
        res=0
        for num in nums:
            myset.add(num)
        for num in myset:
            if num+1 in myset:
                continue
            count=1
            cur=num-1
            while cur in myset:
                count+=1
                cur-=1
            res=max(res,count)
        return res
    

nums = [9,1,4,7,3,-1,0,5,8,-1,6]
sol=Solution()
print(sol.longestConsecutive(nums))
        