#url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        holding=3e5
        res=0
        for price in prices:
            if price>holding:
                res+=(price-holding)
            holding=price
        return res
    

prices=[7,1,5,3,6,4]
sol=Solution()
print(sol.maxProfit(prices))
        