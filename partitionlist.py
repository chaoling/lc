'''
86. Partition List
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
'''
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
from typing import Optional
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        '''
        algorithm: scan the linked list, for each node in the list, if the value is less than or equal to x, then move on to next node
        otherwise, this node needs to be moved later, 
        if no in place is required, can have two bucket list, one store nodes that is less or equal to x, one store nodes that is more than x, then merge them together
        '''
        before_head = ListNode(0)  # Dummy node for the "before" list
        before = before_head  # Pointer for the "before" list
        after_head = ListNode(0)
        after = after_head  # Pointer for the "after" list
        current = head
        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next
        after.next = None  # Terminate the "after" list
        before.next = after_head.next
        return before_head.next  # Return the head of the "before" list, which is the partitioned list  
    
    def my_partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        '''
        algorithm: scan the linked list, for each node in the list, if the value if less than or equal to x, then move on to next node
        otherwise, this node needs to be moved later, 
        if no in place is required, can have two bucket list, one store nodes that is less or equal to x, one store nodes that is more than x, then merge them together
        '''
        if not head or not head.next: #deal with 0 or 1 node only
            return head
        dummy = ListNode()
        dummy.next = head
        pre, cur = dummy, head
        right = ListNode()
        tmp = right
        while cur:
            if cur.val >= x:
                #move it after right dummy node
                tmp.next = cur
                pre.next = cur.next
                cur.next = None
                tmp = tmp.next
                cur = pre.next
            else:
                pre = cur
                cur = cur.next

        #now do the merge
        pre.next = right.next
        return dummy.next if dummy.next else right.next  # return the head of the partitioned list, or the right list if no left part exists

if __name__ == "__main__":
    # Example usage
    head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
    x = 3
    solution = Solution()
    new_head = solution.partition(head, x)
    
    # Print the partitioned list
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
# Output: 1 -> 2 -> 2 -> 4 -> 3 -> 5 -> None
    head = ListNode(1, ListNode(1))
    x = 0
    solution = Solution()
    new_head = solution.partition(head, x)
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")