'''
52. N-Queens II
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 9
'''

class Solution:
    def totalNQueens(self, n: int) -> int:
        '''
        this puzzle can use dfs and backtrack technique
        iterate the chessboard row by row, for each row, try all possible columns,
        make sure: only one queen for each column/row/diag, so you may need a subroutine
        to check the validity of queen placement for each cell?
        once you have a solution, backtrack and do it again
        '''
        ans = [0]
        chess = [ [0 for _ in range(n)] for _ in range(n)] # construct n*n matrix represent the chess board
        def isvalid(row, col):
            if row == 0:
                return True
            if row >= n:
                return False
            #don't need to check row since we only place one queen at a time on each row
            # check column only on previous rows:
            level = 0
            for r in range(row-1,-1,-1): 
                level += 1
                if chess[r][col] == 1:
                    return False
                if 0 <= col-level < n and chess[r][col-level] == 1:
                    return False
                if 0 <= col+level < n and chess[r][col + level] == 1:
                    return False
            return True
            
        def dfs(chess, row, ans):
            #what is the end condition? total num of queens == n?
            if row == n:
                ans[0] += 1
                return
            #for each row, try all n columns:
            for col in range(n):
                if isvalid(row,col):
                    chess[row][col] = 1 #place the queen there and move on to the next row
                    dfs(chess, row + 1, ans) # try the next row, aka dfs
                    chess[row][col] = 0 # backtrack
            return

        dfs(chess, 0, ans)
        return ans[0]
# Time complexity: O(n^n) since we try all possible placements of queens
# Space complexity: O(n^2) for the chess board
# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.totalNQueens(4))  # Output: 2
    print(sol.totalNQueens(8))  # Output: 92
    print(sol.totalNQueens(1))  # Output: 1
    print(sol.totalNQueens(2))  # Output: 0
    print(sol.totalNQueens(3))  # Output: 0