'''
162. Find Peak Element

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
'''

from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        O(N) solution: go through the list and find any number that is greater than left and right
        O(logN)solution: 

        -inf 1 2 3 1 5 6 4 -inf
        '''
        def findPeak(left,right):
            if left == right:
                return left
            mid = left + (right - left)//2
             # Handle boundaries safely
            left_val = nums[mid - 1] if mid > 0 else float('-inf')
            right_val = nums[mid + 1] if mid < len(nums) - 1 else float('-inf')
            
            if nums[mid] > left_val and nums[mid] > right_val: #terminate early
                return mid
            if nums[mid] < right_val:
                return findPeak(mid + 1, right)
            else:
                return findPeak(left, mid)

        n = len(nums) #n = 7
        return findPeak(0,n-1)
if __name__ == "__main__":
    #nums = [1,2,3,1]  # Example input
    nums = [1,2,1,3,5,6,4]
    print(Solution().findPeakElement(nums))  # Example usage