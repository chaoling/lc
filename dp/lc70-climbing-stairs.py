'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
'''
def climbStairs(n: int) -> int:
    '''
        this is a dp problem:
        1D array of solution
        dp[1] = 1 # only one step to reach the top
        dp[2] = 2 # 1 step + 1 step or 2 steps 
        dp[3] = 3 # dp[1] + dp [2] = 1 + 2
        Think of each “state” i (standing on the i-th step) as a goal you can reach in one of two mutually-exclusive ways:

        come from step i-1 and take one step, or
        come from step i-2 and take two steps.

        Because these two source states do not overlap (you can't be on both steps at once), the total number of distinct paths to i is the union of the two sets of paths.
    '''
    pre, cur = 1, 2
    for i in range(3,n+1):
        #dp.append(dp[i-1] + dp[i-2])
        pre, cur = cur, pre + cur
    return cur

if __name__ == "__main__":
    for i in range(2,46):
        print(f"solution for {i} stairs: ",climbStairs(i))