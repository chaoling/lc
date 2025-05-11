'''
289. Game of Life

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.

 

Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 

Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
'''

from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        shadow = [[0 for _ in range(n)] for _ in range(m)]
        directions = ((0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1))
        def num_of_live_neighbors(i, j):
            count = 0
            for dx, dy in directions:
                nx, ny  = i+dx, j+dy
                if 0 <= nx < m and 0 <= ny < n:
                        count += board[nx][ny] & 1 #only check current state (LSB)
            return count

        for i in range(m):
            for j in range(n):
                live_cells = num_of_live_neighbors(i,j)
                if board[i][j] == 1 and 2 <= live_cells <=3:
                    board[i][j] |= 2 #set next state to 1 
                elif board[i][j] == 0 and live_cells == 3:
                    board[i][j] |= 2
                # Any live cell with fewer than two live neighbors dies
                # Any live cell with more than three live neighbors dies
                # Any live cell with two or three live neighbors lives on to the next generation.
                # Any dead cell with exactly three live neighbors becomes a live cell
     
        #Final pass to update the board, shift next state into current
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1 #shift bits right to update current state

if __name__ == '__main__':
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    Solution().gameOfLife(board)
    print(board)
    board = [[1,1],[1,0]]
    Solution().gameOfLife(board)
    print(board)
    board = [[1,0],[0,1]]
    Solution().gameOfLife(board)
    print(board)