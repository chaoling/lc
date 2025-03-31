'''
167. Two Sum II - Input Array Is Sorted
Medium

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
'''

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    '''
    sorted: use binary search to find another number that is equal to target - 1st number ... o(n*log(n))
    can we do o(n) ?
    [1, 3, 4, 7, 10, 12, 14, 21 ] -> target is 14
    use two pointers, search from opposite direction until they meet or cross each other, then no solution
    pay attention to index start at 1
    O(N) time and space complexity! 
    runtime: 3ms beats 81.68% solutions submitted!
    '''
    assert len(numbers) >=2 , "at least two numbers needed for this problem!"
    lp, rp = 1, len(numbers) #but python's list index starts at 0, so we must subtract by 1 when access list items
    while lp <= rp:
        cur_num = numbers[lp-1]
        other_num = target - cur_num
        #look for the other number, move the right pointer towards left until it either find the other_num or less than that 
        while numbers[rp-1] > other_num:
            rp -= 1
        if rp > lp and numbers[rp-1] == other_num:
            #found it!
            return [lp, rp]
        elif rp <= lp:
            #no solution!
            return []
        else:
            lp += 1
    
    else:
        return [] #no solution
    

        
