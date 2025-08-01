'''
714. Best Time to Buy and Sell Stock with Transaction Fee
Medium
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note:

You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.
 
Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
 

Constraints:

1 <= prices.length <= 5 * 104
1 <= prices[i] < 5 * 104
0 <= fee < 5 * 104
'''
from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        '''
        At each day i, you update:
        cash = max(cash, hold + prices[i] - fee)
        Either keep not holding, or sell today
        hold = max(hold, cash - prices[i])
        Either keep holding, or buy today (using cash)
        '''
        n = len(prices)
        cash, hold = 0, -prices[0] # start with 0 cash and bought stock on day 0
        for i in range(1,n):
            cash = max(cash, hold + prices[i] - fee) #keep cash, or sell today
            hold = max(hold, cash - prices[i]) # keep holding, or buy today using cash
        
        return cash
if __name__ == '__main__':
    test = [
        [[1,3,2,8,4,9], 2],
        [[1,3,7,5,10,3], 3],
        [[1,2,3,4,5], 0],
        [[5,4,3,2,1], 0],
        [[1], 0],
    ]
    for prices, fee in test:
        print(f'prices={prices}, fee={fee} => {Solution().maxProfit(prices, fee)}')