#url: https://leetcode.com/problems/asteroid-collision/description/
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        st=[]
        for asteroid in asteroids:
            if len(st)==0 or (st[-1]*asteroid)>0:
                st.append(asteroid)
            elif st[-1]<0:
                st.append(asteroid)
            else:
                while len(st)>0 and st[-1]>0 and abs(st[-1])<abs(asteroid):
                    st.pop()
                if len(st)>0 and abs(st[-1])==abs(asteroid) and st[-1]>0:
                    st.pop()
                    continue
                if len(st)==0 or st[-1]<0:
                    st.append(asteroid)            
        return st
    
asteroids =[-8,8]
sol=Solution()
print(sol.asteroidCollision(asteroids))