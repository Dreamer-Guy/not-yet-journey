#url: https://leetcode.com/problems/coin-change/description/

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount==0:
            return 0
        dp=[-1]*(amount+1)
        dp[0]=0
        coins=list(filter(lambda x:x<=amount,coins))
        if len(coins)==0:
            return -1
        maxCoin=max(coins)
        for i in range(1,amount+1,1):
            temp=float('inf')
            for coin in coins:
                if dp[i-coin]==-1:
                    continue
                temp=min(temp,dp[i-coin]+1)
            dp[i]=temp if temp!=float('inf') else -1
        return dp[amount]
    

coins = [456,117,5,145]
amount = 1459

sol=Solution()
print(sol.coinChange(coins,amount))