'''
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Example 1:

Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105

O(N^2) time and O(N^2) space
'''
from collections import defaultdict
from typing import List
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        '''
        for nxn matrix, there are 2n rows + cols.
        make a hash table on the list of these 2n rows/cols
        if find a pair, add counter by 1
        '''
        n = len(grid)
        d = defaultdict(int)

        # Cout each row
        for row in grid:
            d[tuple(row)] += 1

        count = 0
        # Count each column
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            count += d[col] # if col in d, add the count, allow duplicates

        return count

if __name__ == "__main__":
    s = Solution()
    print(s.equalPairs([[3,2,1],[1,7,6],[2,7,7]])) # 1
    print(s.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])) # 3