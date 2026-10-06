class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        p1 = 0
        p2 = 1
        
        while p2  < len(prices):
            if prices[p2] > prices[p1]:
                profit = prices[p2] - prices[p1]
                if profit > max_profit:
                    max_profit = profit
            else:
                p1 = p2
            p2 +=1
        return max_profit


                
        

                
