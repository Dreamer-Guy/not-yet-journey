#url: https://leetcode.com/problems/group-anagrams/
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic={}
        for str in strs:
            t=str
            t="".join(sorted(t))
            if t in dic:
                dic[t].append(str)
            else:
                dic[t]=[str]
        res=[]
        for key in dic:
            res.append(dic[key])
        return res

strs = ["eat","tea","tan","ate","nat","bat"]
sol=Solution()
print(sol.groupAnagrams(strs))
        