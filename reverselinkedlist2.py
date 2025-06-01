'''
92. Reverse Linked List II
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
 
Follow up: Could you do it in one pass?
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''
        we can do normal linked list, with a small tweek: aka, only starts when the value is left, and end when value is right, don't forget connect the before left and after right together at the end.
        '''
        if not head or not head.next:
            return head
        dummy = ListNode()
        dummy.next = head
        pre, cur = dummy, head
        pos = 1
        while cur:
            if pos < left or pos > right:
                pre = pre.next
                cur = cur.next
                pos += 1
            else:
                #start reverse the list nodes
                # save the pre
                start_head, start_cur = pre, cur #adjust its next when we are done with reverse
                while cur and pos <= right:
                    tmp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = tmp
                    pos += 1
                #connect the new list 
                start_head.next = pre
                start_cur.next = cur
                pre=start_cur
                
        return dummy.next

if __name__ == "__main__":
    # Example usage
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    left = 2
    right = 4
    solution = Solution()
    new_head = solution.reverseBetween(head, left, right)
    
    # Print the reversed list
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")