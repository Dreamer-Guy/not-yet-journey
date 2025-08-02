class Solution(object):
    def countDiff(self,s,str):
        count=0
        for i in range(len(s)):
            if s[i]!=str[i]:
                count+=1
        return count
    def counMini(self,current,endGene,bank,visited):
        if current==endGene:
            return 0
        res=None
        for i,str in enumerate(bank):
            if self.countDiff(current,str)==1 and visited[i]==-1:
                visited[i]=0
                t=1+self.counMini(str,endGene,bank,visited)
                if t>-1:
                    res=min(res,t) if res else t
        return res if res else -1

    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        visited=[-1]*len(bank)
        return self.counMini(startGene,endGene,bank,visited)

startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]

sol=Solution()
print(sol.minMutation(startGene,endGene,bank))