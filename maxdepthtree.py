'''
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) ->int:
            if not node:
                return 0
            else:
                return max(1 + dfs(node.left), 1 + dfs(node.right))

        return dfs(root)
# Example usage:
if __name__ == "__main__":
    # Constructing a binary tree for testing
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    
    solution = Solution()
    print(solution.maxDepth(root))  # Output: 3

    # Testing with a single node tree
    single_node_tree = TreeNode(1)
    print(solution.maxDepth(single_node_tree))  # Output: 1

    # Testing with an empty tree
    empty_tree = None
    print(solution.maxDepth(empty_tree))  # Output: 0