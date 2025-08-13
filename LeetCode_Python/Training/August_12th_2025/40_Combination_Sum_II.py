#url:https://leetcode.com/problems/combination-sum-ii/

#Time:0(2^n) -> iterate through all combinations (C1Kn+C2Kn+...CnKn=2^n)
#Space:O(n) -> Worst case when iterate combination of n elements

class Solution(object):
    def travel(self,candidates,start,target,sum,subset,res):
        if sum==target:
            t=subset[:]
            res.append(t)
            return
        n=len(candidates)
        for i in range(start,n,1):
            if sum+candidates[i]>target or (i>start and candidates[i]==candidates[i-1]):
                continue
            subset.append(candidates[i])
            self.travel(candidates,i+1,target,sum+candidates[i],subset,res)
            subset.pop(-1)
        
        
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        subset=[]
        sum=0
        start=0
        candidates=sorted(candidates)
        self.travel(candidates,start,target,sum,subset,res)
        return res



candidates = [10,1,2,7,6,1,5]
target = 8
sol=Solution()
print(sol.combinationSum2(candidates,target))
        