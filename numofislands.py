'''
200. Number of Islands
https://leetcode.com/problems/number-of-islands/
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

from typing import List

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''
from typing import List


def numIslands(grid: List[List[str]]) -> int:
        '''
        for each cell, do dfs search until all cells connected by land are visited and count number of such island
        '''
        visited = set()
        m, n = len(grid), len(grid[0])
        res = 0
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        if not grid or not grid[0]:
            return 0
        if all(cell == "0" for row in grid for cell in row):
            return 0
        
        def dfs(curr):
            i,j = curr[0], curr[1]
            if (i,j) in visited:
                return
            if grid[i][j] == '0':
                visited.add((i,j))
                return
            if grid[i][j] == '1':
                if (i,j) not in visited:
                    visited.add((i,j))
                for dir in dirs:
                    next = (i+dir[0], j+dir[1])
                    if next[0] >= m or next[0] < 0 or next[1] >= n or next[1] < 0:
                        continue
                    if grid[next[0]][next[1]] == '1' and next not in visited:
                        dfs(next)
                return
            
        def dfs_stack(i, j):
            if (i, j) in visited:
                return
            visited.add((i, j))
            if grid[i][j] == '0':
                return
            stack = [(i, j)]
            while stack:
                ci, cj = stack.pop()
                for dir in dirs:
                    ni, nj = ci + dir[0], cj + dir[1]
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1" and (ni, nj) not in visited:
                        visited.add((ni, nj))
                        stack.append((ni, nj))


        for i in range(0,m):
            for j in range(0,n):
                curr = i, j
                if grid[i][j] == '1' and curr not in visited:
                    #dfs(i,j) #from current cell to dfs, until it 
                    dfs_stack(i, j)
                    res += 1
        
        return res

# Example usage
if __name__ == "__main__":
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(numIslands(grid))  # Output: 1

    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(numIslands(grid2))  # Output: 3
    grid3 = [
        ["1","0","1","1","0"],
        ["0","1","0","0","1"],
        ["1","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(numIslands(grid3))  # Output: 5
    grid4 = [
        ["0","0","0","0","0"],
        ["0","0","0","0","0"],
        ["0","0","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(numIslands(grid4))  # Output: 0
    grid5 = [
        ["1","1","1","1","1"],
        ["1","0","0","0","1"],
        ["1","0","1","0","1"],
        ["1","0","0","0","1"],
        ["1","1","1","1","1"]
    ]
    print(numIslands(grid5))  # Output: 1
    grid6 = [
        ["1","0","1","0","1"],
        ["0","1","0","1","0"],
        ["1","0","1","0","1"],
        ["0","1","0","1","0"]
    ]
    print(numIslands(grid6))  # Output: 10
    grid7 = [
        ["1","1","1","0","0"],
        ["1","0","1","0","0"],
        ["1","1","0","0","0"],
        ["0","0","0","1","1"]
    ]
    print(numIslands(grid7))  # Output: 3
    grid8 = [
        ["1","1","1","1","1"],
        ["1","0","0","0","1"],
        ["1","0","1","0","1"],
        ["1","0","0","0","1"],
        ["1","1","1","1","1"]
    ]
    print(numIslands(grid8))  # Output: 1