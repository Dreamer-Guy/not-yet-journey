#url: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
import math
class Solution(object):
    def evaluate(self,a,b,operator):
        if operator=='-':
            return a-b
        if operator=='+':
            return a+b
        if operator=='/':
            return int(float(a)/float(b))
        return a*b
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st=[]
        for token in tokens:
            if token=='+' or token=='/' or token=='*' or (token=='-' and len(token)==1):
                b=st.pop()
                a=st.pop()
                st.append(self.evaluate(a,b,token))
            else:
                st.append(int(token)) 
        return int(st[-1])
    

tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
sol=Solution()
print(sol.evalRPN(tokens))