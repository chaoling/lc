'''
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
'''

from typing import List


def maximalSquare(matrix: List[List[str]]) -> int:
        '''
        using 2D dp array to fill out the max square on each cell that it can make
        to the right, down and diagonal
        key intuition: A square can only grow as far as its shortest supporting edge lets it.
        dp[i][j] answers: “If I put the bottom‑right corner of a square here, how big can it be?”

        You need the smallest of the three adjacent squares to guarantee all edges are long enough.

        Adding the current '1' lets you extend that minimum by 1.
        '''
        m, n = len(matrix), len(matrix[0]) #m, n -> rows, cols
        dp = [[0]* (n+1) for _ in range(m+1)]
        #keep track of max size
        max_size = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                    max_size = max (dp[i][j], max_size)
        return max_size ** 2

if __name__=="__main__":
     matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
     print(maximalSquare(matrix))