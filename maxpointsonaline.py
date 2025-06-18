'''
https://leetcode.com/problems/max-points-on-a-line/
149. Max Points on a Line
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
Example 1:

Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
 
Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
'''
from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        '''
        for each pair of points on the plane, we have a line
        and we can count number of points falls on that line
        pick the line that cross max number of points
        how to decide if three points align on a line?
        [x0,y0],[x1,y1],[x2,y2] are on a line iff
        (y1-y0)/(x1-x0) == (y2-y1)/(x2-x1) #we need to avoid floating point division
        ==> (y1 - y0) * (x2 - x1) == (y2 - y1) * (x1 - x0)
        can you tell how many points are not on that line
        or on left half plane vs right half plan about that line?
        use a hashmap to count how many lines pass though the same anchor point with different slopes: key: reduced slope (dy, dx) tuple
        value: number of points sharing that slope with anchor
        hint: use [dx//gcd(dy,dx), dy//gcd(dx,dy)] to represent the common slope
        
        '''
        from math import gcd

        result = 0
        n = len(points)
        for i in range(n):
            slopes = {}
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]    
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    dy = abs(dy)
                slopes[(dx, dy)] = slopes.get((dx, dy), 0) + 1  
            result = max(result, max(slopes.values(), default=0) + 1)  # +1 for the anchor point itself
        return result

if __name__ == "__main__":
    points = [[1,1],[2,2],[3,3]]
    print(Solution().maxPoints(points))  # Output: 3
    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    print(Solution().maxPoints(points))  # Output: 4
                   