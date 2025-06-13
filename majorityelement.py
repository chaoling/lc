'''
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
'''
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''

        '''
        from collections import Counter
        d = Counter(nums)
        for num, count in d.items():
            if count > len(nums) // 2:
                return num
        return -1
        # Moore Voting Algorithm
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
        # Bit Manipulation
        n = len(nums)
        majority = 0
        for i in range(32):
            bit_count = 0
            for num in nums:
                if (num >> i) & 1:
                    bit_count += 1
            if bit_count > n // 2:
                majority |= (1 << i)
        if majority >= 2**31:
            majority -= 2**32
        return majority
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3,2,3]))
    print(s.majorityElement([2,2,1,1,1,2,2]))