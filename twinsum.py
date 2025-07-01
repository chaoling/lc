'''
2130 Maximum Twin Sum of a Linked List
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

Example 1:


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 
Example 2:


Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
Example 3:


Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
 
Constraints:

The number of nodes in the list is an even integer in the range [2, 105].

'''
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        '''
        if it is a double linked list, then you can use two pointers from both ends and 
        add them together in O(N/2) 
        or:
        I can reverse the linked list, : 5->4->2->1
                                         1->2->4->5
        then add each sum till mid of the list.
        '''
        from typing import Optional, List, Tuple
        def linkedlist2array(head: Optional[ListNode])->Tuple[int, List[int]]:
            if not head:
                return 0, []
            n = 0
            res = []
            cur = head
            while cur:
                n += 1
                res.append(cur.val)
                cur = cur.next
            return n, res
            
        n, l = linkedlist2array(head)
        res = 0
        for i in range(n//2):
            res = max(res, head.val + l[n-i-1])
            head = head.next
        return res
    
    def pairSum2(self, head: Optional[ListNode]) -> int:
        '''
        This is a more efficient way to do it, using two pointers.
        '''
        slow = fast = head
        stack = []
        
        # Find the middle of the linked list
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        max_sum = 0
        
        # Compare the first half with the second half
        while slow:
            max_sum = max(max_sum, stack.pop() + slow.val)
            slow = slow.next
            
        return max_sum

# Example usage:
if __name__ == "__main__":
    # Create a linked list: 5 -> 4 -> 2 -> 1
    head = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
    
    # Create a solution instance and call the method
    solution = Solution()
    print(solution.pairSum(head))  # Output: 6