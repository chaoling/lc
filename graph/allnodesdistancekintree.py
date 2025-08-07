'''
863. All Nodes Distance K in Binary Tree

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
from typing import List


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        '''
        iterate all nodes in the tree start from the root, in a bfs manner, and whenever it hits target, 
        store all nodes that are k distance away from the target, keep bfs until it reaches k distance again or the end of the 
        tree, whichever condition is met first.
        since all the node value are unique, we can use that to server as the key to the dictionary val:level
        '''
        ans = []
        # before your BFS, initialize a parent map
        parent = {root: None}

        # do a simple BFS (or DFS) just to populate parent pointers
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                parent[node.left] = node
                q.append(node.left)
            if node.right:
                parent[node.right] = node
                q.append(node.right)
       
        visited= set()
        # Now find the target node and do BFS from that node:
        q = deque([(target,0)])
        while q:
            node, level = q.popleft()
            visited.add(node)
            if level == k:
                ans.append(node.val)
            if level < k:
                for nei in (node.left, node.right, parent[node]):
                    if nei and nei not in visited:
                        q.append((nei,level+1))
        return ans