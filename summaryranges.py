'''
228. Summary Ranges

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 

Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.
'''
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        '''
        find range that contains consequetive numbers 
        '''
        res = []
        if not nums:
            return res
        left = nums[0]
        right = left
        for num in nums[1:]:
            if num == right + 1:
                right += 1
            else:
                #found the right boundary
                if right != left:
                    res.append(f"{left}->{right}")
                else:
                    res.append(f"{left}")
                left,right = num, num
        #check the last interval case:
        if right != left:
            res.append(f"{left}->{right}")
        else:
            res.append(f"{left}")

        return res
if __name__ == "__main__":
    s = Solution()
    print(s.summaryRanges([0,1,2,4,5,7])) # ["0->2","4->5","7"]
    print(s.summaryRanges([0,2,3,4,6,8,9])) # ["0","2->4","6","8->9"]
    print(s.summaryRanges([])) # []
    print(s.summaryRanges([1])) # ["1"]
    print(s.summaryRanges([1,2])) # ["1->2"]
    print(s.summaryRanges([1,3])) # ["1","3"]