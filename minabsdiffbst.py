# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        '''
        property of BST:
        inorder traversal makes a sorted list
        '''
        self.prev = None
        self.min_diff = float('inf')
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, abs(node.val - self.prev))
            self.prev = node.val
            inorder(node.right)
        
        inorder(root)
        return self.min_diff
        # Alternatively, we could use a stack to perform the inorder traversal iteratively.
        # However, the recursive approach is more straightforward and easier to read.
        # If we wanted to implement the iterative version, it would look like this:
        # stack = []
        # current = root            
        # while stack or current:
        #     while current:
        #         stack.append(current)
        #         current = current.left
        #     current = stack.pop()
        #     if self.prev is not None:
        #         self.min_diff = min(self.min_diff, abs(current.val - self.prev))
        #     self.prev = current.val
        #     current = current.right
        # return self.min_diff
        # The iterative version would also yield the same result, but the recursive version is more elegant for this problem.
        # Note: The iterative version is commented out as it is not needed for the solution.
        # The recursive version is sufficient and preferred for its simplicity.
        # The time complexity is O(n) where n is the number of nodes in the tree,
        # and the space complexity is O(h) where h is the height of the tree due to recursion stack.
        # Both versions achieve the same time and space complexity.
        # The recursive version is generally more concise and easier to understand for this problem.
        # The iterative version is more verbose and less intuitive for this specific problem.
        # Both versions will yield the same minimum difference between values of any two nodes in the BST.
        # The choice between recursive and iterative is often a matter of personal or team preference,
        # but for this problem, the recursive approach is more elegant and straightforward.
if __name__ == "__main__":
    # Example usage:
    # Construct a binary search tree and call the function
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(6, None, TreeNode(7))
    solution = Solution()
    print(solution.getMinimumDifference(root))  # Output should be the minimum difference between any two nodes in the BST.