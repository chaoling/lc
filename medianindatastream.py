'''
295. Find Median from Data Stream
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
'''
from heapq import heappop, heappush
class MedianFinder:
    
    def __init__(self):
        self.pq_min = []
        self.pq_max = []
        

    def addNum(self, num: int) -> None:
        if not self.pq_min or num >= self.pq_min[0]:
            heappush(self.pq_min, num)
        else:
            heappush(self.pq_max, -num) # max heap by pushing negative values
        
        # balance the two heaps
        if len(self.pq_min) > len(self.pq_max) + 1:
            heappush(self.pq_max, -heappop(self.pq_min))
        elif len(self.pq_max) > len(self.pq_min) + 1:
            heappush(self.pq_min, -heappop(self.pq_max))

    def findMedian(self) -> float:
        if len(self.pq_min) > len(self.pq_max):
            return float(self.pq_min[0])
        elif len(self.pq_max) > len(self.pq_min):
            return float(-self.pq_max[0])
        else:
            return (self.pq_min[0] - self.pq_max[0]) / 2
            
if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian()) # 1.5
    mf.addNum(3)
    print(mf.findMedian()) # 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
'''
If 99% of numbers are in [0, 100], but some are outside
👉 You can combine both strategies:

Use the count array [0..100] for numbers in the range.

Use two heaps for numbers < 0 and > 100.
'''