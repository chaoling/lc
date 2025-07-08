'''
62. Unique Paths
Medium
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:

Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        2D dp:
        dp[i][j] = sum(dp[i-1][j],dp[i][j-1])
        dp[0][0] = 1
        dp[0][.] = 1
        dp[.][0] = 1

        '''
        dp = [[0] * n for _ in range(m)]
        for col in range(n):
            dp[0][col] = 1
        for row in range(m):
            dp[row][0] = 1
        
        for row in range(1,m):
            for col in range(1,n):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        return dp[m-1][n-1]
if __name__ == '__main__':
    test = [
        [3,7],
        [3,2],
        [1,1],
        [100,100]
    ]
    for m,n in test:
        print(f'm={m}, n={n} => {Solution().uniquePaths(m,n)}')