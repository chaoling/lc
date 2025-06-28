'''
1493. Longest Subarray of 1's After Deleting One Element
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        use sliding window methods
        '''
        ans = 0
        n = len(nums)
        left = 0
        flips_remaining = 1
        for right in range(n):
            if nums[right] == 0:
                #do not actually delete 1, flip it to 1 and decrement deletion ops
                flips_remaining -= 1
            while flips_remaining < 0:
                if nums[left] == 0:
                    flips_remaining += 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans - 1

if __name__ == "__main__":
    s = Solution()
    print(s.longestSubarray([1,1,0,1]))  # Output: 3
    print(s.longestSubarray([0,1,1,1,0,1,1,0,1]))  # Output: 5
    print(s.longestSubarray([1,1,1]))  # Output: 2
    print(s.longestSubarray([1,1,0,0,1,1,1,0,1]))  # Output: 4
    print(s.longestSubarray([0,0,0]))  # Output: 0