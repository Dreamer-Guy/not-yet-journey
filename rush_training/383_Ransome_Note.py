#url: https://leetcode.com/problems/ransom-note/
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        let_note=[0]*26
        let_maga=[0]*26
        for c in ransomNote:
            let_note[ord(c)-ord('a')]+=1
        for c in magazine:
            let_maga[ord(c)-ord('a')]+=1
        for i in range(26):
            if let_note[i]>let_maga[i]:
                return False
        return True
    

ransomNote = "a"
magazine = "ba"
sol=Solution()
print(sol.canConstruct(ransomNote,magazine))