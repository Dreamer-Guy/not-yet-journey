#url: https://leetcode.com/problems/spiral-matrix/

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m=len(matrix)
        n=len(matrix[0])
        top=0
        bottom=m-1
        left=0
        right=n-1
        res=[]
        while top<=bottom and left<=right:
            for i in range(left,right+1,1):
                res.append(matrix[top][i])
            top+=1
            if top>bottom:
                break

            for i in range(top,bottom+1,1):
                res.append(matrix[i][right])
            right-=1
            if left>right:
                break
            
            for i in range(right,left-1,-1):
                res.append(matrix[bottom][i])
            bottom-=1
            if top>bottom:
                break
            
            for i in range(bottom,top-1,-1):
                res.append(matrix[i][left])
            left+=1
            if left>right:
                break
        return res
    
matrix = [[1],[2],[3]]
sol=Solution()
print(sol.spiralOrder(matrix))