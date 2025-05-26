'''
82. Remove Duplicates from Sorted List II
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

similar to the problem:
remove-duplicates-from-an-unsorted-linked-list

'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        use a dummy nodes for ease of formality
        (dummy)->(head)->(next)->(next)->....->(tail)->(null)
        pre->(dummy), cur->(head)
        '''
        if not head:
            return None
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        cur = head
      
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            
            if pre.next != cur: #found duplicate
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next

        return dummy.next