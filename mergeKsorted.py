'''
23. Merge k Sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
'''
# Definition for singly-linked list.

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        take the 1st element of each list, put them in a min-heap/priority queue
        then take the element in the order it was saved in the min-heap,
        one at a time, and merge them together
        '''
        from heapq import heappush, heappop
        pq = []
        # Initialize heap with the first node of each list
        for node in lists:
            if node:
                heappush(pq, (node.val, id(node), node))
        dummy = ListNode(0)
        current = dummy
        while pq:
            _,_,node = heappop(pq)
            current.next = node
            current = current.next
            if node.next:
                heappush(pq, (node.next.val, id(node.next), node.next))
        return dummy.next

if __name__ == "__main__":  
    # Example usage:
    # Creating linked lists for testing
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))
    
    lists = [list1, list2, list3]
    
    solution = Solution()
    merged_list = solution.mergeKLists(lists)
    
    # Print the merged linked list
    current = merged_list
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")