'''
2336. Smallest Number in Infinite Set
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
 

Example 1:

Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.
 

Constraints:

1 <= num <= 1000
At most 1000 calls will be made to popSmallest and addBack.
'''
import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.next_int = 1 # serve as generator, initially pretend you already have all int in your set, ready to pop the smallest 1st
        self.add_back = [] #it is a heap, when add back the elements to ensure smallest one is on top
        self.check = set() # to quickly look up what is inserted in the heap when adding back numbers into your container

    def popSmallest(self) -> int:
        if self.add_back:
            num = heapq.heappop(self.add_back)
            self.check.remove(num) #or use discard since no error raised if num does not exist.
           
        else:
            num = self.next_int
            self.next_int += 1
        
        #print(f"pop smallest element: {num=}")
        return num


    def addBack(self, num: int) -> None:
        #print(f"adding {num=} ...")
        # only numbers that have already been popped can be added back
        if num < self.next_int and num not in self.check: 
            heapq.heappush(self.add_back, num)
            self.check.add(num)

if __name__ == "__main__":
    obj = SmallestInfiniteSet()
    print(obj.popSmallest()) # return 1
    print(obj.popSmallest()) # return 2
    obj.addBack(1)           # 1 is added back to the set.
    print(obj.popSmallest()) # return 1, since 1 was added back
    print(obj.popSmallest()) # return 3
    obj.addBack(2)           # 2 is added back to the set.
    print(obj.popSmallest()) # return 2, since 2 was added back