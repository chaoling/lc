from typing import List


class Solution:
    '''
    27. Remove Element
    Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

    Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
    Return k.
    Custom Judge:

    The judge will test your solution with the following code:

    int[] nums = [...]; // Input array
    int val = ...; // Value to remove
    int[] expectedNums = [...]; // The expected answer with correct length.
                                // It is sorted with no values equaling val.

    int k = removeElement(nums, val); // Calls your implementation

    assert k == expectedNums.length;
    sort(nums, 0, k); // Sort the first k elements of nums
    for (int i = 0; i < actualLength; i++) {
        assert nums[i] == expectedNums[i];
    }
    If all assertions pass, then your solution will be accepted.

    

    Example 1:

    Input: nums = [3,2,2,3], val = 3
    Output: 2, nums = [2,2,_,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 2.
    It does not matter what you leave beyond the returned k (hence they are underscores).
    Example 2:

    Input: nums = [0,1,2,2,3,0,4,2], val = 2
    Output: 5, nums = [0,1,4,0,3,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
    Note that the five elements can be returned in any order.
    It does not matter what you leave beyond the returned k (hence they are underscores).

    Constraints:

    0 <= nums.length <= 100
    0 <= nums[i] <= 50
    0 <= val <= 100
    '''
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        use two pointers, left, right, if nums[left] == val: look for right, if nums[right] != val, exchange
        it with nums[left], then left++, otherwise right--, rince and repeat
        '''
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] != val:
                left += 1
            while left <= right and nums[right] == val:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left
      

        #another method
        def removeElement2(self, nums: List[int], val: int) -> int:
            insert_pos = 0
            for num in nums:
                if num != val:
                    nums[insert_pos] = num
                    insert_pos += 1
            return insert_pos

if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([3,2,2,3], 3))  # Output: 2
    print(s.removeElement([0,1,2,2,3,0,4,2], 2))  # Output: 5
    print(s.removeElement([], 0))  # Output: 0
    print(s.removeElement([1], 1))  # Output: 0
    print(s.removeElement([1], 2))  # Output: 1
    print(s.removeElement([1, 2, 3, 4, 5], 3))  # Output: 4
    print(s.removeElement([1, 2, 3, 4, 5], 6))  # Output: 5