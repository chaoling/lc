'''
283. Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
'''
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        hint: use 2 pointers
        one just iterate the list 
        the second iterate only the none-zero element of the list
        zero_pos always points to the next position where a non-zero element should go.
        It doesn’t necessarily track where the next zero is.
        Instead, it represents the boundary between the processed non-zero elements and the remaining portion of the array.
        """
        
        zero_pos, n = 0, len(nums)
        for i in range(n):
            if nums[i] != 0:
                if i != zero_pos:
                    nums[zero_pos] = nums[i] #swap
                    nums[i] = 0
                zero_pos += 1

if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    print(nums)  # Output: [1, 3, 12, 0, 0]
    nums = [0, 0, 1]
    Solution().moveZeroes(nums)