'''
56. Merge Intervals
Medium
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''
from typing import List
class Solution:
    def merge_mysol(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        1) are these intervals sorted by the start position in ascending order? if not, can we sort it first? or do we need to sort?
        2) given si, ei, check si+1 see if si+1 <= ei, then merged these two intervals to si->ei+1, if not, then move on to next interval, then rince and repeat?
        3) pitfall: interval start == end case, also there might be same intervals /redundant intervals
        '''
        intervals.sort(key=lambda x: x[0])
        start, end = intervals[0]
        res = []
        for interval in intervals[1:]:
            s, e = interval
            if s > end:
                res.append([start, end])
                start, end = s, e # move on to next interval
            else:
                end = max(end, e) # merge
        res.append([start, end])
        return res
    
    def merge(intervals):
        # Step 1: Sort intervals by the starting time
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        for interval in intervals:
            # If merged is empty or no overlap, append the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlapping intervals, so merge them
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]
    print(s.merge([[1,4],[4,5]])) # [[1,5]]
    print(s.merge([[1,4],[2,3]])) # [[1,4]]
    print(s.merge([[1,4],[0,2],[3,5]])) # [[0,5]]
    print(s.merge([[1,4],[0,2],[3,5],[6,7]])) # [[0,5],[6,7]]