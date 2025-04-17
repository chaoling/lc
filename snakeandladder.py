'''
909. Snakes and Ladders
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.
'''
from typing import List

def snakesAndLadders(board: List[List[int]]) -> int:
        from collections import deque
        '''
        explore all directions, each level has max 6 possible moves,
        do a BFS until you hit the n^2 destination
        '''
        def num_to_coord(num: int, n: int) -> (int, int):
            # convert destination to coord, n is the side len of square
            # 1-based num → (r,c) in board
            r_idx_from_bottom = (num - 1) // n
            row = n - 1 - r_idx_from_bottom         # flip to 0‑indexed top‑based
            offset = (num - 1) % n
            # even-numbered strips (0,2,4,… from bottom) go left→right
            if r_idx_from_bottom % 2 == 0:
                col = offset
            else:
                col = n - 1 - offset
            return row, col

                    

        n = len(board)
        if n == 1:
            return 0
        
        visited = [False]*(n*n+1)
        visited[1] = True
        q = deque([(1,0)]) #initially, start with 1, level 0
        while q:
            cur, moves = q.popleft()
            for nxt in range(cur+1, min(cur+6, n*n) + 1):
                r, c = num_to_coord(nxt,n)
                dest = board[r][c] if board[r][c] != -1 else nxt
                if dest == n*n:
                    return moves + 1
                if not visited[dest]:
                    visited[dest] = True
                    q.append((dest, moves + 1))
        return -1
