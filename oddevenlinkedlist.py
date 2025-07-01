'''
LC 328 odd-even linked list
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        use two pointers, odd and even
        '''
        dummy = ListNode(0)
        if head:
            dummy.next = head.next
        odd = head
        even = dummy
        #(dummy)->(odd1)->(even1)->(odd2)->(even2)
        while odd and odd.next:
            even.next = odd.next
            odd.next = odd.next.next
            even.next.next = None
            if odd.next:
                odd = odd.next
            even = even.next
        if odd:
            odd.next = dummy.next
        return head

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    # Create a linked list 1->2->3->4->5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Reorder the linked list
    new_head = sol.oddEvenList(head)

    # Print the reordered linked list
    current = new_head
    while current:
        print(current.val, end=' ')
        current = current.next