#url: https://leetcode.com/problems/largest-rectangle-in-histogram/
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n=len(heights)
        nextShort_left=[-1]*n
        nextShort_right=[n]*n
        st=[]
        for i in range(n):
            if(len(st)==0):
                st.append(i)
                continue
            while(len(st)>0 and heights[i]<heights[st[-1]]):
                nextShort_right[st.pop()]=i
            st.append(i)
        st=[]
        for i in range(n-1,-1,-1):
            if(len(st)==0):
                st.append(i)
                continue
            while(len(st)>0 and heights[i]<heights[st[-1]]):
                nextShort_left[st.pop()]=i
            st.append(i)
        res=0
        for i in range(n):
            res=max(res,heights[i]*(nextShort_right[i]-nextShort_left[i]+1-2))
        return res


heights=[2,1,5,6,2,3]
sol=Solution()
print(sol.largestRectangleArea(heights))
