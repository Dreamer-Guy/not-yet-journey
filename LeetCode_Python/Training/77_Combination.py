#url: https://leetcode.com/problems/combinations/description/
class Solution(object):
    def travel(self,n,k,start,subset,res):
        if len(subset)==k:
            t=subset[:]
            res.append(t)
            return
        if len(subset)+(n-start+1)<k:
            return
        for i in range(start,n+1,1):
            subset.append(i)
            self.travel(n,k,i+1,subset,res)
            subset.pop(-1)

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res=[]
        subset=[]
        self.travel(n,k,1,subset,res)
        return res
n=4
k=2
sol=Solution()
print(sol.combine(n,k))        