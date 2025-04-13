'''
123. Best Time to Buy and Sell Stock III
Solved
Hard
Topics
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105
'''  


from typing import List


def maxProfit(prices: List[int]) -> int:
        '''
        one transaction means one buy then sell? (buy and hold does not make sense here)
        must sell before buying again
        how is the problem be considered a dynamic programming problem?
        what is the transfer function of dp[i]? i means ith day transaction, you can buy or sell or hold
     
        use two passes:
        left_profit: [ max profit from day 0 till day i, keep track of min price so far] 
        right_profit: [max profit from day i onward till last day, keep track of max price so far]
        combined: add these two
        '''
        # first pass: from left to right, keep track of min so far
        n = len(prices)
        left_profit = [0] * n
        min_p = prices[0]
        for i in range(1, n):
            min_p = min(min_p, prices[i])
            left_profit[i] = max(left_profit[i-1], prices[i] - min_p)
      
        
        # second pass: from right to left, keep track of max so far
        max_p, n = 0, len(prices)
        right_profit = [0] * n
        max_p = prices[-1]
        right_profit[-1] = 0 # no transaction on last day
        for i in range (n-2,-1,-1):
            max_p = max (max_p, prices[i])
            mp = max (max_p - prices[i], right_profit[i+1])
            right_profit[i] = mp
        
        max_total = 0
        for i in range(n):
            max_total = max(max_total, left_profit[i] + right_profit[i])

        return max_total


if __name__ == "__main__":
     print(maxProfit([3,3,6,0,0,3,1,4]))