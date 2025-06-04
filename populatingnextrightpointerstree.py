'''
117. Populating Next Right Pointers in Each Node II
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
Medium
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100
 

Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
'''

# Definition for a Node.

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        '''
        level order traversal?
        use a fifo or queue to maintain order
        then how do you find the next pointer for each node?
        obviously, the root node's next pointer is None
        then for the subtree:
        if it has left subtree, it's root node's next pointer points to the root node's of the right subtree
        the right subtree's root's next pointer points to None always
        the number of nodes in each binary tree level order is 2^n, including null node
        '''
        from collections import deque
        if not root:
            return None
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i < size - 1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:  
                    q.append(node.right)
        return root 

if __name__ == "__main__":
    # Example usage:
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    solution = Solution()
    connected_root = solution.connect(root)

    # Print the next pointers
    print(connected_root.left.next.val)  # Should print 3
    print(connected_root.left.left.next.val)  # Should print 5
    print(connected_root.left.right.next.val)  # Should print None
    print(connected_root.right.right.next)  # Should print None
    print(connected_root.next)  # Should print None (root's next is None)
    print(connected_root.left.next.val)  # Should print 3
    print(connected_root.right.next)  # Should print None (right child of root has no next)
    print(connected_root.left.left.next.val)  # Should print 5 (left child of left child points to right child of left child)
    print(connected_root.left.right.next)  # Should print None (right child of left child has no next)
    print(connected_root.right.left)  # Should print None (right child of right child has no left child)
    print(connected_root.right.right.next)  # Should print None (right child of right child has no next)
    print(connected_root.left.left.next.val)  # Should print 5 (left child of left child points to right child of left child)
    print(connected_root.left.right.next)  # Should print None (right child of left child has no next)
    print(connected_root.right.left)  # Should print None (right child of right child has no left child)    