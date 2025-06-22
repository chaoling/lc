'''
188. Best Time to Buy and Sell Stock IV
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
 

Constraints:

1 <= k <= 100
1 <= prices.length <= 1000
0 <= prices[i] <= 1000
'''
from typing import List
#from heapq import heappush, heappop
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        '''
        alg: to accumulate all the upward trend line
        \/\\/
        /-\//
        how to deal with the limit of transactions k?
        put all upward trend data (aka the profit) into a max heap (priority queue)
        for transaction in range(k):
            profit += mheap.heappop()
        note: this algo has flaws: ex:
        e.g: [1,2,4,2,5,7,2,4,9,0], since k = 2, you have profits: [ 3,5,7]
        but 7+5 = 12,
        if we take profit 1->7, that's 6, then 7, 
        total profits: 6+7=13
        so ultimately, we need to use dynamic programming method
        '''
        '''
        from heapq import heappush, heappop, heapify
        n = len(prices)
        if n < 2:
            return 0 #don't make any profit since there is only one day
        if n == 2:
            return max(0, prices[1]-prices[0]) #make profit only if upward trend or else 0
        #use two pointers
        pre, cur = 0, 1
        lmax, lmin = prices[0], prices[0]
        profits, total = [], 0
        while cur < n:
            if prices[cur] > prices[pre]: #upward trend
                #update the lmax
                lmax = max(lmax, prices[cur])
                # boundary condition:
                if cur == n-1:
                    profit = prices[cur] - lmin
                    if profit > 0:
                        heappush(profits, -profit) # this is the last day that you can make profit
            elif prices[cur] < prices[pre]: #downward trend:
                #make profit when?
                profit = lmax - lmin
                if profit > 0:
                    heappush(profits, -profit)
                #update new lmin
                lmin = lmax = prices[cur] 
            pre = cur
            cur += 1
            print(f"{pre=}, {cur=}, {lmax=} {lmin=}")
        print(f"{profits=}")
        for i in range(k):
            if profits:
                total -= heappop(profits) #all min heap -> max heap, negate the value
            else:
                break
        
        return total
    '''

    def maxProfitdp(self, k: int, prices: List[int]) -> int:
        '''
        alg: dynamic programming
        dp[i][j] = max(dp[i][j-1], prices[j] - min(prices[m] for m in range(j)))
        where i is the transaction number, j is the day number
        '''
        n = len(prices)
        if n < 2:
            return 0
        if k >= n // 2:
            # if k is larger than half of the days, we can make profit every upward trend
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n-1))
        # dp table
        dp = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            max_diff = -prices[0] # initialize as if we bought on day 0
            for j in range(1, n):
                # Option 1: Do nothing today → same profit as yesterday
                # Option 2: Sell today → add today’s price to best earlier (dp + buy price diff)

                dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
                  # max_diff keeps track of the maximum difference between the current price and the best price to buy before day j
                  # Option 3: maybe buying today gives better future opportunity
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])
        return dp[k][n - 1]

if __name__ == "__main__":
    prices = [1,2,4,2,5,7,2,4,9,0]
    s = Solution()
    print(s.maxProfitdp(2, prices))  # Output: 13