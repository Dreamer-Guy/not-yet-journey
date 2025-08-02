#url: https://leetcode.com/problems/merge-intervals/
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals=sorted(intervals,key=lambda a:a[0])
        st=[]
        for interval in intervals:
            if len(st)==0:
                st.append(interval)
                continue
            while len(st)>0 and st[-1][1]>=interval[0]:
                oldInterval=st.pop()
                interval=[oldInterval[0],max(oldInterval[1],interval[1])]
            st.append(interval)
        return st


intervals=[[1,4],[2,3]]
sol=Solution()
print(sol.merge(intervals))
        