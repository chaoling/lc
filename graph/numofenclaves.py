'''
1020. Number of Enclaves
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:


Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:


Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.
'''
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        '''
        find all land cells in the grid
        for each of them, do dfs and if any of the cell reaches the boundary then mark all of them 0
        rince and repeat, until finally the lonely island left 
        '''
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        m, n = len(grid), len(grid[0])
        visited = set()
        ans = 0
        def dfs(cell, islands):
            x, y = cell
            if x > m-1 or x < 0 or y > n-1 or y < 0 or x == 0 or y == 0 or x == m-1 or y == n - 1 or grid[x][y] == 0:
                return
            if (x, y) not in islands:
                islands.add((x,y))
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in islands:
                    dfs((nx, ny), islands)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    stack = [(i,j)]
                    visited.add((i,j))
                    sizes = 0
                    touches = False
                    while stack:
                        x,y = stack.pop()
                        sizes += 1
                        if x == 0 or y == 0 or x == m - 1 or y == n - 1:
                            touches = True

                        for dx, dy in dirs:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and (nx, ny) not in visited:
                                visited.add((nx, ny))
                                stack.append((nx, ny))
                    if not touches:
                        ans += sizes
        return ans