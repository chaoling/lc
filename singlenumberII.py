'''
137. Single Number II
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
 

Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        For each bit position (0..31), count how many times that bit is set across all numbers.

        If a bit appears 3 * k + 1 times, that bit belongs to the unique number.
        '''
        res = 0
        for i in range(32):
            count = 0
            for num in nums:
                if num >> i & 1:
                    count += 1
            if count % 3:
                res |= 1 << i
        # Handle negative numbers
        if res >= 2**31:
            res -= 2**32
        return res