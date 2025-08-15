#url: https://leetcode.com/problems/rotate-image/
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #Unable to solve in 30 minitues
        n=len(matrix)
        count=int(n/2)+(1 if n%2!=0 else 0)
        for i in range(count):
            for j in range(n):
                t=matrix[i][j]
                matrix[i][j]=matrix[n-1-j][i]
                matrix[n-1-j][i]=matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j]=matrix[j][n-1-i]
                matrix[j][n-1-i]=t

matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol=Solution()
sol.rotate(matrix)
print(matrix)
                


        