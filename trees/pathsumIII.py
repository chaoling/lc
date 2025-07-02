'''
437 Path Sum III
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).


Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 
Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        '''
        at any node downward, if the path sum meets the targetsum, 
        count + 1
        '''
        def dfs(node: TreeNode, curr_sum: int) -> int:
            if not node:
                return 0
            curr_sum += node.val
            count = 1 if curr_sum == targetSum else 0
            count += dfs(node.left, curr_sum) 
            count += dfs(node.right, curr_sum)
            return count

        if not root:
            return 0
        return dfs(root, 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        '''
        This function is a wrapper to call the dfs function
        and handle the case where the root is None.
        use prefix sum to count the number of paths that sum to targetSum
        '''
        if not root:
            return 0
        def dfs(node: TreeNode, curr_sum: int, prefix_sums: dict) -> int:
            if not node:
                return 0
            
            curr_sum += node.val
            count = prefix_sums.get(curr_sum - targetSum, 0)
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
            
            count += dfs(node.left, curr_sum, prefix_sums)
            count += dfs(node.right, curr_sum, prefix_sums)
            
            # Decrement the count of the current sum in the prefix sums
            prefix_sums[curr_sum] -= 1
            
            return count

# Example usage:
if __name__ == "__main__":
    # Create a sample tree for testing
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(11)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.right = TreeNode(1)

    targetSum = 8
    solution = Solution()
    print(solution.pathSum(root, targetSum))  # Output: 3