'''
724. Find Pivot Index
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
 

Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
'''
from pyparsing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        Simulate asteroid collisions using a stack.
        Right-moving asteroids are pushed; left-moving ones may cause collisions.
        '''
        stk = []
        for asteroid in asteroids:
            while stk and asteroid < 0 < stk[-1]:
                if stk[-1] < -asteroid:
                    stk.pop() # Current asteroid destroys the top of the stack
                elif stk[-1] == -asteroid:
                    stk.pop()
                    break # Both asteroids are destroyed
                else:
                    break # Current asteroid is destroyed
            else:
                # No collision, push the asteroid onto the stack
                stk.append(asteroid)
        return stk

if __name__ == "__main__":
    s = Solution()
    print(s.asteroidCollision([5, 10, -5]))  # Output: [5, 10]
    print(s.asteroidCollision([8, -8]))  # Output: []
    print(s.asteroidCollision([10, 2, -5]))  # Output: [10]
    print(s.asteroidCollision([-2, -1, 1, 2]))  # Output: [-2, -1, 1, 2]
    print(s.asteroidCollision([1, -1, -2, -2]))  # Output: [-2, -2]
    print(s.asteroidCollision([-2, -2, 1, -1]))  # Output: [-2, -2]
    print(s.asteroidCollision([-2, -2, 1, 1]))  # Output: [-2, -2, 1, 1]
    print(s.asteroidCollision([-2, -2, 1, 3]))  # Output: [-2, -2, 1, 3]
    print(s.asteroidCollision([-2, -2, 3, -3]))  # Output: [-2, -2]
    print(s.asteroidCollision([-2, -2, 3, -4]))  # Output: [-4]
    print(s.asteroidCollision([-2, -2, 3, -5]))  # Output: [-5]
    print(s.asteroidCollision([-2, -2, 3, -1]))  # Output: [-2, -2]