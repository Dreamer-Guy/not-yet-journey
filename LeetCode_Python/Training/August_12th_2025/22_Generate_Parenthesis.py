#url: https://leetcode.com/problems/generate-parentheses/

class Solution(object):
    def backtracking(self,open,close,cur,res):
        if open==0 and close==0:
            res.append(cur)
            return
        if open==0:
            self.backtracking(open,close-1,cur+")",res)
            return
        if open==close:
            self.backtracking(open-1,close,cur+"(",res)
            return
        self.backtracking(open-1,close,cur+"(",res)
        self.backtracking(open,close-1,cur+")",res)
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        open=n
        close=n
        res=[]
        self.backtracking(open,close,"",res)
        return res

n=1
sol=Solution()
print(sol.generateParenthesis(n))