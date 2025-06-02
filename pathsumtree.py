'''
https://leetcode.com/problems/path-sum/
112. Path Sum
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
        do dfs on trees and backtrack?
        another trick: when navigate along the tree branch from root to leaf,
        subtrck the value of the nodes along the way, when it finally reaches zero
        return True.
        '''
        def dfs(root, targetSum):
            if not root:
                return False
            if not root.left and not root.right: #reached leaf node
                return targetSum == root.val
            else:
                return (dfs(root.left, targetSum - root.val) or
                        dfs(root.right, targetSum - root.val))
        
        return dfs(root, targetSum)

if __name__ == "__main__":
    # Example usage:
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    targetSum = 22
    solution = Solution()
    print(solution.hasPathSum(root, targetSum))  # Output: True
    # Test with an empty tree
    empty_root = None
    print(solution.hasPathSum(empty_root, 0))  # Output: False
    # Test with a tree that does not have the target sum
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    print(solution.hasPathSum(root2, 5))  # Output: False
    # Test with a single node tree
    single_node_root = TreeNode(5)  
    print(solution.hasPathSum(single_node_root, 5))  # Output: True