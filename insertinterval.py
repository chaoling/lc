'''
57. Insert Interval
Medium

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
'''

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        do merge as we did on last question, 1st we need to find a starting position to do so for newInterval
        '''
        merged = []
        s, e = newInterval
        done = False
        for interval in intervals:
            # Case 1: New interval is completely before current interval
            if e < interval[0]:
                if not done:
                    merged.append([s,e])
                    done = True
                merged.append(interval)
            # Case 2: New interval is completely after current interval
            elif s > interval[1]:
                merged.append(interval)
            # Case 3: New interval overlaps with current interval
            elif interval[0] <= e <= interval[1] or interval[0] <= s <= interval[1]:
                s, e = min(s, interval[0]), max(e, interval[1])
        if not done:
            merged.append([s,e])
        return merged
     
if __name__ == "__main__":
    s = Solution()
    print(s.insert([[1,3],[6,9]], [2,5])) # [[1,5],[6,9]]
    print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])) # [[1,2],[3,10],[12,16]]
    print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [0,0])) # [[0,0],[1,2],[3,5],[6,7],[8,10],[12,16]]
