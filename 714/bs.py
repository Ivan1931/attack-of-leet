class Solution:
    def maxProfit(self, prices, fee):
        """
        1) for all possible purchase and sell combinations
            find the profit
            keep running maximum
           return maximum
        2) dynamic programming
        - d_sell[i] is the max profit at i if I sell stock at i
        - d_buy[i] is the max profit at i if I buy stock at i
        d_sell = max(d_buy[0:i]) + p[i] - 2
        d_buy = max(d_sell[0:i]) - p[i]
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        sell = 0
        buy = -prices[0]
        for p in prices[1:]:
            sell = max(sell, buy + p - fee)
            buy = max(buy, sell - p)
        return sell
        

def test():
    solution = Solution()
    test_1 = [[1, 3, 2, 8, 4, 9], 2]
    print(solution.maxProfit(*test_1), "= 8")


if __name__ == "__main__": test()
