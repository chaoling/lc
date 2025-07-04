'''
994. Rotting Oranges
https://leetcode.com/problems/rotting-oranges/
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
'''
from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        simulate the rotten orange case one level at a time useing BFS
        '''
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        dirs = ((-1,0),(1,0),(0,-1),(0,1)) #up, down, left, right
        steps = -1
        # calculate the initial rotten oranges and add them all to the inital queue:
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                   q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        while q:
            for _ in range(len(q)):
                #every neighbor inside this loop if of the same level
                i, j = q.popleft()
                for di, dj in dirs:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                        #mark in rotten and add it to the queue
                        q.append((ni,nj))
                        grid[ni][nj] = 2
                        fresh -= 1
            steps += 1
    
        return max(0, steps) if fresh == 0 else -1

if __name__ == "__main__":
    sol = Solution()
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(sol.orangesRotting(grid))  # Output: 4
    grid2 = [[2,1,1],[0,1,1],[1,0,1]]
    print(sol.orangesRotting(grid2))  # Output: -1
    grid3 = [[0,2]]
    print(sol.orangesRotting(grid3))  # Output: 0