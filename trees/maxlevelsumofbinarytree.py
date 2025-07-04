'''
1161. Maximum Level Sum of a Binary Tree
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:

Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
'''
# Definition for a binary tree node.
from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        '''
        do level order traversal with deque
        keep track of level and the sum of nodes at each level
        '''
        q = deque([(root,1)])
        pre_level, cur_sum = 1, 0
        max_sum, max_level = float('-inf'), 1
        while q:
            node, level = q.popleft()
            if pre_level != level:
                if max_sum < cur_sum:
                    max_sum = cur_sum
                    max_level = pre_level
                cur_sum = 0
                pre_level = level
            cur_sum += node.val
            
            if node.left:
                q.append((node.left,level + 1))
            if node.right:
                q.append((node.right, level + 1))
        if max_sum < cur_sum:
            max_sum = cur_sum
            max_level = pre_level
        return max_level

if __name__ == "__main__":
    sol = Solution()
    # Create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    
    print(sol.maxLevelSum(root))  # Output: 2, since level 2 has the maximum sum (2 + 3 = 5)