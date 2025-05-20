'''
63: Unique Paths II
https://leetcode.com/problems/unique-paths-ii/
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 

Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
'''
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        use 2D dp array to fill the number of unique pathes
        initial: dp[0][0] = 1 if grid[0][0] != 1 else 0
        for any x,y other than 0,0 and x != 0 and y != 0: dp[x][y] = dp[x-1][y] + dp[x][y-1] or 0 if grid[x][y] == 1
        if x == 0: dp[x][y] = dp[0][y-1]
        if y == 0: dp[x][y] = dp[x-1][0]
        return dp[m-1,n-1]
        '''
        m, n = len(obstacleGrid), len(obstacleGrid[0]) # m rows, n columns
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 0 if obstacleGrid[0][0] == 1 else 1
        for i in range(m):
            for j in range(n):
                if (i,j) == (0,0):
                    continue
                elif obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = dp[0][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][0]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
# Example usage:
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
solution = Solution()
print(solution.uniquePathsWithObstacles(obstacleGrid))  # Output: 2
# The above code defines a class Solution with a method uniquePathsWithObstacles that calculates the number of unique paths in a grid with obstacles.