from typing import List

def combine(n: int, k: int) -> List[List[int]]:
        '''
        use dfs with backtracking to generate these sets,
        iterate over range of integers 1-n, every time bfs depth is
        k levels, and return and backtrack
        '''
        res = []

        def dfs(start: int, path: List[int]):
            if len(path) == k:
                res.append(path[:])
                return 
            
            # Only loop until a point where there are enough remaining numbers
            # If len(path) + (n - i + 1) < k, it's impossible to complete the combination, so we can skip.
            for i in range(start, n-(k-len(path))+2):
                    path.append(i)
                    dfs(i+1, path)
                    path.pop() #back tracking

        dfs(1,[])

        return res

if __name__ == "__main__":
     print(combine(n= 4, k=2))