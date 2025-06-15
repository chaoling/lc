'''
35. Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
'''
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        use binary search
        '''
        def bin_search(left, right):
            if left > right:
                return left
            mid = left + (right-left) // 2
            if target ==  nums[mid]:
                return mid
            elif target < nums[mid]:
                return bin_search(left, mid - 1)
            else:
                return bin_search(mid+1, right)

        return bin_search(0, len(nums)-1)
    
    def searchInsert_iter(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left

if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1,3,5,6], 5))
    print(s.searchInsert([1,3,5,6], 2))
    print(s.searchInsert([1,3,5,6], 7))
    print(s.searchInsert([1,3,5,6], 0))
    print(s.searchInsert([1], 0))