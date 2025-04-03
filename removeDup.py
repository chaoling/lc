'''
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.
'''
from typing import List


def removeDuplicates(nums: List[int]) -> int:
    '''
    nums are sorted in non-decending order...
    [1,1,2,2,2,3,3,4,5,6,6,6...]
    have a pointer to the 1st element in the array,
    move pointer forward: if next num is not the same, keep moving
    if the next num is the same, counter++, if counter <=2, keep moving
    else delete this num, keep moving,
    if next number is the same, counter++, else, counter = 0
    '''
    cnt, index = 1, 0
    k = len(nums)
    for index, num in enumerate(nums):
        if index == 0:
            continue
        elif num == nums[index-cnt]:
            cnt += 1
            if cnt > 2:
                #delete this num and move on by mark this num as invalid num 10**5
                nums[index] = 10**5
                k -= 1
                
        else: #num != nums[index-1]
            cnt = 1 # a new number found

    # now we have an array like this: [1,1,2,2,_,_,3,3,4,5,6,6,_]
    # finally, do one more interation to move all numbers to first k places
    new_index = 0
    for i in range(len(nums)):
        if nums[i] < 10**5:
            nums[new_index] = nums[i]
            new_index += 1
    
    return k


def removeDuplicates2(nums: List[int]) -> int:
    '''
    using two pointers
    fast pointer[i]
    slow pointer[j] is two place behind i
    '''
    #edge case: array has only 2 elements
    if len(nums) <= 2:
        return len(nums)
    
    # slow pointer i, the first two elements are always valid
    i = 2

    # use fast pointer (j) to iterate through the list starting from index 2
    for j in range(2, len(nums)):
        if nums[j] != nums[i-2]:
            nums[i] = nums[j]
            i += 1 #keep moving the slow pointer i
    
    return i 



if __name__ == '__main__':
    arr = [1,1,2,2,2,3,3,4,5,6,6,6]
    new_length = removeDuplicates(arr)
    arr2 = [0,0,1,1,1,1,2,3,3]
    new_length2 = removeDuplicates2(arr2)
    print("New length:", new_length)
    print("Modified array:", arr[:new_length])
    print("New length:", new_length2)
    print("Modified array:", arr2[:new_length2])

