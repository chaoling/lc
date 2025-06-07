'''
199. Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:
    1            <---
    / \
      2   3          <---
    \
     5            <---
      \
        4          <---

Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:



Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []

 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        level order traversal, only pick the right most nodes
        '''
        
        if not root:
            return []
        ans = []
        q = deque()
        q.append((root,0))
        level, pre_level = 0, 0
        pre_node = None
        while q:
            node, level = q.popleft() #note: queue should use popleft, not pop! (pop is a stack)
            if level > pre_level: #when level changes, the last node is the rightmost view of that level
                ans.append(pre_node.val)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
            pre_node,pre_level = node, level
        
        ans.append(pre_node.val) #the last node on last level should not be forgotten. 
        return ans

if __name__ == "__main__":
    def stringToTreeNode(data):
        if not data or data == "[]":
            return None
        data = data.strip()[1:-1]
        if not data:
            return None
        nodes = [None if val == "null" else TreeNode(int(val)) for val in data.split(",")]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    def treeNodeToString(root):
        if not root:
            return "[]"
        output = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                output.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                output.append("null")
        while output and output[-1] == "null":
            output.pop()
        return "[" + ",".join(output) + "]"

    root = stringToTreeNode("[1,2,3,null,5,null,4]")
    print(treeNodeToString(root))
    print(Solution().rightSideView(root))  # Output: [1, 3, 4]
    root = stringToTreeNode("[1,null,3]")
    print(treeNodeToString(root))
    print(Solution().rightSideView(root))  # Output: [1, 3]
    root = stringToTreeNode("[1,2,3,4,null,null,5]")
    print(treeNodeToString(root))
    print(Solution().rightSideView(root))  # Output: [1, 3, 5]
