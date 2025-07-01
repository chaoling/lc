'''
1448 Count Good Nodes in Binary Tree
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
 

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        do dfs on tree path, for each node, if the value is max 
        on the path list, then good count +1
        '''
        
        def dfs (root: TreeNode, max_val: int) -> int:
            if not root:
                return 0
            #update the max_val
            is_good = 1 if root.val >= max_val else 0
            new_max = max(max_val, root.val)
            return is_good + dfs(root.left, new_max) + dfs (root.right, new_max)
            
        return dfs(root, float('-inf'))

# Example usage:
if __name__ == "__main__":
    # Create a sample tree for testing
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)

    solution = Solution()
    print(solution.goodNodes(root))  # Output: 4