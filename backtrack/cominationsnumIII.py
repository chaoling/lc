'''
216. Combination Sum III
Medium
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
 

Constraints:

2 <= k <= 9
1 <= n <= 60
'''
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        '''
        pick 1-9 each round, for k rounds, keep combos that adds up to n
        use recursive function and backtrack
        '''
        ans = []
        def combo(start: int, path:List[int], total: int):
            if len(path) == k:
                if total == n:
                    ans.append(path[:])
                    return
            else:
                for num in range(start, 10):
                    if total + num > n:
                        break
                    else:
                        path.append(num)
                        combo(num+1, path, total+num)
                        path.pop()
        combo(1,[],0)
        return ans

if __name__ == '__main__':
    #test cases
    test = [
        [3,7],
        [3,9],
        [4,1],
        [3,2],
        [3,15],
    ]
    for k,n in test:
        print(f'k={k}, n={n} => {Solution().combinationSum3(k,n)}')