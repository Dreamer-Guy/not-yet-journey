#url: https://leetcode.com/problems/letter-case-permutation/

class Solution(object):
    def travel(self,s,index,res):
        if index==len(s)-1:
            if s[-1].isdigit():
                res.append(s)
            else:
                res.append(s[0:index]+s[index].lower())
                res.append(s[0:index]+s[index].upper())
            return 
        if s[index].isdigit():
            return self.travel(s,index+1,res)
        self.travel(s,index+1,res)
        newString=None
        if s[index].islower():
            newString=s[0:index]+s[index].upper()+s[index+1:]
        else:
            newString=s[0:index]+s[index].lower()+s[index+1:]
        self.travel(newString,index+1,res)
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res=[]
        self.travel(s,0,res)
        return res
    
s = "a1b2"
sol=Solution()
print(sol.letterCasePermutation(s))
        