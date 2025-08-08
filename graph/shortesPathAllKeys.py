'''
864. Shortest Path to Get All Keys
You are given an m x n grid grid where:

'.' is an empty cell.
'#' is a wall.
'@' is the starting point.
Lowercase letters represent keys.
Uppercase letters represent locks.
You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible, return -1. 

Example 1:

Input: grid = ["@.a..","###.#","b.A.B"]
Output: 8
Explanation: Note that the goal is to obtain all the keys not to open all the locks.
Example 2:

Input: grid = ["@..aA","..B#.","....b"]
Output: 6
Example 3:

Input: grid = ["@Aa"]
Output: -1

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either an English letter, '.', '#', or '@'. 
There is exactly one '@' in the grid.
The number of keys in the grid is in the range [1, 6].
Each key in the grid is unique.
Each key in the grid has a matching lock.
'''
from collections import deque


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        '''
        it is a state machine, not just simple row, cols
        (r,c, keysMask), km is a bitmask of collected keys.
        Goal state: keysMask == allKeysMask -> (1 << numKeys) -1
        For a key ch → bit = 1 << (ch - 'a').
        For a lock CH → require (keysMask & (1 << (CH - 'A'))) != 0.
        Cell types:
        #: wall → skip.
        . or @: free.
        lowercase a..f: picking it up means set the bit in keysMask.
        uppercase A..F: you may pass only if the bit for its lowercase exists in keysMask.
        '''
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        m, n = len(grid), len(grid[0])
        # Start by locating @ and counting how many distinct keys exist to build allKeysMask.
        # 1) scan for start and all keys
        sx = sy = -1
        allKeysMask = 0
        for i in range(m):
            for j in range(n):
                ch = grid[i][j]
                if ch == '@':
                    sx, sy = i, j
                elif 'a' <= ch <= 'f':
                    allKeysMask |= 1 << (ord(ch) - ord('a'))
        

        # Now restart the bfs from start, until you find the end state, aka mask = allKeysMask
        q = deque([(sx, sy, 0)])
        visited = {(sx, sy, 0)}
        steps = 0
        while q:
            for _ in range(len(q)):
                x, y, mask = q.popleft()
                if mask == allKeysMask:
                    return steps
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < m and 0 <= ny < n):
                        continue
                    cell = grid[nx][ny]
                    if cell == "#":
                        continue
                    # check for lock (before key pick up)
                    if 'A' <= cell <= 'F':
                        need = 1 << (ord(cell) - ord('A'))
                        if not (mask & need):
                            continue
                    new_mask = mask
                    if 'a' <= cell <= 'f':
                        new_mask = mask | (1<< (ord(cell) - ord('a')))
                    
                    state = (nx, ny, new_mask)
                    if state not in visited:
                        visited.add(state)
                        q.append(state)
            steps += 1

        return -1
