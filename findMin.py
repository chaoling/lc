'''
153. Find Minimum in Rotated Sorted Array
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
'''
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        before rotation: just output nums[0]
        after rotation: output nums[s%n]
        where n = len(nums)

        alg: got mid of the array, if nums[mid] is peak, then next item is min
        if nums[mid-1]<nums[mid]<nums[mid+1], then find the lower half, vise vesa
        '''
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] > nums[right]:
                # min must be in right half, excluding mid:
                left = mid + 1
            else:
                #min is at mid or in left half
                right = mid
        #left will point to min
        return nums[left]
if __name__ == '__main__':
    s = Solution()
    print(s.findMin([3, 4, 5, 1, 2]))  # Output: 1
    print(s.findMin([4, 5, 6, 7, 0, 1, 2]))  # Output: 0
    print(s.findMin([11, 13, 15, 17]))  # Output: 11
    print(s.findMin([2, 1]))  # Output: 1
    print(s.findMin([1]))  # Output: 1