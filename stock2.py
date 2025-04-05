'''
122. Best Time to Buy and Sell Stock II
Solved
Medium
Topics
Companies
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
'''
def maxProfit(prices: List[int]) -> int:
    '''
    only track upward segment and count the profit in one scan
    '''
    n = len(prices)
    total_price = 0
    for i in range(1,n):
        if prices[i] > prices[i-1]:
            total_price += prices[i] - prices[i-1]

    return total_price

def anotherway(prices: List[int]) -> int:
       '''
        trading strategy:
        look at the peaks and valleys,
        buy at the valley, sell at the peak
        peak: left and right all no bigger than me
        valley: left and right all no smaller than me
        unless it is the head or tail, then:
        head/tail
        peak: right /left side is smaller than me
        valley: right /left  side is bigger than me
        '''
        '''
        simplify it to only count upward trend in one pass
        '''
        from collections import deque
        peaks, valleys = deque(),deque()
        n = len(prices)
        if n < 2:
            return 0
        #check the head
        if prices[1] > prices[0]:
            valleys.append(0)
        elif prices[1] < prices[0]:
            peaks.append(0)

        #check the middle
        for i in range(1,n-1):
            if prices[i-1] <= prices[i] and prices[i] >= prices[i+1]:
                peaks.append(i)
            elif prices[i-1] >= prices[i] and prices[i] <= prices[i+1]:
                valleys.append(i)
        
        #now check the tail
        if prices[n-1] > prices[n-2]:
            peaks.append(n-1)
        elif prices[n-1] < prices[n-2]:
            valleys.append(n-1)

        #now execute the trading strategy, aka buy at valley and sell at peak:
        #keep track of the total profit
        total_profit = 0
        while valleys and peaks:
            buy = valleys.popleft()
            sell = peaks.popleft()
            while sell <= buy and peaks:
                sell = peaks.popleft()
            if sell >= buy:
                total_profit = total_profit + prices[sell] - prices[buy]
        return total_profit