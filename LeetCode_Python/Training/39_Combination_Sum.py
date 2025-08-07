#url: https://leetcode.com/problems/combination-sum/description/
class Solution(object):
    def travel(self,candidates,target,start,subset,res):
        if sum(subset)==target:
            t=subset[:]
            res.append(t)
            return
        n=len(candidates)
        for i in range (start,n,1):
            if sum(subset)+candidates[i]>target:
                continue
            subset.append(candidates[i])
            self.travel(candidates,target,i,subset,res)
            subset.pop(-1)


    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        subset=[]
        res=[]
        self.travel(candidates,target,0,subset,res)
        return res
candidates = [2,3,6,7]
target = 7

sol=Solution()
print(sol.combinationSum(candidates,target))        