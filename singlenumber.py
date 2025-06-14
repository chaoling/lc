'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
Example 1:
Input: nums = [4,1,2,1,2]
Output: 4
Example 2:
Input: nums = [2,2,1]
Output: 1
Constraints:
1 <= nums.length <= 3 * 10^4
0 <= nums[i] <= 3 * 10^4
Each element in the array appears twice except for one element which appears only once.
'''

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for num in nums[1:]:
            res ^= num
        return res

if __name__ == "__main__":
    s = Solution()
    nums = [4,1,2,1,2]
    print(s.singleNumber(nums)) # 4
    nums = [2,2,1]
    print(s.singleNumber(nums)) # 1