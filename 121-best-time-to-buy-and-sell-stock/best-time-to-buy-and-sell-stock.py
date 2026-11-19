class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = 0
        high = 1
        res = 0
        n = len(prices)
        while high <n:
            if prices[high] > prices[low]:
                res = max(res ,prices[high]-prices[low])
            else:
                low = high
            high +=1
        return res 



        