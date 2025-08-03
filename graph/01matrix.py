'''
542. 01 Matrix
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
 

Note: This question is the same as 1765: https://leetcode.com/problems/map-of-highest-peak/
'''
from collections import deque
from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        do multi-source bfs on matrixes,    
        where all 0s are the sources.
        The distance from a 0 to its neighbors is 1.
        The distance from a 0 to its neighbor's neighbor is 2, and so on
        until all cells are visited.
        Time complexity: O(m * n)
        Space complexity: O(m * n)
        where m is the number of rows and n is the number of columns in the matrix.
        The space complexity is mainly due to the queue used for BFS and the result matrix.
        '''
        m, n = len(mat), len(mat[0])
        q = deque()
        res = [[float('inf')] * n for _ in range(m)]
        dirs = [(0,-1),(-1,0),(0,1),(1,0)]
        # Step 1: Add all 0s to the queue
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    q.append((i, j))

        # Step 2: BFS from all 0s:
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx< m and 0 <= ny < n and res[nx][ny] == float("inf"):
                        res[nx][ny] = res[x][y] + 1
                        q.append((nx,ny))
        return res