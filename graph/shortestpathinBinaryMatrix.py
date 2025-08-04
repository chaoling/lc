'''
1091. Shortest Path in Binary Matrix
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
'''
from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        all 0 pathes surrounded by 1s
        do bfs from top left to bottom right
        '''
        visited = set()
        n = len(grid)
        dirs = [(-1,0),(0,-1),(1,0),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
        q = deque()
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        q.append((0,0,1))
        visited.add((0,0))
        while q:
            x,y,path_len = q.popleft()
            if (x,y) == (n-1,n-1):
                return path_len
            for dx,dy in dirs:
                nx, ny = x+dx, y+dy
                if 0<= nx <n and 0<= ny <n and grid[nx][ny] == 0 and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    q.append((nx,ny,path_len+1))
        return -1