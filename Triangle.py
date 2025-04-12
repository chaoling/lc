'''
120. Triangle
Medium
Topics
Companies
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
 

Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
 

Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
'''
from typing import List


def minimumTotal(triangle: List[List[int]]) -> int:
    '''
    min path sum:
    rule: you can only move to the next row directly below or to the right
    '''
    n = len(triangle)
    if n == 1:
        return triangle [0][0]
    # use the dp[] array to store the current optimum path sum so far row by row
    dp = [ [0] * len(row) for row in triangle ]

    dp[0][0] = triangle[0][0]

    for i in range (1, n):
        m = len(triangle[i])
        for j in range (m):
            if j == 0:
                dp[i][j] = dp[i-1][0] + triangle[i][j] #left edge
            elif j == m-1:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j] #right edge 
            else:
                dp[i][j] = min( dp[i-1][j] , dp[i-1][j-1] )  + triangle[i][j] #interior


    return min (dp[-1])

def minimumTotal_1row(triangle: List[List[int]]) -> int:
    '''
    Keep a single list dp that always represents the current row's best sums.
    Process each new row right-to-left so the old values you still need aren't overwritten:
    '''
    dp = triangle[0][:]                 # start with the top element

    for i in range(1, len(triangle)):
        row = triangle[i]
        dp.append(0)                    # extend for the new rightmost cell

        # right‑to‑left sweep
        for j in range(len(row)-1, -1, -1):
            if j == 0:                  # left edge
                dp[j] = dp[j] + row[j]
            elif j == len(row)-1:       # right edge
                dp[j] = dp[j-1] + row[j]
            else:                       # interior
                dp[j] = min(dp[j-1], dp[j]) + row[j]

    return min(dp)


if __name__=="__main__":
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print(minimumTotal(triangle))
