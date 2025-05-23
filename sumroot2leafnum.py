'''
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

 

Example 1:


Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:


Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.
'''
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


from typing import Optional
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        '''
        pre/in/post order traversal or in order traversal?
        just call it dfs
        along each path, get the val of each node and multiply by 10 for each level [0-leaf_level]
        max numbers: 2^n
        question: shall we do the calculation/summation along the path while doing the traversal?
        '''
        def dfs(node: TreeNode, total):
            if node is None:
                return 0
            total = total * 10 + node.val
            if node.left is None and node.right is None:
                #reached the leaf level: add this to total path sum
                return total
            return dfs(node.left, total) + dfs(node.right, total)

        return dfs(root, 0)
if __name__ == "__main__":
    # Example usage:
    # Constructing a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    result = solution.sumNumbers(root)
    print(result)  # Output: 262 (124 + 125 + 13)