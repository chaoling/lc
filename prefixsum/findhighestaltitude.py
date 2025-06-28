'''
1732. Find the Highest Altitude
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
 

Constraints:

n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100
Time: O(N)
Space: O(1)
'''
from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans, altitude = 0, 0
        for num in gain:
            altitude += num
            ans = max(ans, altitude)
        return ans
    
    def largestAltitude2(self, gain: List[int]) -> int:
        """
        use prefix sum to calculate the altitude at each point
        """
        prefix_sum = [0] # starting altitude is 0
        for g in gain:
            prefix_sum.append(prefix_sum[-1] + g)
        return max(prefix_sum)
        

if __name__ == "__main__":
    s = Solution()
    print(s.largestAltitude([-5, 1, 5, 0, -7]))  # Output: 1
    print(s.largestAltitude([-4, -3, -2, -1, 4, 3, 2]))  # Output: 0
    print(s.largestAltitude([1, 2, 3, 4, 5]))  # Output: 15
    print(s.largestAltitude([-1, -2, -3, -4, -5]))  # Output: 0
    print(s.largestAltitude([0, 0, 0, 0])) # Output: 0