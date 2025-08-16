#url: https://leetcode.com/problems/unique-paths-ii/description/

#Time: O(m*n)
#Space: O(m*n)

class Solution(object):
    # def backtracking(self,grid,dp,i,j):
    #     if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
    #         return 0
    #     if grid[i][j]==1:
    #         return 0
    #     if dp[i][j]!=-1:
    #         return dp[i][j]
    #     right=self.backtracking(grid,dp,i,j+1)
    #     down=self.backtracking(grid,dp,i+1,j)
    #     dp[i][j]=right+down
    #     return dp[i][j]
    # def uniquePathsWithObstacles(self, obstacleGrid):
    #     """
    #     :type obstacleGrid: List[List[int]]
    #     :rtype: int
    #     """
    #     m=len(obstacleGrid)
    #     n=len(obstacleGrid[0])
    #     if obstacleGrid[0][0]==1 or obstacleGrid[m-1][n-1]==1:
    #         return 0
    #     dp=[[-1]*n for _ in range(m)]
    #     dp[m-1][n-1]=1
    #     self.backtracking(obstacleGrid,dp,0,0)
    #     return dp[0][0]
    def uniquePathsWithObstacles(self,obstacleGrid):
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[0][0]==1 or obstacleGrid[m-1][n-1]==1:
            return 0
        dp=[[0]*n for _ in range(m)]
        dp[m-1][n-1]=1
        for i in range(m-2,-1,-1):
            if obstacleGrid[i][n-1]==0:
                dp[i][n-1]+=dp[i+1][n-1]
        for j in range(n-2,-1,-1):
            if obstacleGrid[m-1][j]==0:
                dp[m-1][j]+=dp[m-1][j+1]
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if obstacleGrid[i][j]==1:
                    continue
                dp[i][j]=dp[i][j+1]+dp[i+1][j]
        return dp[0][0]


obstacleGrid = [[0,1,0,0]]
sol=Solution()
print(sol.uniquePathsWithObstacles(obstacleGrid))
    