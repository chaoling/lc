'''
1372. Longest ZigZag Path in a Binary Tree
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

 
Example 1:

Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
Example 2:


Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
Example 3:

Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 5 * 104].
1 <= Node.val <= 100
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def __init__(self):
        self.max_length = 0

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node:TreeNode, dir:str) -> int:
            if not node:
                return 0
            if dir == 'left':
                return 1 + dfs(node.right, "right")
            else: #dir == 'right'
                return 1 + dfs(node.left, "left")

        croot = max(dfs(root, "left"), dfs(root, "right")) - 1
        cl = self.longestZigZag(root.left) if root.left else 0
        cr = self.longestZigZag(root.right) if root.right else 0
        return max(croot, cl, cr)
    
    def longestZigZag2(self, root: Optional[TreeNode]) -> int:
        '''
        This is the O(N) version.
        Instead of calling longestZigZag recursively on every node, do a single post-order DFS traversal of the tree and compute the longest ZigZag path as you go.
        At each node, keep track of:
        The longest ZigZag path starting by going left from that node.
        The longest ZigZag path starting by going right from that node.
        Return a tuple like (left_zigzag, right_zigzag) from your DFS, where:

        left_zigzag is the length of the ZigZag path if you go left first.
        right_zigzag is the same for right.
        This allows the parent node to compute its ZigZag based on its child’s results.
        '''
        def dfs(node:TreeNode) -> tuple[int, int]:
            if not node:
                return (-1, -1) # Base case: return -1 to offset +1 below
            left = dfs(node.left)
            right = dfs(node.right)

            left_zigzag = 1 + left[1]
            right_zigzag = 1 + right[0]

            self.max_length = max(self.max_length, left_zigzag, right_zigzag)
            return (left_zigzag, right_zigzag)
        
        dfs(root)
        return self.max_length
            
# Example usage:
if __name__ == "__main__":  
    sol = Solution()
    # Create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    
    # Find the longest zigzag path
    print(sol.longestZigZag(root))  # Output: 3
    print(sol.longestZigZag2(root))  # Output: 3