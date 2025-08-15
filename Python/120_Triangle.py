# url: https://leetcode.com/problems/triangle/
class Solution:
    def solveMimumTotal(self,i,j,triangle,dp):
        if(dp[i][j]!=None):
            return dp[i][j]
        left=self.solveMimumTotal(i+1,j,triangle,dp)
        right=self.solveMimumTotal(i+1,j+1,triangle,dp)
        dp[i][j]=triangle[i][j]+min(left,right)
        return dp[i][j]

    def minimumTotal(self,triangle):
        n=len(triangle)
        dp=[]
        for list in triangle:
            dp.append([None]*len(list))
        dp.remove(dp[n-1])
        dp.append(triangle[n-1])
        return self.solveMimumTotal(0,0,triangle,dp)


triangle = [[-1],[2,3],[1,-1,-3]]
sol=Solution()
print(sol.minimumTotal(triangle))
        