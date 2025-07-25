'''
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 
Example 1:


Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
Example 2:


Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
Example 3:


Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.

Constraints:

The number of nodes in the list is in the range [1, 105].
1 <= Node.val <= 105
'''
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        use slow and fast pointer to find the middle-1 of a linked list
        do the deletion of the next: cur->next = cur->next-next
        return the head
        '''
        fast = head
        dummy = ListNode(val=0, next=head) #add a dummy node in front of the current head
        slow = dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # at this point, slow is at the middle-1 of the linked list
        # now delete the next node of slow
        if slow.next:
            slow.next = slow.next.next
        return dummy.next

if __name__ == "__main__":
    sol = Solution()
    # create a linked list 1->2->3->4->5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    # delete the middle node
    new_head = sol.deleteMiddle(head)
    # print the new linked list
    cur = new_head
    while cur:
        print(cur.val, end="->" if cur.next else "\n")
        cur = cur.next
