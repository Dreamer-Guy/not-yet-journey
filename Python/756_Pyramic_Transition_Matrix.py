#url:https://leetcode.com/problems/pyramid-transition-matrix/

class Solution(object):
    def isPossible(self,current,map):
        if len(current)==1:
            return True
        n=len(current)
        newCurrent=[]
        for i in range(n-1):
            l=[]
            for t1 in current[i]:
                for t2 in current[i+1]:
                    t=t1+t2
                    if t in map:
                        l+=map[t]
            if len(l)==0:
                return False
            newCurrent.append(l)
        return self.isPossible(newCurrent,map)

    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        map={}
        for item in allowed:
            key=item[0:2]
            if key in map:
                map[key].append(item[2:])
            else:
                map[key]=[item[2:]]
        current=[]
        for ite in bottom:
            current.append([ite])
        return self.isPossible(current,map)

        

bottom = "AAAA"
allowed = ["AAB","AAC","BCD","BBE","DEF"]
sol=Solution()
print(sol.pyramidTransition(bottom,allowed))