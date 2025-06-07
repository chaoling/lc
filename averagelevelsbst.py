'''
637. Average of Levels in Binary Tree
https://leetcode.com/problems/average-of-levels-in-binary-tree/
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:


Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''
# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root) -> List[float]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_sum = 0
            level_count = len(queue)
            #At the start of each iteration of the outer while queue: loop, 
            # the queue only contains all nodes of the current level, (why? because we only add children of nodes that were processed in the previous level)
            # added during the previous level’s processing.
            
            for _ in range(level_count):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level_sum / level_count)
        
        return result
        
    def averageOfLevels_mine(self, root: Optional[TreeNode]) -> List[float]:
        '''
        algorithm: do the level order traversal, calculate average for each level
        '''
        ans = []
        q = deque()
        prelevel, level, count, s = 0, 0, 0, 0
        q.append((root,level))
        while q:
            node, level = q.popleft()
            if level == prelevel:
                count += 1
                s += node.val
            else:
                ans.append(s/count)
                s, count = node.val, 1  #reset the counter and sum
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
            prelevel = level
        ans.append(s/count)
        return ans