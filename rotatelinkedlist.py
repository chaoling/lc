'''
61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
'''
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

from typing import Optional
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        observations: slice the list with last k members in a group
        eg: 1,2,3 | 4,5
        then make the tail group the head group, make the head group the tail group, fix the next pointer when necessary
        observation 2: reverse the linked list
        1,2,3,4,5 -> 5,4,3,2,1
        now, reverse the first k elements: 4->5->3->2->1
        finally, reverse the remaining elements: 4->5->1->2->3
        '''
        def getLength(head):
            length = 0
            current = head
            while current:
                current = current.next
                length += 1
            return length

        def reverse(head: Optional[ListNode], k=-1):
            '''
            return the size of the list and the node of the last element after reverse,
            if entire list, then node is the head node,
            if first k elements, then node is the kth element after reverse.
            '''
          
            pre, cur = None, head
            # (pre)->(cur)->(nxt)->()
            # (pre)<-(cur)->(nxt)
            # ()<-(pre)->(cur)->(nxt)
            count = 0
            while cur and (k < 0 or count < k):
                # reverse the linked list
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
                count += 1
            return pre, cur # the node of the last element after reverse, if k < 0, then cur is None

        if not head or not head.next:
            return head #do nothing, the linked list don't need to do anything else.
        n = getLength(head)
        k = k % n
        if k == 0:
            return head
        #1st reverse the entire linked list
        head, _ = reverse(head)
        #now reverse the first k elements in the list
        new_head, remainder = reverse(head, k)
        #now reverse the remaining elements in the list
        if remainder:
            tail, _ = reverse(remainder)
            # fix the middle next pointer
            head.next = tail
        return new_head 

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next


if __name__ == "__main__":
    head = create_linked_list([1,2,3,4,5])
    k = 2
    sol = Solution()
    new_head = sol.rotateRight(head, k)
    print_linked_list(new_head)  # Expected output: 4 -> 5 -> 1 -> 2 -> 3
    head = create_linked_list([0,1,2])
    k = 4
    new_head = sol.rotateRight(head, k)
    print_linked_list(new_head)  # Expected output: 2 -> 0 -> 1
    head = create_linked_list([1,2])
    k = 1
    new_head = sol.rotateRight(head, k)
    print_linked_list(new_head)  # Expected output: 2 -> 1
    head = create_linked_list([1])
    k = 0
    new_head = sol.rotateRight(head, k)
    print_linked_list(new_head)  # Expected output: 1
    head = create_linked_list([])
    k = 5
    new_head = sol.rotateRight(head, k)
    print_linked_list(new_head)  # Expected output: (nothing, since the list is empty)
    head = create_linked_list([1,2,3,4,5,6,7])
    k = 3
    new_head = sol.rotateRight(head, k)
    print_linked_list(new_head)  # Expected output: 5 -> 6 -> 7 -> 1 -> 2 -> 3 -> 4