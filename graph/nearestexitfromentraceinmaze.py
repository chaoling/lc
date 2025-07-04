'''
1926 Nearest Exit from Entrance in Maze
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.


Example 1:


Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.
Example 2:


Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.
Example 3:


Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.
 

Constraints:

maze.length == m
maze[i].length == n
1 <= m, n <= 100
maze[i][j] is either '.' or '+'.
entrance.length == 2
0 <= entrancerow < m
0 <= entrancecol < n
entrance will always be an empty cell.
'''
from collections import deque
from typing import List
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        '''
        hint: since we are looking for nearest exit from the entrance, we can
        find shortest path from entrance to exit using BFS
        a list of [x,y] represent the node in the graph matrix
        '''
        rows, cols = len(maze), len(maze[0])
        entrance = (tuple(entrance))  # convert entrance to tuple for immutability
        visited = {entrance}  # use a set to keep track of visited nodes
        q = deque([entrance])
        moves = ((-1,0),(1,0),(0,-1),(0,1)) #move up, down, left, right direction
        steps = 0

        while q:
            for _ in range(len(q)):
                #pop the first element from the queue
                #this is the current position we are at
                #we will check if this position is an exit
                #if yes, return the steps taken to reach this position
                #if no, continue to the next position in the queue
                cur_pos = q.popleft()
                #check if current position is an exit, which is at the border of the maze
                #and not the entrance
                if (cur_pos[0] in (0, rows-1) or cur_pos[1] in (0, cols-1)) and cur_pos != entrance:
                    #if yes, return the steps taken to reach this position
                    #since we are doing BFS, the first time we reach an exit is the shortest path
                    #so we can return the steps taken to reach this position
                    #steps is the number of moves taken to reach this position
                    return steps
                for move in moves:
                    #calculate next position
                    nx, ny = cur_pos[0] + move[0], cur_pos[1] + move[1]
                    #check if next position is within the maze and not a wall
                    #and not visited before
                    #if not, continue to the next move
                    #if yes, add to the queue
                    if 0 <= nx < rows and  0 <= ny < cols and maze[nx][ny] == '.' and (nx, ny) not in visited:
                        #add next position to the visited set and queue
                        visited.add((nx,ny))
                        q.append((nx, ny))
            steps += 1

        return -1  # if no exit found, return -1

if __name__ == "__main__":  
    
    sol = Solution()
    '''
    maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
    entrance = [1, 2]
    print(sol.nearestExit(maze, entrance))  # Output: 1

    maze2 = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
    entrance2 = [1, 0]
    print(sol.nearestExit(maze2, entrance2))  # Output: 2

    maze3 = [[".", "+"]]
    entrance3 = [0, 0]
    print(sol.nearestExit(maze3, entrance3))  # Output: -1
    '''

    maze4 = [["+",".","+","+","+","+","+"],
             ["+",".","+",".",".",".","+"],
             ["+",".","+",".","+",".","+"],
             ["+",".",".",".",".",".","+"],
             ["+","+","+","+",".","+","."]]
    entrance4 = [0, 1]
    print(sol.nearestExit(maze4, entrance4))  # Output: 7