#url: 3. Longest Substring Without Repeating Characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=126
        chars=[-1]*n
        count=0
        res=0
        for i,c in enumerate(s):
            index=ord(c)-ord(' ')
            if chars[index]!=-1:
                oldIndex=chars[index]
                for j in range(n):
                    if chars[j]!=-1 and chars[j]<=oldIndex:
                        chars[j]=-1
                        count-=1
            count+=1
            chars[index]=i
            res=max(res,count)
        return res
s = "abcabcbb"
sol=Solution()
print(sol.lengthOfLongestSubstring(s))
        