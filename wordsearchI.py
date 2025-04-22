'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
'''

from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        path = list(word)
        def dfs(i,j,path,level):
            ch = board[i][j]
            if ch != path[level]:
                return False
            else:
                if level == len(path)-1:
                    return True
                board[i][j] = "#"
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    ni, nj = i+dx, j+dy
                    if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != "#":
                        if dfs(ni, nj, path, level+1):
                            return True
                board[i][j] = ch #backtrack

        for i in range(m):
            for j in range(n):
                if dfs(i,j,path,0):
                    return True
        else:
            return False