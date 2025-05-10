from typing import List

'''
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''
class Solution:
    def threeSumMyFun(self, nums: List[int]) -> List[List[int]]:
        def twoSum(target: int, nums: List[int], skip_index: int) -> List[List[int]]:
            num_to_index = {}
            ans = set()
            for i, num in enumerate(nums):
                if i == skip_index:
                    continue
                complement = target - num
                if complement in num_to_index and num_to_index[complement] != skip_index:
                    ans.add(tuple(sorted((num, complement))))
                num_to_index[num] = i
            return [list(pair) for pair in ans]

        res = set()
        nums.sort()
        for i, fixed in enumerate(nums):
            pairs = twoSum(-fixed, nums, i)
            for pair in pairs:
                triplet = tuple(sorted(pair + [fixed]))
                res.add(triplet)

        return [list(triplet) for triplet in res]

    from typing import List

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # sort to handle duplicates and ensure order
        n = len(nums)
        res = set()

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # skip duplicate fixed numbers
            target = -nums[i]
            seen = set()
            for j in range(i + 1, n):
                complement = target - nums[j]
                if complement in seen:
                    res.add((nums[i], complement, nums[j]))
                seen.add(nums[j])

        return [list(triplet) for triplet in res]

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))  # Example input
    print(sol.threeSumMyFun([-1, 0, 1, 2, -1, -4]))  # Example input