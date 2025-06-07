'''
222. Count Complete Tree Nodes
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.
 
Example 1:

Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
'''
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
from typing import Optional
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        '''
        use dfs to run into the leftmost leaf, calculate the depth h (0->...)
        number of nodes = 2^h - 1 + number of leaves
        '''
        def get_depth(node):
            h = 0
            while node and node.left:
                h += 1
                node = node.left
            return h

        def exists(index, depth, node):
            # find if the leaf node exist using binary search -> O(logN)
            left, right = 0, 2**depth - 1
            for _ in range(depth):
                mid = left + (right - left ) // 2
                if index <= mid:
                    # look inside left half tree
                    node = node.left
                    right = mid
                elif index > mid:
                    # look inside right half tree
                    node = node.right
                    left = mid + 1
                if not node:
                    return False
            return True
        if not root:
            return 0
        depth = get_depth(root)
        if depth == 0:
            return 1
        left, right = 0, 2**(depth) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if exists(mid, depth, root):
                left = mid + 1
            else:
                right = mid - 1
        
        return 2**(depth) - 1 + left
# Time: O(logN * logN) -> O(logN)
# Space: O(logN) -> O(1)
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    print(Solution().countNodes(root))  # Output: 6
    root = TreeNode(1)
    print(Solution().countNodes(root))  # Output: 1
    root = None
    print(Solution().countNodes(root))  # Output: 0