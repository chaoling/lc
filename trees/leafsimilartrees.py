'''
872. Leaf-Similar Trees
https://leetcode.com/problems/leaf-similar-trees/
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
 

Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
'''
# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        '''
        do dfs search and put all leaf nodes in to a list
        then compare lists
        '''
        def dfs(root: Optional[TreeNode], leaves: List):
            if not root:
                return
            if not root.left and not root.right:
                #found leaf node
                leaves.append(root.val)
                return #leaves
            else:
                if root.left:
                    dfs(root.left, leaves)
                if root.right:
                    dfs(root.right, leaves)
        
        leaves1 = []
        leaves2 = []
        
        dfs(root1, leaves1)
        dfs(root2, leaves2)
      
        return leaves1 == leaves2

# Example usage:
if __name__ == "__main__":
    # Create a sample tree for testing
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)

    root2 = TreeNode(6)
    root2.left = TreeNode(7)
    root2.right = TreeNode(8)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)

    solution = Solution()
    print(solution.leafSimilar(root1, root2))  # Output: True or False based on leaf similarity