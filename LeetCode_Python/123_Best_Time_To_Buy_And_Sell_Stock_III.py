class Solution(object):    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        dp=[0]*n #Represent the max profit with maximum m-1 transaction at day i
        maxTransactions=2
        for t in range(maxTransactions):
            buy=float('-inf')
            sell=0
            for i in range(n):
                buy=max(buy,dp[i]-prices[i])
                sell=max(sell,buy+prices[i])
                dp[i]=max(dp[i],sell)
        return dp[n-1]

# class Solution(object): 
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         buy1=-float('inf')
#         sell1=-float('inf')
#         buy2=-float('inf')
#         sell2=-float('inf')
#         for price in prices:
#             buy1=max(buy1,-price)
#             sell1=max(sell1,buy1+price)
#             buy2=max(buy2,sell1-price)
#             sell2=max(sell2,buy2+price)
#         return sell2
    
prices=[3,3,5,0,0,3,1,4]
sol=Solution()
print(sol.maxProfit(prices))