from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        observation: we can rotate the array by k steps to the right
        O(N) time complexity, O(1) space complexity
        where N is the length of the array.
        We can do this by moving the last k elements to the front and shifting the rest of the elements to the right.
        This can be done in-place by using a temporary variable to hold the last element and shifting the rest of the elements.
        Alternatively, we can use slicing to achieve the same result.
        This method is in-place and has O(n) time complexity.
        We can also use the reverse method to achieve the same result.
        1. Reverse the entire array.
        2. Reverse the first k elements.
        3. Reverse the remaining n-k elements.
        4. This method is also in-place and has O(n) time complexity.
        example:
        Input: nums = [1,2,3,4,5,6,7], k = 3
        Output: [5,6,7,1,2,3,4]
        """
        n = len(nums)
        k = k % n
        for i in range(k):
            tmp = nums[-1]
            for j in range(n-1,0,-1):
            # nums[j] -> nums[(j+1)%n] move everyone 1 step to the right
                nums[j] = nums[j-1]
            nums[0] = tmp

        # Alternatively, we can use slicing
    def rotate1(self, nums: List[int], k: int) -> None: 
        #O(N) time complexity, O(N) space complexity
        nums[:] = nums[-k:] + nums[:-k]
        # This is more efficient and concise, but the above method is in-place as required.
    
    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Another approach using reverse.
        """
        #O(N) time complexity, O(1) space complexity
        n = len(nums)
        k = k % n
        
        # Reverse the entire array
        nums.reverse()
        
        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])
        
        # Reverse the remaining n-k elements
        nums[k:] = reversed(nums[k:])
        # This method is also in-place and has O(n) time complexity.

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    sol.rotate(nums, k)
    print(nums)  # Output should be [5, 6, 7, 1, 2, 3, 4]