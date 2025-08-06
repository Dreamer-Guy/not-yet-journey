#url: https://leetcode.com/problems/word-search/description/    
class Solution(object):
    def travel(self,board,visited,y,x,index,target):
        if index>=len(target):
            return True
        if y<0 or y>=len(board) or x<0 or x>=len(board[0]):
            return False
        if visited[y][x]==1:
            return False
        if board[y][x]!=target[index]:
            return False
        visited[y][x]=1
        if self.travel(board,visited,y-1,x,index+1,target):
            return True
        if self.travel(board,visited,y+1,x,index+1,target):
            return True
        if self.travel(board,visited,y,x-1,index+1,target):
            return True
        if self.travel(board,visited,y,x+1,index+1,target):
            return True
        visited[y][x]=0
        return False
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m=len(board)
        n=len(board[0])
        visited=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.travel(board,visited,i,j,0,word):
                    return True
        return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
sol=Solution()
print(sol.exist(board,word))