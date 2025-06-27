'''
1679. Max Number of K-Sum Pairs
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
'''
from collections import defaultdict
from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        '''
        array is not sorted, use a hash table?
        interate the array, if nums[i] not in hash table,
        put it in with key: k - nums[i], value: i
        if you found nums[i] in the hash table, remove it,
        count += 1
        '''
        freq = defaultdict(int)
        count = 0
        for num in nums:
            complement = k - num
            if freq[complement] > 0:
                freq[complement] -= 1
                count +=1
            else:
                freq[num] += 1   #for future complement to pair
        return count

if __name__ == "__main__":
    nums = [1,2,3,4]
    k = 5
    print(Solution().maxOperations(nums, k))  # Output: 2
    nums = [3,1,3,4,3]
    k = 6
    print(Solution().maxOperations(nums, k))  # Output: 1
    nums = [1,2,3,4,5]
    k = 7
    print(Solution().maxOperations(nums, k))  # Output: 3