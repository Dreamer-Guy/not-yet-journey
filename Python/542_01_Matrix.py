#url: https://leetcode.com/problems/01-matrix/description/
class Solution(object):
    def expanding(self,mat,res,i,j,distance):
        if i<0 or j<0 or i>=len(mat) or j>=len(mat[0]):
            return
        if mat[i][j]==0:
            distance=0
        if res[i][j] is not None and res[i][j]<=distance:
            return
        res[i][j]=distance
        self.expanding(mat,res,i-1,j,distance+1)
        self.expanding(mat,res,i+1,j,distance+1)
        self.expanding(mat,res,i,j-1,distance+1)
        self.expanding(mat,res,i,j+1,distance+1)

        
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(mat)
        n=len(mat[0])
        res=[[None]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    self.expanding(mat,res,i,j,0)
        return res

#using queue
mat=[[0,0,0],[0,1,0],[1,1,1]]
sol=Solution()
print(sol.updateMatrix(mat))