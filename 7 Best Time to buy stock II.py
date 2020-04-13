"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time
(i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # [7,1,5,3,6,4]
        max_diff = 0

        if prices.index(max(prices)) > prices.index(min(prices)):
            max_diff = max(prices) - min(prices)

        # generate_low_high_values
        pairs = []
        current_profit = 0
        for index in range(len(prices) - 1):
            price = prices[index]
            next_price = prices[index + 1]
            print(price, next_price)

            if len(pairs) > 0:
                # if price < next_price and price not in pairs[-1]:
                if price < next_price:

                    pairs.append([price, next_price])
                    # pairs.append(next_price - price)
                    profit = next_price - price
                    print(profit, "profit")
                    current_profit += profit

            else:
                if price < next_price:
                    pairs.append([price, next_price])
                    profit = next_price - price
                    print(profit, "profit once")

                    current_profit += profit

        print(max_diff, "max_diff")
        print(pairs, "pairs")

        return max([max_diff, current_profit])

        # if len(prices) == 1:
        #     return 0
        # profit = 0
        # for i in range(1, len(prices)):
        #     if prices[i] > prices[i - 1]:
        #         profit += prices[i] - prices[i - 1]
        # return profit


sol_instance = Solution()

# x = sol_instance.maxProfit([7, 1, 5, 3, 6, 4])
# x1 = sol_instance.maxProfit([1, 2, 3, 4, 5])
# x2 = sol_instance.maxProfit([7, 6, 4, 3, 1])
x3 = sol_instance.maxProfit([6, 1, 3, 2, 4, 7])


# print(x, "x")
# print(x1, "x1")
print(x3, "x3")
