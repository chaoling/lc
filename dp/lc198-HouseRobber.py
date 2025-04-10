'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
'''
from typing import List

def rob(nums: List[int]) -> int:
    '''
    1D dp problem:
    you can not visit the neighbor house in the same night
    at any point, dp[i], you have two choices: rob it or not rob it,
    suppose it is the current optimum, you can only visit dp[i+2] if you rob the current house
    you can visit dp[i+1] if you choose not to rob the current house
    dp [i] = max(dp[i-1], dp[i-2] + nums[i])
    Because “rob only the even indexed houses” and “rob only the odd indexed houses” 
    cover just two of the many legal ways to pick non‑adjacent houses, and neither one is guaranteed to contain the optimum.
    index : 0   1   2   3
    money : 2   1   1   2
    Even indices (0 & 2) -> 2 + 1 = 3

    Odd indices (1 & 3) -> 1 + 2 = 3

    Best choice (0 & 3) → 2 + 2 = 4 ✅
    '''
    
    n = len(nums) #get the number of houses to rob

    if n < 2:
        return sum(nums)
    prev2, prev1 = nums[0], max(nums[0], nums[1])
    for i in range(2, n):
        prev2, prev1 = prev1, max(prev1, prev2 + nums[i])
       
    return prev1