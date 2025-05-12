'''
73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Modify matrix in-place such that if an element is 0, its entire row and column are set to 0.
        Uses recursion with a seen map to track visited positions.
        """
        seen = set()  # Keep track of (i, j) cells already processed
        m, n = len(matrix), len(matrix[0])

        def clear_neighbor(i, j):
            if (i, j) in seen:
                return
            seen.add((i, j))

            # Clear entire row
            for col in range(n):
                if matrix[i][col] != 0:
                    matrix[i][col] = 0
                elif (i, col) not in seen:
                    clear_neighbor(i, col)

            # Clear entire column
            for row in range(m):
                if matrix[row][j] != 0:
                    matrix[row][j] = 0
                elif (row, j) not in seen:
                    clear_neighbor(row, j)

        # Main scan
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0 and (i, j) not in seen:
                    clear_neighbor(i, j)
        # No return needed as we modify the matrix in place


    def setZeroesOptimized(self, matrix: List[List[int]]) -> None:
        """
        Optimized version using first row and first column as markers.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # Mark rows and columns to be zeroed
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero out marked rows
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        # Zero out marked columns
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # Handle the first row and column
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
# Example usage
if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sol.setZeroesOptimized(matrix)
    print(matrix)  # Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    sol.setZeroesOptimized(matrix)
    print(matrix)  # Output: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    # Output: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sol.setZeroesOptimized(matrix)