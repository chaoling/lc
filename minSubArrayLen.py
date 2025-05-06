class Solution:
    '''
    209. Minimum Size Subarray Sum
    Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
    A subarray is a contiguous part of an array. 

    Example 1:

    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem constraint.
    Example 2:

    Input: target = 4, nums = [1,4,4]
    Output: 1
    Example 3:

    Input: target = 11, nums = [1,1,1,1,1,1,1,1]
    Output: 0
    '''
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        can we sort it first? no...
        can we just use windows to scan the array and return if found the target sum? O(N^3)?
        use a sliding window to find the minimum length of subarray
        that has a sum greater than or equal to target.
        1. use two pointers, left and right, to represent the current window
        2. move the right pointer to expand the window and add the current element to the total
        3. if the total is greater than or equal to target, update the minimum length
        4. move the left pointer to shrink the window and subtract the current element from the total
        5. repeat steps 2-4 until the right pointer reaches the end of the array
        6. return the minimum length found, or 0 if no such subarray exists
        '''
        n = len(nums)
        left, right = 0, 0
        min_len = float('inf')
        total = 0
        while right < n:
            total += nums[right]
            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        return min_len if min_len != float('inf') else 0