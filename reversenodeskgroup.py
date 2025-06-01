'''
25. Reverse Nodes in k-Group
https://leetcode.com/problems/reverse-nodes-in-k-group/
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 
Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_segment(start: Optional[ListNode], end: Optional[ListNode]) -> Optional[ListNode]:
            """
            Reverse the linked list from 'start' to 'end' inclusive.
            Returns the new head of the reversed segment.
            """
            if not start or not end:
                return start

            prev = end.next  # Store the node after the segment
            curr = start
            stop = end.next  # Avoid accessing end.next after mutation

            while curr != stop:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp

            return prev  # New head of the reversed segment

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Find the k-th node
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # Less than k nodes left

            group_next = kth.next
            start = group_prev.next

            # Reverse current k-group
            new_head = reverse_segment(start, kth)

            # Reconnect reversed group with the rest of the list
            group_prev.next = new_head
            start.next = group_next

            # Move group_prev to the end of the reversed group
            group_prev = start

            
    def my_reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        algorithm: only reverse the subgroup if it is a muliple of k
        use a dummy head
        '''
        def reverseList(head: Optional[ListNode], tail: Optional[ListNode]):
            '''
            1->2->3->(4) ==> 3->2->1->(4)
            '''
            if tail:
                pre, cur = tail.next, head
            else:
                pre, cur = None, head
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
                if tail and pre == tail:
                    break
            return pre

        if k == 1: #this problem is reduced to just simply reverse every node in the linked list
            return head #reverseList(head=head, tail=None)
        
        dummy = ListNode(val=-1, next=head)
        pre, cur, tail = dummy, head, head
        pos = 1
        while tail:
            # check subgroup is formed
            if pos % k == 0:
                new_head = reverseList(cur,tail)
                pre.next = new_head
                pre = cur
                cur, tail = pre.next, pre.next
                pos = 1 #reset pos to 1, a new start
            else:
                tail = tail.next
                pos += 1
        return dummy.next

if __name__ == "__main__":
    # Example usage
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    k = 2
    solution = Solution()
    new_head = solution.reverseKGroup(head, k)
    
    # Print the modified list
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
# Output: 2 -> 1 -> 4 -> 3 -> 5 -> None
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    k = 3
    solution = Solution()
    new_head = solution.reverseKGroup(head, k)
    
    # Print the modified list
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
# Output: 3 -> 2 -> 1 -> 4 -> 5 -> None
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    k = 1
    solution = Solution()
    new_head = solution.reverseKGroup(head, k)
    
    # Print the modified list
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
# Output: 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    k = 6
    solution = Solution()
    new_head = solution.reverseKGroup(head, k)
    
    # Print the modified list
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
# Output: 1 -> 2 -> 3 -> 4 -> 5 -> None (since k > length of list, no reversal occurs)
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    k = 5
    solution = Solution()
    new_head = solution.reverseKGroup(head, k)
    
    # Print the modified list
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")