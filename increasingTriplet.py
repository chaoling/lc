'''
334. Increasing Triplet Subsequence
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
'''
from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        visually, this problem is equivalent to picking at least 
        three points in the 2D plane that has an upward trend line
        so we can look at peaks and valleys,
        if at least three data points between a valley and a peak, 

        naive solution: for each number in the list, find rest of the number that has
        at least 2 number that is greater than it
        '''
        n = len(nums)
        for i in range(n):
            count = [nums[i]]
            for j in range(i+1 , n): 
                if nums[j] > nums[i]:
                    if nums[j] <= count[-1]:
                        count[-1] = nums[j] #replace with smaller candidates
                    else:
                        count.append(nums[j])
                if len(count) >= 3:
                    return True
        return False

    def increasingTripletOptimized(self, nums: List[int]) -> bool:
        '''
        optimized solution: use two variables to keep track of the first and second number
        in the triplet, if we find a number that is greater than the second number, then we have
        found a triplet
        '''
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
    
if __name__ == "__main__":
    s = Solution()
    print(s.increasingTriplet([1,2,3,4,5]))  # True
    print(s.increasingTriplet([5,4,3,2,1]))  # False
    print(s.increasingTriplet([2,1,5,0,4,6]))  # True
    print(s.increasingTriplet([20,100,10,12,5]))  # False