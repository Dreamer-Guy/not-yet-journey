#url: https://leetcode.com/problems/top-k-frequent-elements/
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """ 
        dic={}
        minHeap=[]
        for num in nums: 
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        for key in dic:
            heapq.heappush(minHeap,(-dic[key],key))
        res=[]
        for i in range(k):
            prio,val=heapq.heappop(minHeap)
            res.append(val)
        return res


nums=[1]
k=1

sol=Solution()
print(sol.topKFrequent(nums,k))

        