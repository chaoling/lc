'''
934. Shortest Bridge
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
'''
from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        '''
        1) find the two island and mark them in the grid with different numbers 2 vs 1
        2) do bfs again from one island to another by flipping the grid
           and find the shortest flips
        '''
        from typing import List
        from collections import deque


        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False]*n for _ in range(n)]
        queue = deque()

        # DFS to mark the first island and add its border to the queue
        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= n or visited[x][y] or grid[x][y] == 0:
                return
            visited[x][y] = True
            grid[x][y] = 2
            queue.append((x, y))
            for dx, dy in directions:
                dfs(x + dx, y + dy)

        # Find and mark the first island
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

        # BFS to expand from the first island and find the shortest bridge
        steps = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if not visited[nx][ny]:
                            if grid[nx][ny] == 1:
                                return steps  # Found the second island
                            visited[nx][ny] = True
                            queue.append((nx, ny))
            steps += 1
        return steps