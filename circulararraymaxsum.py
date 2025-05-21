from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        '''
        key: it is circular, so when your scan pointer is at the end of the regular array, 
        you still need to wrap around the array to the beginning until you've done all subarrays
        that only inlude each element of the fixed buffer nums at most once.
        aka, for i <= k1, k2 <= j , k1%n != k2%n 
        using Kadane's algorithm:
        The maximum circular subarray sum is either:

        the normal maximum subarray sum (no wrap)

        or the entire array sum minus the minimum subarray sum (wrap)
        '''
        total = nums[0]
        max_s = cur_max = nums[0]
        min_s = cur_min = nums[0]
        for num in nums[1:]:
            total += num
            cur_max = max(cur_max + num, num)
            cur_min = min(cur_min + num, num)
            max_s = max(max_s, cur_max)
            min_s = min(min_s, cur_min)
        
        if max_s < 0: # all numbers in nums are negative case
            return max_s
        else:
            return max(total - min_s, max_s)
        # Time complexity: O(n)
        # Space complexity: O(1)
if __name__ == "__main__":
    s = Solution()
    print(s.maxSubarraySumCircular([1,-2,3,-2])) # 3
    print(s.maxSubarraySumCircular([5,-3,5])) # 10
    print(s.maxSubarraySumCircular([-3,-2,-3])) # -2
    print(s.maxSubarraySumCircular([-1,-2,-3])) # -1
    print(s.maxSubarraySumCircular([1,2,3,4,5])) # 15