'''
1004. Max Consecutive Ones III
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        sliding windows, inside the window, make sure the number of 0s will be less or equal to k
        otherwise, 
        '''
        n = len(nums)
        max_len, cur_len = 0, 0
        flip = k
        left, right = 0, 0
        while right < n:
            if nums[right] == 1:
                right += 1
                cur_len += 1
            elif flip > 0:
                flip -= 1
                right += 1
                cur_len += 1
            else: #running window can not hold consequtive 1s anymore, have to shrink window from left
                if nums[left] == 1:
                    cur_len -= 1
                else:
                    cur_len -= 1
                    flip += 1
                left += 1    
            #update the max len
            max_len = max(max_len, cur_len)
        return max_len
    
    def longestOnes2(self, nums: List[int], k: int) -> int:
        '''
        sliding windows, inside the window, make sure the number of 0s will be less or equal to k
        otherwise, 
        '''
        n = len(nums)
        max_len = 0
        left = 0
        for right in range(n):
            if nums[right] == 0:
                k -= 1
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len

if __name__ == "__main__":
    s = Solution()
    print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)) #6
    print(s.longestOnes([0,0,1,1,0,0,1,1,1,0], 3)) #10
    print(s.longestOnes([1,1,1,1], 0)) #4
    print(s.longestOnes([0,0,0,1], 4)) #4  