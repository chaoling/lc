'''
130. Surrounded Regions
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:

In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]
Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
'''
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Start DFS/BFS from all boundary 'O's and mark them as not flippable.
        Then flip all unmarked 'O's to 'X'.
        """
        m, n = len(board), len(board[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(i,j) -> bool:
            #mark the 'O''s none flippable by mark the cell something else
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if board[i][j] != 'O':
                return
            board[i][j] = '#'
            for di, dj in directions:
                dfs(i + di, j + dj)

        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m-1 or j == n-1) and board[i][j] == 'O':
                    dfs(i,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': #flip the 'O' if and only if it is not connected to the edge.
                    board[i][j] = 'X'

        for i in range(m):
            for j in range(n):
                if board[i][j] == '#': #flip the '#' back to 'O'
                    board[i][j] = 'O'

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    solution.solve(board)
    print(board)  # Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    board2 = [["X"]]
    solution.solve(board2)
    print(board2)  # Output: [["X"]]
    board3 = [["O","O","O"],["O","X","O"],["O","O","O"]]
    solution.solve(board3)
    print(board3)  # Output: [["O","O","O"],["O","X","O"],["O","O","O"]]
    # The last example shows that the 'O's on the edge are not flipped to 'X'.
    # The function correctly identifies and preserves the 'O's that are connected to the edge.
    # The time complexity is O(m*n) where m is the number of rows and n is the number of columns in the board.
    '''
    can slightly speed up the outer loop in Step 1 by iterating only over the borders, like so:
    for i in range(m):
    if board[i][0] == 'O':
        dfs(i, 0)
    if board[i][n - 1] == 'O':
        dfs(i, n - 1)
for j in range(n):
    if board[0][j] == 'O':
        dfs(0, j)
    if board[m - 1][j] == 'O':
        dfs(m - 1, j)

    '''