# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(left, right):
            if not left and not right:
                return True
            elif not left or not right or left.val != right.val:
                return False
            else:
                return helper(left.left,right.right) and helper(left.right,right.left)
        if not root:
            return False
        else:
            return helper(root.left, root.right)

if __name__ == "__main__":
    s = Solution()
    #     1
    #    / \
    #   2   2
    #  / \ / \
    # 3  4 4  3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print(s.isSymmetric(root)) # True
    
    #     1
    #    / \
    #   2   2
    #    \   \
    #     3   3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)
    print(s.isSymmetric(root)) # False