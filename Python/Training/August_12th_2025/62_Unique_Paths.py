#url: https://leetcode.com/problems/unique-paths/

# Time: O(m*n)
# Space: O(m*n)
class Solution(object):
    def backtracking(self,m,n,dp,i,j):
        if i<0 or i>=m or j<0 or j>=n:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        down=self.backtracking(m,n,dp,i+1,j)
        right=self.backtracking(m,n,dp,i,j+1)
        dp[i][j]=down+right
        return dp[i][j]
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[[-1]*n for _ in range(m)]
        dp[m-1][n-1]=1
        self.backtracking(m,n,dp,0,0)
        return dp[0][0]

m=3
n=2
sol=Solution()
print(sol.uniquePaths(m,n))
        