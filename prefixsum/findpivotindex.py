'''
724. Find Pivot Index
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
 

Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
'''
from pyparsing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums) # O(N)
        sum_left = 0
        sum_right = total - sum_left - nums[0]
        if sum_left == sum_right:
            return 0
        for i in range(1,n):  #O(N)
            sum_left += nums[i-1]
            sum_right = total - sum_left - nums[i]
            if sum_left == sum_right:
                return i
        return -1
    
    def pivotIndex2(self, nums: List[int]) -> int:
        """
        use prefix sum to calculate the left sum and right sum at each index
        """
        n = len(nums)
        prefix_sum = [0] * (n+1) # prefix_sum[i] is the sum of nums[0:i-1], i starts from 1
        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1] # O(N)
        
        for i in range(n):
            sum_left = prefix_sum[i]
            sum_right = prefix_sum[n] - prefix_sum[i+1] # total - sum_left - nums[i]
            if sum_left == sum_right:
                return i
        return -1
    
if __name__ == "__main__":  
    s = Solution()
    print(s.pivotIndex([1,7,3,6,5,6]))  # Output: 3
    print(s.pivotIndex([1,2,3]))  # Output: -1
    print(s.pivotIndex([2,1,-1]))  # Output: 0
    print(s.pivotIndex([-1,-1,-1,0,1,1]))  # Output: 0
    print(s.pivotIndex([-1,-1,-1,-1,-1,0]))  # Output: -1
    print(s.pivotIndex([-1,-1,-1,-1,0,-1]))  # Output: -1
    print(s.pivotIndex([0,0,0,0]))  # Output: 0
    print(s.pivotIndex([0,0,0,1]))  # Output: 2
    print(s.pivotIndex([1,0,0,0]))  # Output: 3
    print(s.pivotIndex([1]))  # Output: 0
    print(s.pivotIndex([1,2]))  # Output: -1
    print(s.pivotIndex([2,1]))  # Output: -1