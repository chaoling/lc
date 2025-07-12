'''
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        remember when all of the possible temp occur as array index?
        use a monotonic decreasing stack of temperatures (its indexes)
        go through the temp list backwards
        every time you saw a temp that is higher that the top of the stack
        pop it, until you reach a place that the top is higher than you, then
        you push yourself onto the stack
        '''
        n = len(temperatures)
        ans = [0] * n
        stk = []
        for i in range(n-1,-1,-1):
            while stk and temperatures[i] >= temperatures[stk[-1]]:
                stk.pop() 
            if stk:
                ans[i] = stk[-1] - i
            stk.append(i)
        return ans

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
    print(sol.dailyTemperatures([30, 40, 50, 60]))                # Output: [1, 1, 1, 0]
    print(sol.dailyTemperatures([30, 60, 90]))                    # Output: [1, 1, 0]
    print(sol.dailyTemperatures([100, 90, 80, 70]))                # Output: [0, 0, 0, 0]
    print(sol.dailyTemperatures([70, 70, 70, 70]))                # Output: [0