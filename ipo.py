'''
502. IPO
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.

 

Example 1:

Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
Example 2:

Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6
 

Constraints:

1 <= k <= 105
0 <= w <= 109
n == profits.length
n == capital.length
1 <= n <= 105
0 <= profits[i] <= 104
0 <= capital[i] <= 109
'''
from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        '''
        put project in priority queue with weight of profits from high -> low
        for each project i in the queue, do it if the w > capital[i], stop when
        total project > k
        '''
        pq = []
        projects = sorted(zip(capital, profits))
        n = len(profits)
        i = 0
        while k > 0:
            while i < n and projects[i][0] <= w:
                heappush(pq, -projects[i][1])
                i += 1

            if not pq:
                break

            w -= heappop(pq)
            k -= 1
        return w

# 1. sort projects by capital
# 2. use a max heap to store the profits of the projects that can be done with current capital
# 3. for each project, if current capital >= capital required, add profit to max heap
# 4. if max heap is not empty, pop the max profit and add to current capital
# 5. repeat until k projects are done or no more projects can be done
# time: O(N log N)
# space: O(N)
if __name__ == '__main__':
    s = Solution()
    print(s.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))
    print(s.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]))
